class Face():
    def __init__(self, fsolid=None, floops=[], is_inner=False):
        self.FSolid = fsolid
        self.FLoops = floops
        self.is_inner = is_inner
        
    def add_loop(self, loop):
        self.FLoops.append(loop)
    def merge_loops(self, loops):
        self.FLoops.extend(loops)
    def delete_loop(self, loop):
        self.FLoops.remove(loop)
    