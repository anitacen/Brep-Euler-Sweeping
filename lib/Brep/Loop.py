class Loop():
    def __init__(self, lface=None, lhedge=None, is_inner=False):
        self.LFace = lface
        self.LHedge = lhedge
        self.is_inner = is_inner
    
    def find_hedge_with_one_vert(self, vert):
        h_start, h_end = None, None
        h = self.LHedge
        while (h.vert1 != vert):
            h = h.next
        h_start = h
        while (h.vert2 != vert):
            h = h.next  
        h_end = h
        return h_start, h_end
    
    def find_hedge_with_two_vert(self, vert1, vert2):
        h_1_2, h_2_1 = None, None
        h = self.LHedge
        while (h.vert1 != vert1 or h.vert2 != vert2): 
            h = h.next
        h_1_2 = h
        while (h.vert2 != vert1 or h.vert1 != vert2):
            h = h.next
        h_2_1 = h
        return h_1_2, h_2_1