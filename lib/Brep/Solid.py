class Solid():
    def __init__(self, sfaces=[], sedges=[]):
        self.SFaces = sfaces
        self.SEdges = sedges

    def add_face(self, face):
        self.SFaces.append(face)
    def add_edge(self, edge):
        self.SEdges.append(edge)
        
    def delete_face(self, face):
        self.SFaces.remove(face)
    def delete_edge(self, edge):
        self.SEdges.remove(edge)