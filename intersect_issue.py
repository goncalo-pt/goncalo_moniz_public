import vedo
import numpy as np

my_mesh = vedo.Mesh('my_vedo_mesh.obj')
pt = np.array([2.43196056, 2.        , 0.57248911])
sphere = vedo.Sphere(pos=pt, r=1.1, res=12)
inter = sphere.intersect_with(my_mesh, tol=0.005)
vedo.show(my_mesh, inter)

