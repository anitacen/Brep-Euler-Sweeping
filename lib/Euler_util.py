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
    if loop.LHedge == None:
        return
    while (h.next != loop.LHedge):
        h.HLoop = loop
        h = h.next
    h.HLoop = loop

def remove_hedge(hedge):
    edge = hedge.edge
    solid = hedge.HLoop.LFace.FSolid
    solid.delete_edge(edge)
    del hedge
    return

def print_solid(solid):
    i = 0
    for f in solid.SFaces:
        print("Face # {}".format(i))
        i += 1
        j = 0
        for l in f.FLoops:
            print("\tLoop # {}".format(j))
            j += 1
            
            h = l.LHedge
            k = 0
            if h != None:
                while (h.next != l.LHedge):
                    print("\t\tHedge # {}: {}".format(k, h.get_names()))
                    k += 1
                    h = h.next
                print("\t\tHedge # {}: {}".format(k, h.get_names()))