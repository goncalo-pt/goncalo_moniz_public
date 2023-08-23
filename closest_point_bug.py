#build simple mesh
import numpy as np
import vedo

points = [
          # Right  
          np.array([2.65, 0.6, 0.0]), 
          np.array([2.65, 0.6, 3.4]),
          np.array([2.22, 0.6, 3.9]),
          np.array([1.89, 0.6, 4.16]),
          np.array([1.55, 0.6, 4.4]),
          np.array([0.6, 0.6, 4.7]),
          np.array([0.6, 0.6, 4.7]),
        
          # Left
          np.array([-2.65, 0.6, 0.0]), 
          np.array([-2.65, 0.6, 3.4]),
          np.array([-2.22, 0.6, 3.9]),
          np.array([-1.89, 0.6, 4.16]),
          np.array([-1.55, 0.6, 4.4]),
          np.array([-0.6, 0.6, 4.7]),



         # Right  
          np.array([2.65, 4.0, 0.0]), 
          np.array([2.65, 4.0, 3.4]),
          np.array([2.22, 4.0, 3.9]),
          np.array([1.89, 4.0, 4.16]),
          np.array([1.55, 4.0, 4.4]),
          np.array([0.6, 4.0, 4.7]),
          np.array([0.6, 4.0, 4.7]),
        
          # Left
          np.array([-2.65, 4.0, 0.0]), 
          np.array([-2.65, 4.0, 3.4]),
          np.array([-2.22, 4.0, 3.9]),
          np.array([-1.89, 4.0, 4.16]),
          np.array([-1.55, 4.0, 4.4]),
          np.array([-0.6, 4.0, 4.7]),

          ]
pts = vedo.Points(points)

mesh = vedo.Mesh([points, [[0,13,1],[1,13,14],[1,2,14],[2,14,15],[2,3,15],[3,15,16],[3,4,16],[4,16,17],
                           [4,5,17],[5,17,18],[5,6,18],[6,18,19],[6,12,19],[12,19,25],[11,12,25],[11,24,25],
                           [10,11,24],[10,23,24],[9,10,23],[9,22,23],[8,9,22],[8,21,22],[7,8,21],[7,20,21]]]
                        ,c='grey')

mesh = mesh.subdivide(method=2, mel=0.5)
labels = mesh.labels('id')
cell_labels = mesh.labels(on="cells")

closest = mesh.closest_point(pt=(1,1,1), radius=1.7, return_cell_id=True)
print(closest)

vedo.show(mesh, labels, axes=3)

