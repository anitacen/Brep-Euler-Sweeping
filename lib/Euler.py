# v| vertex
# e| edge
# f| face
# h| handle
# r| ring
# s| solid
from .Brep import *
from .Euler_util import *

def mvfs(point):
    # v e f h r s
    # 1 0 1 0 0 1
    # Given a point, make a solid, face, loop and vertex
    solid = Solid()
    face = Face(fsolid=solid)
    loop = Loop(lface=face)
    vertex = Vertex(point=point)
    solid.add_face(face)
    face.add_loop(loop)
    return solid, face, loop, vertex

def mev(old_vertex, point, loop):
    # v e f h r s
    # 1 1 0 0 0 0
    vertex = Vertex(point=point)
    # Given two verts, make two hedges and one edge
    hedge1, hedge2, edge = make_hedges_edge(old_vertex, vertex)
    # Link the edge to solid
    solid = loop.LFace.FSolid
    solid.add_edge(edge)
    # Given a loop, insert two Hedges in loop
    hedge1.HLoop = hedge2.HLoop = loop
    link_two_hedge(hedge1, hedge2)
    if loop.LHedge == None:
        link_two_hedge(hedge2, hedge1)
        loop.LHedge = hedge1
    else:
        h_start, h_end = loop.find_hedge_with_one_vert(old_vertex)
        link_two_hedge(h_end, hedge1)
        link_two_hedge(hedge2, h_start)
    return vertex

def mef(vert1, vert2, loop):
    # v e f h r s
    # 0 1 1 0 0 0
    # Given two verts, make two hedges and one edge
    hedge1, hedge2, edge = make_hedges_edge(vert1, vert2)
    # Make a face and a loop
    solid = loop.LFace.FSolid
    new_face = Face(fsolid=solid, floops=[])
    new_loop = Loop(lface=new_face)
    solid.add_face(new_face)
    solid.add_edge(edge)
    new_face.add_loop(new_loop)
    # Make sure v1->v2's normal pointing outside
    h_start_vert1, h_end_vert1 = loop.find_hedge_with_one_vert(vert1)
    h_start_vert2, h_end_vert2 = loop.find_hedge_with_one_vert(vert2)
    link_two_hedge(h_end_vert1, hedge1)
    link_two_hedge(hedge1, h_start_vert2)
    link_two_hedge(h_end_vert2, hedge2)
    link_two_hedge(hedge2, h_start_vert1)
    # Update loop's LHedge and hedges's HLoop
    loop.LHedge = hedge1
    new_loop.LHedge = hedge2
    update_HLoop(new_loop)
    return new_face, new_loop

def kemr(vert1, vert2, loop, face):
    # v  e f h r s
    # 0 -1 0 0 1 0
    new_loop = Loop(lface=face, lhedge=None, is_inner=True)
    face.add_loop(new_loop)
    # Find the two hedges
    h_1_2, h_2_1 = loop.find_hedge_with_two_vert(vert1, vert2)
    link_two_hedge(h_2_1.prev, h_1_2.next)
    link_two_hedge(h_1_2.prev, h_2_1.next)
    # Update loop's LHedge and hedges's HLoop
    if (h_1_2.vert1 == h_2_1.vert2 and h_1_2.vert2 == h_2_1.vert1):
        loop.LHedge = h_1_2.prev
        new_loop.LHedge = None
        update_HLoop(new_loop)
        remove_hedge(h_1_2)
    else:
        loop.LHedge = h_1_2.prev
        new_loop.LHedge = h_1_2.next
        update_HLoop(new_loop)
        remove_hedge(h_1_2)
        remove_hedge(h_2_1)
    return new_loop

def kfmrh(in_face, out_face):
    for l in in_face.FLoops:
        l.is_inner = True
    out_face.merge_loops(in_face.FLoops)
    solid = in_face.FSolid
    solid.delete_face(in_face)
