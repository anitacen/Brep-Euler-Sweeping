def print_solid(solid):
    i = 0
    for f in solid.SFaces:
        print("Face # {}".format(i))
        i += 1
        j = 0
        for l in f.FLoops:
            print("\tLoop # {} is_inner: {}".format(j, l.is_inner))
            j += 1
            print_loop(l)

def print_loop(loop):
    h = loop.LHedge
    k = 0
    if h != None:
        while (h.next != loop.LHedge):
            print("\t\tHedge # {}: {}".format(k, h.get_names()))
            k += 1
            h = h.next
        print("\t\tHedge # {}: {}".format(k, h.get_names()))

def print_verts(V):
    for v in V:
        print("\t{}".format(v.name))