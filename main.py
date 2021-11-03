from lib.Brep import *
from lib.Euler import *

P1  = [5,0,0, "1"]
P2  = [0,0,0, "2"]
P3  = [0,5,0, "3"]
P4  = [5,5,0, "4"]
P5  = [5,0,5, "5"]
P6  = [0,0,5, "6"]
P7  = [0,5,5, "7"]
P8  = [5,5,5, "8"]
P9  = [4,1,0, "9"]
P10 = [3,1,0, "10"]
P11 = [3,2,0, "11"]
P12 = [4,2,0, "12"]

solid, face_down, loop_down, V1 = mvfs(P1)
V2, h12, h21 = mev(V1, P2, loop_down)
V3, h23, h32 = mev(V2, P3, loop_down)
V4, h34, h43 = mev(V3, P4, loop_down)
face_right, loop_right, h41, h14 = mef(V4, V1, loop_down)
V8, h48, h84 = mev(V4, P8, loop_right)
V5, h85, h58 = mev(V8, P5, loop_right)
face_front, loop_front, h51, h15 = mef(V5, V1, loop_right)
V6, h56, h65 = mev(V5, P6, loop_front)
face_left, loop_left, h62, h26 = mef(V6, V2, loop_front)
V7, h67, h76 = mev(V6, P7, loop_left)
face_behind, loop_behind, h73, h37 = mef(V7, V3, loop_left)
face_up, loop_up, h78, h87 = mef(V7, V8, loop_behind)

V9, h19, h91 = mev(V1, P9, loop_down)

h = loop_down.LHedge
for i in range(6):
    print("from {} to {}".format(h.edge.name1, h.edge.name2))
    h = h.next

new_loop = kemr(V1, V9, loop_down)
