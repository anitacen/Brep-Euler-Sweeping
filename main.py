from lib.Shape import *
from lib.Sweeping import sweeping
from lib.Visual import visualize
from lib.util import *

outter = [
    [5,0,0, "1" ],
    [0,0,0, "2" ],
    [0,5,0, "3" ],
    [5,5,0, "4" ],
    [7,3,0, "13"],
]
inner1 = [
    [4,1,0, "5" ],
    [4,2,0, "6" ],
    [3,2,0, "7" ],
    [3,1,0, "8" ],
]
inner2 = [
    [2,1,0, "9"],
    [2,4,0, "10"],
    [1,4,0, "11"],
    [1,1,0, "12"],
]


solid, face_down, face_up, loop_down, loop_up, V0 = make_polygon_with_point_list(outter)
loop_in_1, V1 = make_ring_with_point_list(inner1, face_down, loop_down)
loop_in_2, V2 = make_ring_with_point_list(inner2, face_up, loop_up)
sweeping([0,0,5], loop_up, [loop_in_1])
sweeping([0,0,-5], loop_down, [loop_in_2])
print_solid(solid)
visualize(solid)
