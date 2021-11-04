
from lib.Brep import *
from lib.Euler import *

def make_polygon_with_point_list(P):
    V = [Vertex() for i in range(len(P))]
    solid, face, loop, V[0] = mvfs(P[0])
    
    for i in range(1, len(P)):
        V[i] = mev(V[i-1], P[i], loop)
    new_face, new_loop = mef(V[-1], V[0], loop)
    return solid, face, new_face, loop, new_loop, V