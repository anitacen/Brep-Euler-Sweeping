class Hedge():
    def __init__(self, vert1=None, vert2=None, loop=None, 
                prev=None, next=None, edge=None):
        self.HLoop = loop
        self.vert1 = vert1
        self.vert2 = vert2
        self.prev = prev
        self.next = next
        self.edge = edge
    def get_names(self):
        return self.vert1.name, self.vert2.name
    def get_points(self):
        return self.vert1.point, self.vert2.point

class Edge():
    def __init__(self, hedge1=None, hedge2=None):
        self.hedge1 = hedge1
        self.hedge2 = hedge2
    def get_names(self):
        return self.hedge1.vert1.name, self.hedge1.vert2.name
    def get_points(self):
        return self.hedge1.vert1.point, self.hedge1.vert2.point