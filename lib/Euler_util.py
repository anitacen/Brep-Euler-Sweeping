from .Brep import *

def make_hedges_edge(vert1, vert2):
    # Given two verts
    hedge1 = Hedge(vert1=vert1, vert2=vert2)
    hedge2 = Hedge(vert2=vert1, vert1=vert2)
    # link two Hedges by making one Edge
    edge = Edge(hedge1=hedge1, hedge2=hedge2)
    hedge1.edge = hedge2.edge = edge
    return hedge1, hedge2, edge

def link_two_hedge(h1, h2):
    h1.next = h2
    h2.prev = h1
    return

def update_HLoop(loop):
    h = loop.LHedge
    while (h.next != loop.LHedge):
        h.HLoop = loop
        h = h.next

def remove_hedge(hedge):
    edge = hedge.edge
    solid = hedge.HLoop.LFace.FSolid
    solid.remove_edge(edge)
    del hedge
    return