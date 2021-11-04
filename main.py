from lib.Shape import *
from lib.Brep import *
from lib.Euler import *
from lib.Euler_util import *
from lib.Sweeping import *

P1  = [5,0,0, "1" ]
P2  = [0,0,0, "2" ]
P3  = [0,5,0, "3" ]
P4  = [5,5,0, "4" ]


P5  = [4,1,0, "5"]
P6  = [4,2,0, "6"]
P7  = [3,2,0, "7"]
P8  = [3,1,0, "8"]


solid, face_down, face_empty, loop_down, loop_empty, [V1, V2, V3, V4] = make_polygon_with_point_list([P1, P2, P3, P4])
loop_in_empty, [V5, V6, V7, V8] = make_ring_with_point_list([P5, P6, P7, P8], face_down, loop_down)

Sweeping([0,0,5], loop_empty, [loop_in_empty])
print("final")
print_solid(solid)