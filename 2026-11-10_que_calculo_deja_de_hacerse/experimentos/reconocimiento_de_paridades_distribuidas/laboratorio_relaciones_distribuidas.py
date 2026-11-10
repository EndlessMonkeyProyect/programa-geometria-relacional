#!/usr/bin/env python3
"""GR3–ROSI–CAG | relaciones XOR distribuidas y ocultas por puertas CNF.
   Biblioteca estándar, semilla fija, extracción DESDE CNF sin metadatos.
   Detecta una clase restringida: circuitos XOR construidos por OR/AND/AND-NOT
   con extensión única; las restricciones finales pueden ser OR sobre entradas.
"""
from collections import Counter
from itertools import product
import random, time, json, argparse, statistics, os


def norm(cl):
    d={}
    for l in cl:
        if abs(l) in d and d[abs(l)]!=l: return None
        d[abs(l)]=l
    return tuple(sorted(d.values(), key=lambda l:(abs(l),l<0)))


def emit_gate(out, op, a, b):
    if op == 'OR':
        return [(-a,out),(-b,out),(a,b,-out)]
    if op == 'AND':
        return [(-out,a),(-out,b),(out,-a,-b)]
    raise ValueError(op)

class Builder:
    def __init__(self,n):
        self.n=n; self.top=n; self.cl=[]
    def gate(self,op,a,b):
        self.top+=1;z=self.top;self.cl+=emit_gate(z,op,a,b);return z
    def xor2(self,a,b):
        t=self.gate('OR',a,b)
        u=self.gate('AND',a,b)
        return self.gate('AND',t,-u)
    def xor3(self,a,b,c,rhs,unit=True):
        w=self.xor2(a,b)
        z=self.xor2(w,c)
        if unit:self.cl.append((z,) if rhs else (-z,))
        return z
    def near3(self,a,b,c,rhs,missing):
        z=self.xor3(a,b,c,rhs,unit=False)
        lits=[v if bit else -v for v,bit in zip((a,b,c),missing)]
        h=self.gate('AND',lits[0],lits[1])
        p=self.gate('AND',h,lits[2])
        acc=self.gate('OR',z if rhs else -z,p)
        self.cl.append((acc,))


def gen(n, extra, seed, shuffled=True, partial=0, long_edges=0):
    """Conecta todas las variables primarias mediante ternas solapadas, ciclo.
    Se garantiza al menos una solución por siembra. Se permutan TODOS los ID.
    """
    rng=random.Random(seed); prim=[rng.randrange(2) for _ in range(n)]
    b=Builder(n); eq=[];near=[]
    for i in range(0,n,2):
        triple=(1+i,1+(i+1)%n,1+(i+2)%n)
        rhs=prim[triple[0]-1]^prim[triple[1]-1]^prim[triple[2]-1]
        if len(near)<partial and (i//2)%2==0:
            pats=[q for q in product((0,1),repeat=3) if (q[0]^q[1]^q[2])!=rhs]
            miss=rng.choice(pats);b.near3(*triple,rhs,miss);near.append((triple,rhs,miss))
        else:
            b.xor3(*triple,rhs);eq.append((triple,rhs))
    used={frozenset(x[0]) for x in eq}|{frozenset(x[0]) for x in near}
    for _ in range(long_edges):
        while True:
            triple=tuple(rng.sample(range(1,n+1),3))
            if frozenset(triple) not in used:
                used.add(frozenset(triple));break
        rhs=prim[triple[0]-1]^prim[triple[1]-1]^prim[triple[2]-1]
        b.xor3(*triple,rhs);eq.append((triple,rhs))
    ors=[]
    for j in range(extra):
        ids=tuple(rng.sample(range(1,n+1),3));false=[rng.randrange(2) for _ in ids]
        if all(prim[v-1]==q for v,q in zip(ids,false)): false[0]^=1
        cl=tuple(-v if q else v for v,q in zip(ids,false))
        b.cl.append(cl);ors.append(cl)
    raw=[norm(c) for c in b.cl]
    assert None not in raw
    if shuffled:
        perm=list(range(1,b.top+1));rng.shuffle(perm)
        rel={i:perm[i-1] for i in range(1,b.top+1)}
        raw=[norm(tuple((1 if x>0 else -1)*rel[abs(x)] for x in cl)) for cl in raw]
        rng.shuffle(raw)
        rel_prim=[rel[v] for v in range(1,n+1)]
    else:
        rel_prim=list(range(1,n+1))
    return {'cnf':raw,'variables':b.top,'primary':rel_prim,'eq':eq,'near':near,'ors':ors,'planted':prim}


def scan_gates(cnf):
    clauses=set(cnf);gates={};used=set();ambig=[]
    for cl in sorted(clauses, key=lambda c:(len(c),c)):
        if len(cl)!=3:continue
        cand=[]
        for outlit in cl:
            other=[l for l in cl if l!=outlit]
            if len(other)!=2:continue
            if outlit<0:
                z=-outlit;a,b=other
                pair={norm((-a,z)),norm((-b,z))}
                if pair<=clauses:cand.append((z,'OR',a,b,pair))
            if outlit>0:
                z=outlit;a,b=[-l for l in other]
                pair={norm((a,-z)),norm((b,-z))}
                if pair<=clauses:cand.append((z,'AND',a,b,pair))
        if len(cand)>1:ambig.append(cl)
        if len(cand)==1:
            z,op,a,b,pair=cand[0]
            if z in gates or (used & (pair|{cl})):
                raise ValueError('puertas ambiguas/superpuestas')
            gates[z]=(op,a,b);used|=pair|{cl}
    if ambig:raise ValueError('no hubo unicidad sintáctica')
    units=[c for c in clauses-used if len(c)==1]
    leftovers=[c for c in clauses-used if len(c)>1]
    if any(len(c)==2 for c in leftovers):raise ValueError('residuos binarios fuera de puertas')
    if any(len(c)>3 for c in leftovers):raise ValueError('residuos >3')
    return gates,units,leftovers,used


def near_from_circuit(gates,xor,units,sources):
    xor_map={z:(a,b) for z,a,b in xor};used=set();out=[]
    def expr(v,seen=None):
        if v in sources:return {v}
        if v not in xor_map:raise ValueError('relación no afín')
        if seen is None: seen=set()
        if v in seen:raise ValueError('ciclo de paridad')
        seen=seen|{v}; a,b=xor_map[v]
        return expr(a,seen)^expr(b,seen)
    for (lit,) in units:
        if lit<=0 or lit not in gates or gates[lit][0]!='OR':continue
        acc=lit;_,u,v=gates[acc]
        for xor_l,p in ((u,v),(v,u)):
            if abs(xor_l) not in xor_map or p<=0 or p not in gates:continue
            pg=gates[p]
            if pg[0]!='AND':continue
            for h,c in ((pg[1],pg[2]),(pg[2],pg[1])):
                if h<=0 or h not in gates or gates[h][0]!='AND':continue
                q=gates[h];lits=[q[1],q[2],c]
                vs=[abs(z) for z in lits]
                if len(set(vs))!=3 or any(v not in sources for v in vs):continue
                support=expr(abs(xor_l))
                if support!=set(vs):continue
                rhs=int(xor_l>0)
                missing={abs(z):int(z>0) for z in lits}
                if sum(missing.values())%2==rhs:continue
                used|={acc,p,h}
                out.append((tuple(sorted(support)),rhs,tuple(missing[v] for v in sorted(support))))
                break
            else:continue
            break
    return out,used


def extract(cnf,nvars):
    cnf=[norm(c) for c in cnf];assert None not in cnf
    gates,units,leftovers,used=scan_gates(cnf)
    inner=set();xor=[]
    used_by=Counter()
    for z,(op,a,b) in gates.items():
        for i in (a,b):used_by[abs(i)]+=1
    for z,(op,a,b) in gates.items():
        if op!='AND':continue
        t=next((v for v in (a,b) if v>0 and v in gates and gates[v][0]=='OR'),None)
        u=next((-v for v in (a,b) if v<0 and -v in gates and gates[-v][0]=='AND'),None)
        if t is None or u is None:continue
        t_in=gates[t][1:];u_in=gates[u][1:]
        if set(t_in)!=set(u_in) or len(set(t_in))!=2:continue
        if not all(v>0 for v in t_in):continue
        if used_by[t]!=1 or used_by[u]!=1:continue
        xor.append((z,t_in[0],t_in[1]));inner.update((t,u))
    xor_outputs={z for z,a,b in xor}
    sources=set(range(1,nvars+1))-set(gates)
    near,helpers=near_from_circuit(gates,xor,units,sources)
    if (xor_outputs|inner|helpers)!=set(gates): raise ValueError('puerta no reducible a XOR ni a ROSI')
    if (xor_outputs&inner) or ((xor_outputs|inner)&helpers):raise ValueError('variables auxiliares solapadas')
    if any(abs(l) in inner|helpers for cl in leftovers for l in cl):raise ValueError('OR externa usa variable interna')
    if any(abs(l) not in sources for cl in leftovers for l in cl):raise ValueError('OR externa no primaria')
    if any(abs(l) in inner for z,a,b in xor for l in (a,b)):raise ValueError('entrada XOR no afín')
    for z in helpers:
        if z not in {a for (a,) in units} and used_by[z]!=1:raise ValueError('auxiliar ROSI compartido')
    usable=sorted(sources|xor_outputs)
    index={v:i for i,v in enumerate(usable)}
    if any(v not in index for z,a,b in xor for v in (a,b)):raise ValueError('entrada XOR fuera de la familia')
    rows=[]
    for z,a,b in xor:rows.append((sum(1<<index[v] for v in (z,a,b)),0))
    for (l,) in units:
        if abs(l) in helpers:
            if l<0 or l not in {p for p in helpers if used_by[p]==0}:raise ValueError('unidad ROSI inválida')
            continue
        if abs(l) not in sources|xor_outputs:raise ValueError('unidad inválida')
        rows.append((1<<index[abs(l)],int(l>0)))
    ors=[[ (index[abs(l)],int(l<0)) for l in cl] for cl in leftovers]
    near_eq=[]
    for vs,rhs,miss in near:
        near_eq.append((sum(1<<index[v] for v in vs),rhs,tuple((index[v],bit) for v,bit in zip(vs,miss))))
    assert len(used)+len(units)+len(leftovers)==len(set(cnf))
    return {'n_sources':len(sources),'n_gate_outputs':len(gates),'xor_gates':len(xor),
            'n_affine_vars':len(usable),'n_or':len(ors),'n_near':len(near_eq),
            'rows':rows,'ors':ors,'near':near_eq,
            'all_clauses_accounted':True,'no_3of4_parity_templates':check_no_local_roots(cnf)}


def check_no_local_roots(cnf):
    d={}
    for c in cnf:
        if len(c)!=3: continue
        v=tuple(sorted(abs(l) for l in c))
        for parity in (0,1):
            if sum(l<0 for l in c)%2==parity:
                d[v,parity]=d.get((v,parity),0)+1
    return all(q<=2 for q in d.values())

class Gauss:
    def __init__(self):self.b={};self.ops=0
    def add(self,m,r):
        old=self.b
        for pv in sorted(old, reverse=True):
            if (m>>pv)&1:
                bm,br=old[pv];m^=bm;r^=br;self.ops+=1
        if m==0:return r==0
        old[m.bit_length()-1]=(m,r)
        return True
    def copy(self):
        c=Gauss();c.b=self.b.copy();return c


def count_extracted(d):
    t0=time.perf_counter();base=Gauss()
    if not all(base.add(m,r) for m,r in d['rows']):
        return {'count':0,'ms':1000*(time.perf_counter()-t0),'leaves':0,'gauss_ops':base.ops,'base_rank':len(base.b),'active':0}
    ors=d['ors'];near=d['near']; stats={'leaves':0,'ops':base.ops,'branches':0}
    def ie(i,B,s,active):
        if i==len(active):
            stats['leaves']+=1;return s*(1<<(d['n_affine_vars']-len(B.b)))
        a=ie(i+1,B,s,active)
        sub=B.copy();ok=True
        for v,bit in active[i]:
            if not sub.add(1<<v,bit):ok=False;break
        stats['ops']+=sub.ops
        if ok:a+=ie(i+1,sub,-s,active)
        return a
    def complete(B):
        stats['branches']+=1;active=[]
        for clause in ors:
            b2=B.copy();ok=all(b2.add(1<<v,bit) for v,bit in clause)
            stats['ops']+=b2.ops
            if not ok: continue
            if len(b2.b)==len(B.b):return 0
            active.append(clause)
        return ie(0,B,1,active)
    def branch(i,B):
        if i==len(near):return complete(B)
        mask,rhs,miss=near[i];total=0
        bb=B.copy()
        if bb.add(mask,rhs):total+=branch(i+1,bb)
        stats['ops']+=bb.ops
        bb=B.copy();ok=True
        for v,val in miss:
            if not bb.add(1<<v,val):ok=False;break
        stats['ops']+=bb.ops
        if ok:total+=branch(i+1,bb)
        return total
    val=branch(0,base)
    return {'count':val,'ms':1000*(time.perf_counter()-t0),'leaves':stats['leaves'],
            'gauss_ops':stats['ops'],'base_rank':len(base.b),'n_near_branches':stats['branches'],
            'free_bits_if_no_OR':d['n_affine_vars']-len(base.b)}


def direct_primary(n,eq,near,ors):
    # cálculo independiente desde estructura ORIGINAL del generador
    A=Gauss()
    for vs,r in eq:
        if not A.add(sum(1<<(v-1) for v in vs),r):return 0
    def or_ie(i,B):
        if i==len(ors):return 1<<(n-len(B.b))
        res=or_ie(i+1,B);sub=B.copy();valid=True
        for lit in ors[i]:
            if not sub.add(1<<(abs(lit)-1),int(lit<0)):
                valid=False;break
        if valid:res-=or_ie(i+1,sub)
        return res
    def near_rec(i,B):
        if i==len(near):return or_ie(0,B)
        vs,rhs,miss=near[i];result=0;bb=B.copy()
        if bb.add(sum(1<<(v-1) for v in vs),rhs):result+=near_rec(i+1,bb)
        bb=B.copy();ok=True
        for v,val in zip(vs,miss):
            if not bb.add(1<<(v-1),val):ok=False;break
        if ok:result+=near_rec(i+1,bb)
        return result
    return near_rec(0,A)


def truth_eval(nprim,gen):
    """Segundo control: evalúa todas las asignaciones PRIMARIAS, simula todas
       las puertas por las ecuaciones generadoras y cuenta los satisfactores.
       No usa el extractor ni la eliminación gaussiana."""
    eq=gen['eq'];near=gen['near'];ors=gen['ors'];count=0
    for bits in product((0,1),repeat=nprim):
        if any((bits[a-1]^bits[b-1]^bits[c-1])!=r for (a,b,c),r in eq):continue
        if any(((bits[a-1]^bits[b-1]^bits[c-1])!=r and (bits[a-1],bits[b-1],bits[c-1])!=miss) for (a,b,c),r,miss in near):continue
        if any(not any(bits[abs(v)-1] != int(v<0) for v in cl) for cl in ors):continue
        count+=1
    return count

class Stop(Exception): pass

def dpll_cnf(n,cnf,maxnodes=12000,seconds=2.0):
    start=time.perf_counter();nodes=0;branches=0
    def solve(cnf, assignment):
        nonlocal nodes, branches
        nodes+=1
        if nodes>maxnodes or time.perf_counter()-start>seconds:raise Stop()
        while True:
            simplified=[];units=[]
            for cl in cnf:
                found=False;rem=[]
                for lit in cl:
                    if abs(lit) in assignment:
                        if assignment[abs(lit)]==(lit>0):found=True;break
                    else:rem.append(lit)
                if found:continue
                if not rem:return 0
                if len(rem)==1:units.append(rem[0])
                simplified.append(tuple(rem))
            if not units:
                cnf=simplified;break
            added=False
            for lit in units:
                v=abs(lit);b=lit>0
                if v in assignment:
                    if assignment[v]!=b:return 0
                else:assignment[v]=b;added=True
            if not added:
                cnf=simplified;break
            cnf=simplified
        if not cnf:return 1<<(n-len(assignment))
        degrees=Counter(abs(l) for cl in cnf for l in cl)
        v=max(degrees,key=lambda v:(degrees[v],-v));branches+=1
        aa=assignment.copy();aa[v]=False
        bb=assignment.copy();bb[v]=True
        return solve(cnf,aa)+solve(cnf,bb)
    try:
        ans=solve(cnf,{})
        return {'count':ans,'nodes':nodes,'branches':branches,'ms':1000*(time.perf_counter()-start),'complete':True}
    except Stop:
        return {'count':None,'nodes':nodes,'branches':branches,'ms':1000*(time.perf_counter()-start),'complete':False}


def component_count(n,cnf):
    par=list(range(n+1))
    def root(i):
        while par[i]!=i:
            par[i]=par[par[i]];i=par[i]
        return i
    for c in cnf:
        ids=[abs(l) for l in c]
        for j in ids[1:]:
            a,b=root(ids[0]),root(j)
            if a!=b:par[a]=b
    return len({root(i) for i in range(1,n+1)})


def min_degree_width(n,eq):
    """ANCHO DE UNA ORDENACIÓN HEURÍSTICA, NO COTA INFERIOR DE TREEWIDTH."""
    adj={i:set() for i in range(1,n+1)}
    for vs,_ in eq:
        for a in vs:
            for b in vs:
                if a!=b:adj[a].add(b)
    width=0
    while adj:
        v=min(adj,key=lambda v:(len(adj[v]),v));nb=list(adj[v]);width=max(width,len(nb))
        for i,a in enumerate(nb):
            for b in nb[i+1:]:adj[a].add(b);adj[b].add(a)
        del adj[v]
        for a in nb:adj[a].discard(v)
    return width


def gate_semantic_checks():
    checks=0
    def val(l,v):return v[abs(l)] == (l>0)
    for op in ('OR','AND'):
        for sa,sb in product((1,-1),repeat=2):
            cls=emit_gate(3,op,sa,2*sb)
            for x,y,z in product((False,True),repeat=3):
                v={1:x,2:y,3:z}
                sat=all(any(val(l,v) for l in c) for c in cls)
                target=(val(sa,v) or val(2*sb,v)) if op=='OR' else (val(sa,v) and val(2*sb,v))
                assert sat==(z==target)
                checks+=1
    # Certificado semántico independiente sobre los 8 patrones de cada triple
    for rhs in (0,1):
        g=Builder(3);g.xor3(1,2,3,rhs)
        tests=[(None,g)]
        for bits in product((0,1),repeat=3):
            if sum(bits)%2 !=rhs:
                h=Builder(3);h.near3(1,2,3,rhs,bits)
                tests.append((bits,h))
        for miss,b in tests:
            gd,us,other,used=scan_gates([norm(c) for c in b.cl])
            assert not other
            for bits in product((0,1),repeat=3):
                v={i+1:bool(bit) for i,bit in enumerate(bits)}
                def solve(i):
                    if i in v:return v[i]
                    op,a,c=gd[i]
                    def vl(l):
                        x=solve(abs(l))
                        return x if l>0 else not x
                    v[i]=vl(a) or vl(c) if op=='OR' else vl(a) and vl(c)
                    return v[i]
                for i in gd:solve(i)
                sat=all(any(val(l,v) for l in c) for c in b.cl)
                expected=(sum(bits)%2==rhs) or (miss is not None and bits==miss)
                assert sat==expected,(rhs,miss,bits)
                checks+=1
    return checks


def experiment(n,k,seed,dpll=True,partial=0,long_edges=0):
    t0=time.perf_counter();g=gen(n,k,seed,partial=partial,long_edges=long_edges)
    parser=extract(g['cnf'],g['variables'])
    components=component_count(g['variables'],g['cnf'])
    assert components==1 and parser['n_sources']==n, (components,parser['n_sources'])
    assert parser['xor_gates']==2*(len(g['eq'])+len(g['near'])) and parser['n_near']==partial
    parse_ms=1000*(time.perf_counter()-t0)
    assert parser['no_3of4_parity_templates']
    actual=count_extracted(parser)
    expected=direct_primary(n,g['eq'],g['near'],g['ors'])
    assert actual['count']==expected, (n,k,actual['count'],expected)
    if n<=16:
        brute=truth_eval(n,g)
        assert brute==expected
    else:brute=None
    baseline=dpll_cnf(g['variables'],g['cnf']) if dpll else None
    if baseline and baseline['complete']:
        assert baseline['count']==expected,('DPLL',baseline,expected)
    return {'n_primary':n,'n_total':g['variables'],'clauses':len(g['cnf']),'incidence_components':components,
            'n_parity_constraints':len(g['eq']),'n_near':len(g['near']),'n_OR':k,'long_edges':long_edges,
            'min_degree_elimination_width':min_degree_width(n,g['eq']+[(x,r) for x,r,miss in g['near']]),
            'detected_xor2':parser['xor_gates'],'n_gate_outputs':parser['n_gate_outputs'],
            'local_templates_3_of_4':not parser['no_3of4_parity_templates'],
            'all_clauses_accounted':parser['all_clauses_accounted'],
            'affine_rank':actual['base_rank'],'free_bits_before_OR':actual.get('free_bits_if_no_OR'),
            'count':actual['count'],'independent_primary_count':expected,'brute_count':brute,
            'detector_plus_count_ms':round(parse_ms+actual['ms'],3),
            'gate_extraction_ms':round(parse_ms,3),
            'gauss_count_ms':round(actual['ms'],3),
            'IE_leaves':actual['leaves'],'near_branches':actual.get('n_near_branches'),
            'DPLL':baseline}


def test_adversarial():
    g=gen(12,2,100)
    # Cambiar una cláusula externa para que la entrada ya NO pertenezca a la familia
    # sin ofrecer interpretación parcial incorrecta.
    rogue=tuple(g['cnf'])+((g['variables'], -g['variables']+1),)
    try:extract(rogue,g['variables'])
    except (ValueError,AssertionError):reject=True
    else:reject=False
    # Invirtiendo el resultado de un XOR, dos unidades opuestas fuerzan contradicción
    g2=gen(10,0,80)
    one=next(cl for cl in g2['cnf'] if len(cl)==1)
    contra=g2['cnf']+[(-one[0],)]
    x=extract(contra,g2['variables']);c=count_extracted(x)
    return {'rechaza_clausula_fuera_de_contrato':reject,'contradiccion_unidades':c['count']==0}


def main():
    res={'version':'2026-11-09','gate_truth_table_checks':gate_semantic_checks(),'metodo':'extrae compuertas OR/AND y composiciones XOR de 3-CNF permutada',
         'controles':[],'negativos':test_adversarial()}
    assert all(res['negativos'].values())
    for n,k,u in [(8,0,0),(10,1,1),(12,2,1),(14,2,2),(16,3,2),(20,2,2),(24,2,2),(32,2,3),(48,2,3),(64,2,3),(96,2,3)]:
        r=experiment(n,k,seed=981+n*7+k,dpll=n<=24,partial=u)
        res['controles'].append(r)
        print('n',n,'todas',r['n_total'],'cl',r['clauses'],'xor',r['detected_xor2'],'near',r['n_near'],
              'sol',r['count'],'ms',r['detector_plus_count_ms'],
              'DPLL',r['DPLL']['nodes'] if r['DPLL'] else '-',
              'completo',r['DPLL']['complete'] if r['DPLL'] else '-',flush=True)
    validations=[]
    for i in range(30):
        n=(6,8,10,12,14)[i%5];k=i%3;u=(i//3)%min(3,n//4)
        z=experiment(n,k,seed=3000+i*11,partial=u,dpll=False)
        assert z['brute_count']==z['count']
        validations.append({'n':n,'near':u,'k':k,'count':z['count']})
    res['aleatorios_adicionales']={'casos':len(validations),'coinciden_con_fuerza_bruta':True}
    longtest=[]
    for n in (12,16,20,24,32,48,64,96):
        long_edges=n//3
        z=experiment(n,2,seed=8282+n,partial=min(3,n//8),long_edges=long_edges,dpll=n<=24)
        longtest.append(z)
    res['conexiones_largas']=longtest
    repeat=[]
    for n,k,u in [(24,2,2),(32,2,3),(48,2,3),(96,2,3)]:
        g=gen(n,k,981+n*7+k,partial=u)
        times=[]
        for _ in range(7):
            t0=time.perf_counter();d=extract(g['cnf'],g['variables']);v=count_extracted(d)
            assert v['count']==direct_primary(n,g['eq'],g['near'],g['ors'])
            times.append(1000*(time.perf_counter()-t0))
        repeat.append({'n':n,'repeticiones':len(times),'min_ms':round(min(times),3),
                       'mediana_ms':round(statistics.median(times),3),'max_ms':round(max(times),3)})
    res['tiempos_repetidos']=repeat
    dpll_repeat=[]
    for n,k,u,reps in [(24,2,2,7),(32,2,3,3)]:
        g=gen(n,k,981+n*7+k,partial=u);runs=[]
        for _ in range(reps):
            # El tope de nodos limita el trabajo; el reloj solo mide estas repeticiones.
            z=dpll_cnf(g['variables'],g['cnf'],maxnodes=250000,seconds=float('inf'))
            assert z['complete'] and z['count']==direct_primary(n,g['eq'],g['near'],g['ors'])
            runs.append(z)
        dpll_repeat.append({'n':n,'repeticiones':reps,'mediana_ms':round(statistics.median(z['ms'] for z in runs),3),
                            'nodos':runs[0]['nodes'],'conteo':runs[0]['count'],'todos_completos':True})
    res['DPLL_tiempos_repetidos']=dpll_repeat
    output=os.path.join(os.path.dirname(os.path.abspath(__file__)),'RESULTADOS_RELACIONES_DISTRIBUIDAS.json')
    with open(output,'w') as f:
        json.dump(res,f,ensure_ascii=False,indent=2)
    print('PASS CONEXIONES LARGAS',[(z['n_primary'],z['min_degree_elimination_width'],z['count'],z['DPLL']['nodes'] if z['DPLL'] else None) for z in longtest]); print('PASS',res['negativos'],'comprobaciones de tablas',res['gate_truth_table_checks'],'aleatorios',len(validations),'repetidos',repeat)

if __name__=='__main__':main()
