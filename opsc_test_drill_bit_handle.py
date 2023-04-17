import opsc
import opsc_library_gen


name_project = "drill_bit_handle"
diameter_drill_bit = 3.4
depth_drill_bit = 20
pos_drill_bit = [0,0,0]
diameter_handle = 15
length_handle = 50
pos_handle = [0,0,0]



# Define the objects to be used in the OpenSCAD object
objects = [    
    {'shape': 'cylinder', 'type': 'n', 'pos':pos_drill_bit, 'r':diameter_drill_bit/2, 'h':depth_drill_bit},
    {'shape': 'cylinder', 'type': 'p', 'pos':pos_handle, 'r':diameter_handle/2, 'h':length_handle},    
]



"""
examples
objects = [
    {'shape': 'cube', 'type': 'positive', 'size': [10,5,23]},
    {'shape': 'cylinder', 'type': 'positive', 'r1':3, 'r2':3, 'h':10},
    {'shape': 'sphere', 'type': 'negative', 'radius': 5},

    {'shape': 'cube', 'type': 'positive', 'size': [10,5,23]},
    {'shape': 'cube', 'type': 'positive', 'size': [10,5,23]},
    {'shape': 'cube', 'type': 'positive', 'size': [10,5,23]},
    
    {'shape': 'my_custom_object', 'type': 'positive', 'param1': 10, 'param2': 20},
]
"""




opsc.opsc_make_object(f'outputs/{name_project}/working.scad', objects, save_type="all")

opsc_library_gen.gen_library({},save_file=True)