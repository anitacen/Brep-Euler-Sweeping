from lib.Brep import *
from lib.Euler import *
from lib.Euler_util import *
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
P13 = [4,1,5, "13"]
P14 = [3,1,5, "14"]
P15 = [3,2,5, "15"]
P16 = [4,2,5, "16"]

solid, face_down, loop_down, V1 = mvfs(P1)
V2, _, _ = mev(V1, P2, loop_down)
V3, _, _ = mev(V2, P3, loop_down)
V4, _, _ = mev(V3, P4, loop_down)
# TODO:
face_right, loop_right, _, _ = mef(V4, V1, loop_down)
# V8, _, _ = mev(V4, P8, loop_right)
# V5, _, _ = mev(V8, P5, loop_right)
# face_front, loop_front, _, _ = mef(V5, V1, loop_right)
# V6, _, _ = mev(V5, P6, loop_front)
# face_left, loop_left, _, _ = mef(V6, V2, loop_front)
# V7, _, _ = mev(V6, P7, loop_left)
# face_behind, loop_behind, _, _ = mef(V7, V3, loop_left)
# face_up, loop_up, _, _ = mef(V7, V8, loop_behind)

# V9, _, _ = mev(V1, P9, loop_down)
# loop_down_in = kemr(V1, V9, loop_down, face_down)
# V12, _, _ = mev(V9, P12, loop_down_in)
# V11, _, _ = mev(V12, P11, loop_down_in)
# V10, _, _ = mev(V11, P10, loop_down_in)
# face_right_in, loop_right_in, _, _ = mef(V10, V9, loop_down_in)

# V13, _, _ = mev(V9, P13, loop_right_in)
# V16, _, _ = mev(V13, P16, loop_right_in)
# face_behind_in, loop_behind_in, _, _ = mef(V16, V12, loop_right_in)

# V15, _, _ = mev(V16, P15, loop_behind_in)
# face_left_in, loop_left_in, _, _ = mef(V15, V11, loop_behind_in)

# V14, _, _ = mev(V15, P14, loop_left_in)
# face_front_in, loop_front_in, _, _ = mef(V14, V10, loop_left_in)

# face_up_in, loop_up_in, _, _ = mef(V14, V13, loop_front_in)

# kfmrh(face_up_in, face_up)

print("final")
print_solid(solid)