import unittest
from math import sqrt
import numpy as np
from radios_esferas_v10 import A,RADII,ANGLES,radial_mask,radial_experiment,tetrahedron,geom_experiment,trilateration_difference,signed_volume

class RadialTests(unittest.TestCase):
    def test_generated_lattice(self): self.assertEqual(list(RADII), list(range(2,25,2)))
    def test_angles(self): self.assertEqual(list(ANGLES), list(range(0,360,30)))
    def test_counts(self):
        self.assertEqual(radial_experiment()['counts'], dict(total=144,A=36,B=16,intersection_AB=4,projection_AB=48,silence_AB=96,C=36,new_projection_C=32,projection_ABC=80,silence_ABC=64))
    def test_common_radial_radii(self):
        r=radial_experiment(); common_radii=RADII[np.any(r['A']&r['B'],axis=1)]
        np.testing.assert_array_equal(common_radii,[12,24])
    def test_common_angles(self):
        m=radial_experiment()['A']&radial_experiment()['B']
        np.testing.assert_array_equal(ANGLES[np.any(m,axis=0)],[0,180])
    def test_orientation_does_not_add_radii(self):
        r=radial_experiment(); usedA=set(RADII[np.any(r['A'],axis=1)])
        usedC=set(RADII[np.any(r['C'],axis=1)])
        self.assertEqual(usedA,usedC)
    def test_silence_is_not_measurement(self):
        r=radial_experiment(); self.assertFalse(r['AB'][0,0]); self.assertFalse(r['ABC'][0,0])
    def test_new_angle_adds_cells(self):
        r=radial_experiment(); self.assertEqual(int(np.sum(r['C'] & ~r['AB'])),32)

class SphereTests(unittest.TestCase):
    def test_equilateral_triangle(self):
        anchors,_,_,_,_=tetrahedron()
        self.assertAlmostEqual(np.linalg.norm(anchors[0]-anchors[1]),A)
        self.assertAlmostEqual(np.linalg.norm(anchors[0]-anchors[2]),A)
        self.assertAlmostEqual(np.linalg.norm(anchors[1]-anchors[2]),A)
    def test_sphere_distances_symmetry(self):
        anchors,p,m,_,_=tetrahedron()
        np.testing.assert_allclose(np.linalg.norm(anchors-p,axis=1),[A]*3,rtol=0,atol=1e-12)
        np.testing.assert_allclose(np.linalg.norm(anchors-m,axis=1),[A]*3,rtol=0,atol=1e-12)
    def test_candidates_are_reflections(self):
        _,p,m,_,_=tetrahedron()
        np.testing.assert_allclose(p[:2],m[:2])
        self.assertAlmostEqual(p[2],-m[2])
    def test_rank_three_anchors(self): self.assertEqual(geom_experiment()['rank_3'],2)
    def test_rank_four_coplanar(self): self.assertEqual(geom_experiment()['rank_4_coplanar'],2)
    def test_fourth_coplanar_not_discriminating(self): self.assertTrue(geom_experiment()['coplanar_same_distances'])
    def test_rank_four_noncoplanar(self): self.assertEqual(geom_experiment()['rank_4_noncoplanar'],3)
    def test_noncoplanar_discriminates(self):
        g=geom_experiment()
        self.assertGreater(g['minus_distance_to_anchor4']-g['plus_distance_to_anchor4'],2.)
        self.assertLess(g['error_non_coplanar'],1e-12)
    def test_oriented_volume_changes_sign(self):
        g=geom_experiment()
        self.assertAlmostEqual(g['signed_volume_plus'],-g['signed_volume_minus'])
        self.assertGreater(g['signed_volume_plus'],0)
    def test_volume_magnitude(self):
        g=geom_experiment();self.assertAlmostEqual(g['signed_volume_plus'],A**3/(6*sqrt(2)))
    def test_noisy_noncoplanar_anchor_still_full_rank(self):
        anchors,p,_,_,other=tetrahedron(); bases=np.vstack([anchors,other]); d=np.linalg.norm(bases-p,axis=1)
        for k in range(1,20):
            pert=d+1e-6*np.array([k,-k,k,-k])
            _, rank, residual=trilateration_difference(bases,pert)
            self.assertEqual(rank,3)
            self.assertLess(residual,1e-12)
    def test_planar_reflection_invariance_random(self):
        rng=np.random.default_rng(20261018)
        anchors=rng.uniform(-5,5,size=(7,3)); anchors[:,2]=0
        for _ in range(50):
            v=rng.uniform(-3,3,size=3);v[2]=rng.uniform(.1,3)
            reflection=v*np.array([1,1,-1]);
            np.testing.assert_allclose(np.linalg.norm(anchors-v,axis=1),np.linalg.norm(anchors-reflection,axis=1),atol=1e-12)
    def test_rank_noncoplanar_random_generic(self):
        rng=np.random.default_rng(1701)
        for i in range(20):
            anchors=rng.normal(size=(4,3))
            if abs(np.linalg.det(anchors[1:]-anchors[0]))<.07: continue
            v=rng.normal(size=3)
            guess,rank,_=trilateration_difference(anchors,np.linalg.norm(anchors-v,axis=1))
            self.assertEqual(rank,3)
            np.testing.assert_allclose(guess,v,atol=1e-10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
