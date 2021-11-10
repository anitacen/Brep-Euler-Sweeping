from lib.Brep import *

class VSolid():
    def __init__(self):
        self.verts = []
        self.edges = []
        self.map_name_idx = {}
        self.faces = []
        self.idx = 0
    def update(self, edge):
        
        p1, p2 = edge.get_points()
        n1, n2 = edge.get_names()
        if n1 not in self.map_name_idx.keys():
            self.map_name_idx[n1] = self.idx
            self.verts.append(scale(p1))
            self.idx += 1
        if n2 not in self.map_name_idx.keys():
            self.map_name_idx[n2] = self.idx
            self.verts.append(scale(p2))
            self.idx += 1
        idx1, idx2 = self.map_name_idx[n1], self.map_name_idx[n2]
        self.edges.append((idx1, idx2))
    
    def update_face(self, face):
        for l in face.FLoops:
            if not l.is_inner:
                h = l.LHedge
                v = []
                while (h.next != l.LHedge):
                    v.append(self.map_name_idx[h.vert1.name])
                    h = h.next
                v.append(self.map_name_idx[h.vert1.name])
        self.faces.append(v)
    

def scale(p):
    new_p = []
    for i in p:
        new_p.append(i * 0.2)
    return new_p