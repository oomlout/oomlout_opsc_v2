import opsc
import opsc_library_gen


name_project = "test_servo_horn"
cylinder_main_radius = 5
cylinder_main_height = 4

''' #v1
cylinder_horn_bottom_radius = 5/2
cylinder_horn_top_radius = cylinder_horn_bottom_radius - 1/2
cylinder_horn_top_height = 3
'''

#v2
cylinder_horn_bottom_radius = 6/2
cylinder_horn_top_radius = cylinder_horn_bottom_radius - 1/2
cylinder_horn_top_height = 3



def main():
    # Define the objects to be used in the OpenSCAD object
    objects = []    
    objects.append({'shape': 'cube_rounded', 'type': 'p', "size":[30,30,4]},   )
    #do an array of 9 holes in an x y grid with a spacing variable
    for x in range(3):
        for y in range(3):
            spacing = 7
            pos = [x*spacing,y*spacing,0]
            objects.extend(get_hole(pos=pos)


def get_hole(**kwargs):
    r1 = kwargs.get('r1', 1)
    r2 = kwargs.get('r2', 1)
    h = cylinder_horn_top_height
    pos = kwargs.get('pos', [0,0,0])
    rv = []
    rv.append({'shape': 'cylinder', 'type': 'n', 'r1':r1, 'r2':r2, 'h':h, "pos":pos, 'm': '#'})
    rv.append({'shape': 'hole', 'type': 'n', 'r':1} )
    return rv


if __name__ == "__main__":
    main()
    


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

#opsc_library_gen.gen_library({},save_file=True)