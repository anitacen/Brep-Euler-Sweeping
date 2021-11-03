class Hedge():
    def __init__(self, vert1=None, vert2=None, loop=None, 
                prev=None, next=None, edge=None):
        self.HLoop = loop
        self.vert1 = vert1
        self.vert2 = vert2
        self.prev = prev
        self.next = next
        self.edge = edge

class Edge():
    def __init__(self, hedge1=None, hedge2=None):
        self.hedge1 = hedge1
        self.hedge2 = hedge2
        self.point1, self.point2 = hedge1.vert1.point, hedge1.vert2.point
        self.name1, self.name2 = hedge1.vert1.name, hedge1.vert2.name