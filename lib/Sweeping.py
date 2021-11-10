from lib.Euler import *
from lib.util.Sweep_util import *

def sweeping(sweep_vert, loop_main, loop_inner):
    # main loop sweeping
    V_init = get_vert_list(loop_main)
    P_sweep = [get_sweep_point(V_init[i], sweep_vert) for i in range(len(V_init))]
    face_main, new_loop = sweeping_loop(loop_main, V_init, P_sweep)
    for loop in loop_inner:
        V_init = get_vert_list(loop)
        P_sweep = [get_sweep_point(V_init[i], sweep_vert) for i in range(len(V_init))]
        new_face, new_loop = sweeping_loop(loop, V_init, P_sweep)
        kfmrh(new_face, face_main)
    return

def sweeping_loop(loop, V_init, P_sweep):
    V_sweep = [Vertex() for i in range(len(P_sweep))]
    for i in range(len(V_init)):
        V_sweep[i] = mev(V_init[i], P_sweep[i], loop)
        V_sweep[i].name = V_init[i].name + "'s"
    loop_empty = loop
    for i in range(1, len(V_init)):
        new_face, new_loop = mef(V_sweep[i], V_sweep[i-1], loop_empty)
        loop_empty = new_loop
    new_face, new_loop = mef(V_sweep[0], V_sweep[-1], loop_empty)
    return new_face, new_loop

def get_vert_list(loop):
    V = []
    h = loop.LHedge
    while (h.next != loop.LHedge):
        V.append(h.vert1)
        h = h.next
    V.append(h.vert1)
    return V