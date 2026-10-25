import json, math, pathlib, random, html, colorsys
from PIL import Image,ImageDraw,ImageFont
BASE=pathlib.Path('/mnt/data/cristal_semantico_integral');data=json.loads((BASE/'CRISTAL_DATOS.json').read_text())
N=data['nodes'];D=data['discriminants'];L=data['links'];FAM=list(data['families']);axis=data['axes'];random.seed(21)
colors={a:v['color'] for a,v in axis.items()}
CORE={'cristal_semantico','cristal_relacional','cierre_en_si','diferencia','relacion','unidad','trama_comun','determinante','suficiencia','rosi','normalizacion','casa','hogar','comprender','identidad','novedad','reflexion','interfaz','gravedad','p_vs_np','informacion','simbolo'}
# layout: sector-based, dense but strongly differentiated by family; allow zoom.
C=(-0.,0.); coords={}
for k,f in enumerate(FAM):
 chunk=sorted([n for n in N if n['family']==f],key=lambda n:(n['id'] not in CORE,n['label']))
 theta0=-math.pi/2+k*2*math.pi/7
 # wedge width 0.68 rad; 4 rings with 4-7 nodes each
 for i,n in enumerate(chunk):
  ring=i//6; j=i%6; cnt=min(6,len(chunk)-ring*6)
  theta=theta0+(j-(cnt-1)/2)*(.70/max(cnt-1,1)) + (ring%2)*.025
  r=300+ring*115
  coords[n['id']]=[round(r*math.cos(theta),2),round(r*math.sin(theta),2)]
# root concepts enter central ring for prominent spine
leaders=['cristal_semantico','cierre_en_si','diferencia','trama_comun','cristal_relacional','rosi','pregunta']
for i,id in enumerate(leaders):
 theta=-math.pi/2+2*math.pi*i/7
 coords[id]=[round(155*math.cos(theta),2),round(155*math.sin(theta),2)]
# place determinants near midpoint, with radial variation
for i,d in enumerate(D):
 ax,ay=coords[d['a']];bx,by=coords[d['b']];mx=(ax+bx)/2;my=(ay+by)/2
 angle=math.atan2(my,mx)+((i%3)-1)*.22;r=(mx*mx+my*my)**.5
 radius=max(218,min(550,r+30+(i%4)*9))
 coords[d['id']]=[round(radius*math.cos(angle),2),round(radius*math.sin(angle),2)]
# handle plot with dark background
W=2440;H=2100;center=(W//2,1000);scale=1.58
img=Image.new('RGB',(W,H),'#0a1421');draw=ImageDraw.Draw(img,'RGBA')
font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fb=lambda sz:ImageFont.truetype(font_path,sz)
for radius in (155,300,415,530,645):
 R=radius*scale
 draw.ellipse((center[0]-R,center[1]-R,center[0]+R,center[1]+R),outline=(139,166,195,22),width=2)
for i,f in enumerate(FAM):
 theta=-math.pi/2+i*2*math.pi/7
 x=center[0]+650*scale*math.cos(theta);y=center[1]+650*scale*math.sin(theta)
 label=data['families'][f].split(' · ')[-1]
 draw.text((x-140,y-10),label,font=fb(19),fill=(209,222,240,200))
# scaffolding edges subtle
for link in L:
 a,b=link['a'],link['b'];x,y=coords[a];xx,yy=coords[b]
 draw.line([(center[0]+x*scale,center[1]+y*scale),(center[0]+xx*scale,center[1]+yy*scale)],fill=(88,142,168,53),width=2)
for d in D:
 x1,y1=coords[d['a']];x2,y2=coords[d['b']];xm,ym=coords[d['id']]
 for xx,yy in ((x1,y1),(x2,y2)):
  draw.line([(center[0]+xm*scale,center[1]+ym*scale),(center[0]+xx*scale,center[1]+yy*scale)],fill=(222,185,116,100),width=2)
for n in N:
 x,y=coords[n['id']];px,py=center[0]+x*scale,center[1]+y*scale
 color=colors[n['primary']]
 rgb=tuple(int(color[i:i+2],16) for i in (1,3,5))
 r=10 if n['id'] in CORE else 6
 draw.ellipse((px-r-5,py-r-5,px+r+5,py+r+5),fill=(*rgb,32))
 draw.ellipse((px-r,py-r,px+r,py+r),fill=(*rgb,240),outline=(230,240,245,100),width=1)
 if n['id'] in CORE:
  label=n['label'];bbox=draw.textbbox((0,0),label,font=fb(18));tw=bbox[2]-bbox[0]
  draw.rounded_rectangle((px-tw/2-7,py+13,px+tw/2+7,py+38),radius=6,fill=(10,23,38,205))
  draw.text((px-tw/2,py+15),label,font=fb(18),fill=(242,243,238,235))
for d in D:
 x,y=coords[d['id']];px,py=center[0]+x*scale,center[1]+y*scale;s=6
 draw.polygon([(px,py-s),(px+s,py),(px,py+s),(px-s,py)],fill=(250,204,130,235))
# center glow
cx,cy=center
for rad,opacity in ((104,13),(80,28),(62,44)):
 draw.ellipse((cx-rad,cy-rad,cx+rad,cy+rad),fill=(106,148,202,opacity))
draw.ellipse((cx-49,cy-49,cx+49,cy+49),outline=(231,234,237,188),width=3)
draw.text((cx-28,cy-13),'Δ*',font=fb(42),fill=(250,239,223,255))
draw.text((84,68),'CRISTAL  SEMÁNTICO',font=fb(64),fill=(241,244,247,255))
draw.text((88,145),'El lenguaje como trama de diferencias acreditables',font=fb(26),fill=(174,190,207,255))
draw.text((89,H-120),f"{len(N)} TÉRMINOS   •   {len(D)} DETERMINANTES   •   {len(L)} RELACIONES DE LECTURA",font=fb(24),fill=(184,204,220,220))
draw.text((89,H-79),'Narrativa → Ontología → Formalización   |   Ejes de color ≠ grados de certeza',font=fb(19),fill=(131,152,174,235))
img.save(BASE/'CRISTAL_INTEGRAL.png',optimize=True)
# write browser app: data inline, no external assets
DATA=json.dumps({**data,'positions':coords},ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
template=r'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"/><title>Cristal semántico integral — Programa de Geometría Relacional</title>
<style>
:root{color-scheme:dark;--bg:#081421;--card:#0e2031;--card2:#13283a;--fg:#eff5f6;--muted:#a9bac8;--line:#2d475b;--accent:#ebc389}*{box-sizing:border-box}body{margin:0;font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--fg);font-size:14px}header{display:flex;gap:15px;align-items:center;justify-content:space-between;padding:15px 23px;border-bottom:1px solid #254054;background:#0a1827}header h1{font-size:20px;letter-spacing:-.04em;margin:0}header small,.muted{color:var(--muted)}#stats{font-size:12px;color:var(--muted)}main{display:grid;grid-template-columns:260px minmax(340px,1fr) 380px;height:calc(100dvh - 74px);min-height:590px}.sidebar,.detail{padding:18px;overflow:auto;background:#0b1a29}.sidebar{border-right:1px solid #294458}.detail{border-left:1px solid #294458}h2{font-size:16px;margin:8px 0 14px;letter-spacing:-.02em}h3{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#a7bdd3;margin:18px 0 7px}input,select{background:#132a3f;color:#f6f5f2;border:1px solid #3a5269;border-radius:9px;padding:10px;width:100%;outline:none}input:focus,select:focus{border-color:#dbc290}label{display:block;color:#b9cad6;margin:14px 0 5px;font-size:12px}.toggle{display:flex;gap:9px;align-items:center;padding:7px 1px;cursor:pointer}.toggle input{width:auto;accent-color:#ebc389}.toggle span{flex:1}.count{color:#849cab;font-size:11px}button{border:1px solid #416076;border-radius:9px;background:#153046;color:#eef5f8;padding:9px 12px;cursor:pointer;font-weight:600}button:hover{background:#244661}.chips{display:flex;gap:6px;flex-wrap:wrap}.chip{border:1px solid #3b556a;border-radius:99px;padding:6px 9px;background:#112638;color:#d8e4e9;cursor:pointer;font-size:12px}.chip:hover{border-color:var(--accent)}.map{position:relative;overflow:hidden;background:radial-gradient(circle at 46% 51%,#142c43,#0b1929 58%,#081522)}.map svg{height:100%;width:100%;display:block;touch-action:none;user-select:none}.map footer{position:absolute;bottom:16px;left:16px;right:16px;background:#0b1b2bdf;border:1px solid #2b4559;padding:10px 14px;border-radius:10px;color:#b0c4d4;font-size:12px;pointer-events:none}.badge{display:inline-block;border:1px solid #637488;border-radius:8px;padding:3px 7px;font-size:11px;color:#dce4e9;margin:2px 4px 2px 0}.headitem{font-weight:700;font-size:24px;letter-spacing:-.03em;margin:0 0 3px}.en{font-size:14px;color:#bfd4dc;margin-bottom:12px;font-style:italic}.panel{border:1px solid #2e4a60;border-radius:11px;padding:12px 14px;margin:10px 0;background:#102539}.panel p{margin:5px 0;line-height:1.5}.pairlabel{font-size:19px;font-weight:750;color:#f2c994;margin:6px 0 10px}.status{display:inline-block;margin:8px 0;padding:5px 8px;border:1px solid #876b45;color:#f0ca93;border-radius:7px;font-size:11px}.detail p{line-height:1.54}.detail .hint{font-size:13px;color:#bdd0dc}.small{font-size:12px;color:#a7bccc}.facet{display:flex;gap:8px;align-items:center;margin:5px 0}.swatch{height:10px;width:10px;border-radius:50%;flex:none}.headrow{display:flex;align-items:center;justify-content:space-between}.facetcircle{cursor:pointer}.facetlabel{pointer-events:none;font-size:10px;paint-order:stroke;stroke:#0b1a2a;stroke-width:3px;stroke-linejoin:round}.mutedline{height:1px;background:#274359;margin:14px 0}.legend{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px}.legitem{display:flex;gap:6px;align-items:center;color:#c3d1dd;font-size:11px}.legend i{width:9px;height:9px;border-radius:50%;display:inline-block;flex:none}.pathstep{margin:7px 0;padding:8px;border-left:3px solid #cca97e;background:#142b40;font-size:12px}.tabrow{display:flex;gap:4px}.tabrow button{flex:1;padding:8px 3px;font-size:12px}.selected{border-color:#e2be8c;background:#35475a}svg .edge{stroke:#789ab0;stroke-width:1;opacity:.25}svg .detedge{stroke:#e4b977;stroke-width:1.05;opacity:.28}svg .term{cursor:pointer}svg .term circle{transition:r .14s,fill-opacity .14s;stroke:#e9e3d4;stroke-opacity:.24;stroke-width:.8}svg .det{cursor:pointer}svg .det polygon{fill:#e8c18a;stroke:#e8d8bd;stroke-width:.7}svg .dimmed{opacity:.18!important}svg .active{opacity:1!important}svg .active circle{stroke:#fff4cf;stroke-width:2}svg .active polygon{stroke:#fff5d7;stroke-width:2}svg .edge.active,svg .detedge.active{stroke:#ffd58f;stroke-width:2.2;opacity:.85!important}svg .nodetext{font-size:12px;fill:#f3f6f7;pointer-events:none;paint-order:stroke;stroke:#091521;stroke-width:3}svg .familylbl{font-size:18px;fill:#97b8cb;font-weight:600;pointer-events:none}.controlhint{font-size:11px;color:#8199ac;margin:10px 0 0}.warn{background:#392b25;border:1px solid #956f46;padding:9px;border-radius:8px;color:#f1d2a9;margin-top:10px;font-size:12px}@media(max-width:1050px){main{grid-template-columns:210px minmax(250px,1fr) 300px}.sidebar,.detail{padding:11px}header h1{font-size:17px}}@media(max-width:780px){header{padding:12px 15px}#stats{display:none}main{display:flex;flex-direction:column;height:auto}.sidebar{order:1;border:0;border-bottom:1px solid #294458;max-height:250px}.map{order:2;height:52vh;min-height:360px}.detail{order:3;min-height:520px;border:0;border-top:1px solid #294458}.map footer{font-size:11px;padding:7px;bottom:5px}}
</style></head><body>
<header><div><h1>CRISTAL SEMÁNTICO <span style="color:#bca285">/ integral</span></h1><small>Programa de Geometría Relacional · Atlas navegable v1.0</small></div><div id="stats"></div></header>
<main><aside class="sidebar"><h2>Explorar la trama</h2><label for="search">Buscar palabra, inglés o noción</label><input id="search" placeholder="cierre, hogar, Δ, ..." autocomplete="off"/><h3>Familias</h3><div id="families"></div><h3>Determinantes</h3><label for="left">Comparar A</label><select id="left"></select><label for="right">Con B</label><select id="right"></select><button id="compare" style="width:100%;margin-top:10px">Encontrar diferencia</button><button id="reset" style="width:100%;margin-top:7px">Ver toda la trama</button><div class="mutedline"></div><h3>Rutas sugeridas</h3><div class="chips" id="quick"></div><h3>Orientaciones</h3><div class="legend" id="legend"></div><p class="controlhint">Tocá un nodo o rombo. Arrastrá para mover; rueda o gesto de pinza para ampliar. Los rombos dorados son diferencias propuestas, no puntos de verdad automática.</p></aside>
<section class="map"><svg xmlns="http://www.w3.org/2000/svg" id="canvas" viewBox="-680 -700 1360 1400" role="img" aria-label="Mapa interactivo con conceptos y determinantes"><defs><radialGradient id="halo"><stop offset="0" stop-color="#264d68" stop-opacity=".28"/><stop offset="1" stop-color="#152b40" stop-opacity="0"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="7"/></filter></defs><circle r="285" fill="url(#halo)"/><g id="space"></g></svg><footer id="foot">Una relación es una pregunta con límites: acercar dos palabras no las convierte en sinónimos.</footer></section>
<aside class="detail" id="detail"><div class="small">FACETA SELECCIONADA</div><h2>Una diferencia puede ser un nuevo nodo</h2><p>Comenzá por «Casa ↔ Hogar» o seleccioná cualquier concepto. Cada ficha distingue narrativa, ontología, posible formalización, símbolo, etimología, uso actual y límite epistemológico.</p></aside></main>
<script>const DATA=__DATA__;
const N=DATA.nodes,D=DATA.discriminants,LINKS=DATA.links,P=DATA.positions,AX=DATA.axes,FAM=DATA.families;
const byId=Object.fromEntries(N.map(n=>[n.id,n]));const byDet=Object.fromEntries(D.map(x=>[x.id,x]));
const byPair=Object.fromEntries(D.map(d=>[[d.a,d.b].sort().join(':'),d]));const selFamily=new Set(Object.keys(FAM));let selected=null,sourceFamily='',scale=1,px=0,py=0,allEdges=[],allObjects=[];
const el=id=>document.getElementById(id); const ns='http://www.w3.org/2000/svg';
function escapeHtml(s){return String(s??'').replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
function E(t,attrs={}){let e=document.createElementNS(ns,t);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));return e;}
function boot(){el('stats').textContent=N.length+' términos · '+D.length+' determinantes · '+LINKS.length+' relaciones';
 el('families').innerHTML=Object.entries(FAM).map(([f,label])=>'<label class="toggle"><input type="checkbox" data-family="'+f+'" checked><span>'+escapeHtml(label)+'</span><span class="count">'+N.filter(n=>n.family===f).length+'</span></label>').join('');
 document.querySelectorAll('[data-family]').forEach(x=>x.addEventListener('change',()=>{x.checked?selFamily.add(x.dataset.family):selFamily.delete(x.dataset.family);filter();}));
 const opts=N.slice().sort((a,b)=>a.label.localeCompare(b.label,'es')).map(n=>'<option value="'+n.id+'">'+escapeHtml(n.label)+'</option>').join('');
 el('left').innerHTML=opts;el('right').innerHTML=opts;el('left').value='casa';el('right').value='hogar';
 el('legend').innerHTML=Object.entries(AX).map(([k,a])=>'<div class="legitem"><i style="background:'+a.color+'"></i>'+escapeHtml(a.label)+'</div>').join('');
 const routes=[['Casa ↔ Hogar','d01'],['Recordar ↔ Entender','d02'],['Herencia ↔ Trama','d05'],['Novedad ↔ Cierre','d08'],['Diferencia ↔ Distancia','d10'],['P ↔ NP','d20'],['Cristal ↔ Cristal','d29']];
 el('quick').innerHTML=routes.map(([n,id])=>'<button class="chip" data-det="'+id+'">'+n+'</button>').join('');
 document.querySelectorAll('[data-det]').forEach(x=>x.onclick=()=>focus(x.dataset.det));
 el('compare').onclick=compare;el('reset').onclick=resetMap;el('search').oninput=filter;buildMap();filter();focus('d01');resetMap(false);initPan();}
function buildMap(){const sp=el('space');for(const r of [150,300,415,530,645])sp.appendChild(E('circle',{r,fill:'none',stroke:'#728aa2','stroke-opacity':'.10','stroke-width':'1.2'}));
 Object.entries(FAM).forEach(([f,l],i)=>{let angle=-Math.PI/2+i*Math.PI*2/7;let t=E('text',{x:Math.cos(angle)*635,y:Math.sin(angle)*635,'text-anchor':'middle',class:'familylbl'});t.textContent=l.split(' · ').slice(1).join(' · ');sp.appendChild(t);});
 for(const l of LINKS){const [x1,y1]=P[l.a],[x2,y2]=P[l.b];let e=E('line',{x1,y1,x2,y2,class:'edge','data-a':l.a,'data-b':l.b});sp.appendChild(e);allEdges.push(e);}
 for(const d of D){const [x,y]=P[d.id];for(const target of [d.a,d.b]){const [tx,ty]=P[target];let e=E('line',{x1:x,y1:y,x2:tx,y2:ty,class:'detedge','data-a':d.id,'data-b':target});sp.appendChild(e);allEdges.push(e);}}
 for(const n of N){let [x,y]=P[n.id],g=E('g',{class:'term','data-id':n.id,transform:`translate(${x},${y})`,tabindex:0,role:'button','aria-label':n.label});let core=['cierre_en_si','cristal_semantico','diferencia','trama_comun','rosi','cristal_relacional','pregunta'].includes(n.id),r=core?12:7;
 g.appendChild(E('circle',{r,fill:AX[n.primary].color}));let title=E('title');title.textContent=n.label+' / '+n.en;g.appendChild(title);
 if(core){let t=E('text',{class:'nodetext',x:14,y:4});t.textContent=n.label;g.appendChild(t);}
 g.onclick=ev=>{ev.stopPropagation();focus(n.id)};g.onkeydown=ev=>{if(ev.key==='Enter')focus(n.id)};sp.appendChild(g);allObjects.push(g);}
 for(const d of D){let [x,y]=P[d.id],g=E('g',{class:'det','data-id':d.id,transform:`translate(${x},${y})`,tabindex:0,role:'button','aria-label':'Determinante '+d.label});g.appendChild(E('polygon',{points:'0,-6 6,0 0,6 -6,0'}));let t=E('title');t.textContent=d.label;g.appendChild(t);g.onclick=ev=>{ev.stopPropagation();focus(d.id)};g.onkeydown=ev=>{if(ev.key==='Enter')focus(d.id)};sp.appendChild(g);allObjects.push(g);}}
function familyVisible(id){return Boolean(byId[id]&&selFamily.has(byId[id].family));}
function filter(){const q=el('search').value.toLocaleLowerCase('es').trim();
 const vis=id=>{const n=byId[id];return !!n&&familyVisible(id)&&(!q||[n.label,n.en,n.narr,n.onto].join(' ').toLocaleLowerCase('es').includes(q));};
 allObjects.forEach(g=>{const id=g.dataset.id,yes=byId[id]?vis(id):selFamily.has(byId[byDet[id].a].family)&&selFamily.has(byId[byDet[id].b].family)&&(!q||[byDet[id].label,byId[byDet[id].a].label,byId[byDet[id].b].label].join(' ').toLocaleLowerCase('es').includes(q));g.classList.toggle('dimmed',!yes)});
 allEdges.forEach(e=>e.classList.toggle('dimmed',!(vis(e.dataset.a)||vis(e.dataset.b)||byDet[e.dataset.a]&&!q)));highlight(selected);}
function resetMap(clearDetail=true){selected=null;el('search').value='';allObjects.forEach(g=>{g.classList.remove('dimmed','active')});allEdges.forEach(e=>{e.classList.remove('dimmed','active')});if(clearDetail){el('detail').innerHTML='<div class="small">CRISTAL COMPLETO</div><h2>Explorá la trama</h2><p>Seleccioná un concepto, compará dos palabras o tocá un rombo dorado para revelar su diferencia candidata.</p>';el('foot').textContent='Mapa completo: las líneas indican vecindad editorial o contraste propuesto; no equivalencia automática.';}}
function focus(id){selected=id;let node=byId[id],det=byDet[id];
 if(node){el('detail').innerHTML='<div class="small">FACETA / '+escapeHtml(FAM[node.family])+'</div><h2 class="headitem">'+escapeHtml(node.label)+'</h2><div class="en">'+escapeHtml(node.en)+'</div><span class="badge">'+escapeHtml(node.epistemic)+'</span><h3>Narrativa</h3><div class="panel"><p>'+escapeHtml(node.narr)+'</p></div><h3>Ontología</h3><div class="panel"><p>'+escapeHtml(node.onto)+'</p></div><h3>Formalización o criterio</h3><div class="panel"><p>'+escapeHtml(node.formal)+'</p></div><h3>Orientación y símbolo</h3>'+node.axes.map(a=>'<div class="facet"><span class="swatch" style="background:'+AX[a].color+'"></span>'+escapeHtml(AX[a].label)+'</div>').join('')+'<p class="small">Imagen mental: '+escapeHtml(node.symbol)+'</p><h3>Origen e historia</h3><p>'+escapeHtml(node.history)+'</p><p class="small">'+escapeHtml(node.history_status)+'</p><h3>Uso social y riesgo de confusión</h3><p>'+escapeHtml(node.current)+'</p><div class="mutedline"></div><p class="small"><b>Documento de origen / continuidad:</b> '+escapeHtml(node.source)+'</p>';
 } else if(det){let a=byId[det.a],b=byId[det.b];el('detail').innerHTML='<div class="small">DETERMINANTE / '+escapeHtml(det.id)+'</div><h2 class="pairlabel">'+escapeHtml(det.label)+'</h2><div class="en">'+escapeHtml(a.label)+' ↔ '+escapeHtml(b.label)+'</div><span class="status">'+escapeHtml(det.status)+'</span><h3>Pregunta de ROSI</h3><div class="panel"><p>'+escapeHtml(det.question)+'</p></div><h3>Diferencia que se intenta sostener</h3><p>'+escapeHtml(det.contrast)+'</p><h3>Contrato de validez</h3><p>'+escapeHtml(det.scope)+'</p><h3>Falsador o límite</h3><div class="panel"><p>'+escapeHtml(det.falsifier)+'</p></div><button onclick="window.selectTerm(\''+det.a+'\')">'+escapeHtml(a.label)+'</button> <button onclick="window.selectTerm(\''+det.b+'\')">'+escapeHtml(b.label)+'</button><p class="small" style="margin-top:20px">Aplicación editorial del protocolo ROSI. El evaluador ROS-1 no se ejecutó: no atribuirle certificación automática.</p>';}
 highlight(id);}
window.selectTerm=focus;
function highlight(id){if(!id)return;const rel=new Set([id]);for(const e of allEdges){if(e.dataset.a===id||e.dataset.b===id){rel.add(e.dataset.a);rel.add(e.dataset.b)}}
 if(byDet[id]){rel.add(byDet[id].a);rel.add(byDet[id].b)}
 allObjects.forEach(g=>{g.classList.toggle('active',rel.has(g.dataset.id));g.classList.toggle('dimmed',!rel.has(g.dataset.id))});allEdges.forEach(e=>{let active=rel.has(e.dataset.a)&&rel.has(e.dataset.b);e.classList.toggle('active',active);e.classList.toggle('dimmed',!active)});
 el('foot').textContent=(byDet[id]? 'Determinante: '+byDet[id].label+' — '+byDet[id].status : 'Concepto: '+byId[id].label+' · '+AX[byId[id].primary].label)+' · El vínculo no significa equivalencia automática.';}
function compare(){let a=el('left').value,b=el('right').value;if(a===b){focus(a);return};let d=byPair[[a,b].sort().join(':')];if(d){focus(d.id);return}
 selected=null;allObjects.forEach(g=>{g.classList.toggle('dimmed',!([a,b].includes(g.dataset.id)));g.classList.remove('active');});let A=byId[a],B=byId[b];
 let shared=A.axes.filter(x=>B.axes.includes(x));let uniqueA=A.axes.filter(x=>!B.axes.includes(x)),uniqueB=B.axes.filter(x=>!A.axes.includes(x));
 el('detail').innerHTML='<div class="small">COMPARACIÓN ABIERTA / ROSI</div><h2>'+escapeHtml(A.label)+' ↔ '+escapeHtml(B.label)+'</h2><span class="status">OPEN · REQUEST_DISCRIMINANT</span><p>No existe todavía una ficha de contraste validada para este par. No inventamos una diferencia mínima.</p><h3>Convergencias editoriales</h3><p>'+shared.map(x=>escapeHtml(AX[x].label)).join(', ').concat(shared.length?'':'No hay facetas compartidas preetiquetadas.')+'</p><h3>Facetas no compartidas</h3><p>'+escapeHtml(A.label)+': '+uniqueA.map(x=>escapeHtml(AX[x].label)).join(', ')+'</p><p>'+escapeHtml(B.label)+': '+uniqueB.map(x=>escapeHtml(AX[x].label)).join(', ')+'</p><h3>Pregunta imprescindible</h3><p>¿Qué respuesta cambia al sustituir A por B en un contexto C? Definir C y un contraejemplo antes de llamar determinante a una palabra.</p><p class="small">Las facetas son etiquetas editoriales: no son una métrica semántica ni garantizan minimalidad.</p>';
}
function initPan(){const svg=el('canvas'),sp=el('space');let holding=false,last=null,hadMove=false;function update(){sp.setAttribute('transform',`translate(${px},${py}) scale(${scale})`)};
 svg.addEventListener('wheel',ev=>{ev.preventDefault();const r=svg.getBoundingClientRect();const sx=(ev.clientX-r.left)/r.width*1360-680,sy=(ev.clientY-r.top)/r.height*1400-700;let next=Math.max(.58,Math.min(4.4,scale*Math.exp(-ev.deltaY*.001)));px=sx-(sx-px)*(next/scale);py=sy-(sy-py)*(next/scale);scale=next;update()},{passive:false});
 svg.addEventListener('pointerdown',ev=>{if(ev.target.closest('.term,.det'))return;holding=true;last=[ev.clientX,ev.clientY];svg.setPointerCapture(ev.pointerId)});
 svg.addEventListener('pointermove',ev=>{if(!holding||!last)return;let rect=svg.getBoundingClientRect();px+=(ev.clientX-last[0])/rect.width*1360;py+=(ev.clientY-last[1])/rect.height*1400;last=[ev.clientX,ev.clientY];update()});
 svg.addEventListener('pointerup',()=>{holding=false;last=null});svg.addEventListener('dblclick',()=>{scale=1;px=0;py=0;update()});}
boot();</script></body></html>'''
(BASE/'CRISTAL_INTERACTIVO.html').write_text(template.replace('__DATA__',DATA),encoding='utf-8')
print('overview.png', (BASE/'CRISTAL_INTEGRAL.png').stat().st_size,'HTML', (BASE/'CRISTAL_INTERACTIVO.html').stat().st_size)
