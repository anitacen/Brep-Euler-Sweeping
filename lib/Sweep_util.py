from lib.Euler_util import *

def get_sweep_point(v, sweep_vert):
    point = v.point
    name = v.name
    new_point = [(point[i] + sweep_vert[i]) for i in range(3)]
    return new_point