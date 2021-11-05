from lib.Brep import *
from lib.Euler import *

def make_ring_with_point_list(P, face, main_loop):
    V = [Vertex() for i in range(len(P))]
    V_main = main_loop.LHedge.vert1
    V[0] = mev(V_main, P[0], main_loop)
    loop_in = kemr(V_main, V[0], main_loop, face)

    for i in range(1, len(P)):
        V[i] = mev(V[i-1], P[i], loop_in)
    new_face, new_loop = mef(V[-1], V[0], loop_in)
    return new_loop, V