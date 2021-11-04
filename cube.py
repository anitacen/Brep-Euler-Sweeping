
from lib.Brep import *
from lib.Euler import *
from lib.Euler_util import *

def make_cube_example():
    P1  = [5,0,0, "1" ]
    P2  = [0,0,0, "2" ]
    P3  = [0,5,0, "3" ]
    P4  = [5,5,0, "4" ]
    P5  = [5,0,5, "5" ]
    P6  = [0,0,5, "6" ]
    P7  = [0,5,5, "7" ]
    P8  = [5,5,5, "8" ]
    P9  = [4,1,0, "9" ]
    P10 = [3,1,0, "10"]
    P11 = [3,2,0, "11"]
    P12 = [4,2,0, "12"]
    P13 = [4,1,5, "13"]
    P14 = [3,1,5, "14"]
    P15 = [3,2,5, "15"]
    P16 = [4,2,5, "16"]

    solid, face_down, loop_down, V1 = mvfs(P1)

    V2 = mev(V1, P2, loop_down)
    V3 = mev(V2, P3, loop_down)
    V4 = mev(V3, P4, loop_down)
    face_right, loop_right = mef(V4, V1, loop_down)

    V8 = mev(V4, P8, loop_right)
    V5 = mev(V8, P5, loop_right)
    face_front, loop_front = mef(V5, V1, loop_right)
    V6 = mev(V5, P6, loop_front)
    face_left, loop_left = mef(V6, V2, loop_front)
    V7 = mev(V6, P7, loop_left)
    face_behind, loop_behind = mef(V7, V3, loop_left)
    face_up, loop_up = mef(V7, V8, loop_behind)

    V9 = mev(V1, P9, loop_down)
    loop_down_in = kemr(V1, V9, loop_down, face_down)

    V12 = mev(V9, P12, loop_down_in)
    V11 = mev(V12, P11, loop_down_in)
    V10 = mev(V11, P10, loop_down_in)
    face_right_in, loop_right_in = mef(V10, V9, loop_down_in)

    V13 = mev(V9, P13, loop_right_in)
    V16 = mev(V13, P16, loop_right_in)
    face_behind_in, loop_behind_in = mef(V16, V12, loop_right_in)
    V15 = mev(V16, P15, loop_behind_in)
    face_left_in, loop_left_in = mef(V15, V11, loop_behind_in)
    V14 = mev(V15, P14, loop_left_in)
    face_front_in, loop_front_in = mef(V14, V10, loop_left_in)
    face_up_in, loop_up_in = mef(V14, V13, loop_front_in)

    kfmrh(face_up_in, face_up)

    print("final")
    print_solid(solid)

if __name__ == "__main__":
    make_cube_example()