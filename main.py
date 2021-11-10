from lib.Shape import *
from lib.Sweeping import sweeping
from lib.Visual import visualize
from lib.util.util import print_solid

outter = [
    [5,0,0, "A" ],
    [0,0,0, "B" ],
    [0,5,0, "C" ],
    [5,5,0, "D" ],
    [7,3,0, "E"],
]
inner1 = [
    [4,1,0, "a" ],
    [5,2,0, "b" ],
    [4,3,0, "c" ],
    [3,2,0, "d" ],
]
inner2 = [
    [2,1,0, "1"],
    [2,4,0, "2"],
    [1,4,0, "3"],
    [1,1,0, "4"],
]


solid, face_down, face_up, loop_down, loop_up, V0 = make_polygon_with_point_list(outter)
loop_in_1, V1 = make_ring_with_point_list(inner1, face_down, loop_down)
loop_in_2, V2 = make_ring_with_point_list(inner2, face_up, loop_up)
sweeping([0,0,5], loop_up, [loop_in_1])
sweeping([0,0,5], loop_down, [loop_in_2])
print_solid(solid)
visualize(solid)
