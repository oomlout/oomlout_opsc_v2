import opsc



def gen_library(do, save_file = False):
    gen_slot_keyhole(do, save_file)
    gen_slot_screwhole(do, save_file)

def gen_slot_keyhole(do, save_file = False):
    rads = [20,4]
    
    for r in rads:
        objects = []
        rl = r * 1.25   
        dic = opsc.opsc_easy("positive", "slot", w=rl + r,r=r/2, pos=[0,rl/2,0],rot=[0,0,90])
        objects.append(dic)
        dic = opsc.opsc_easy("positive", "hole", r=rl/2, pos=[0,rl,0],rot=[0,0,0])
        objects.append(dic)

        name = "slot_keyhole_m" + str(r)
        if save_file:
            save_lib(name,objects)
        do[name] = opsc.opsc_get_object(objects)

def gen_slot_screwhole(do, save_file = False):
    rads = [20,4]
    
    for r in rads:
        objects = []
        rl = r * 2
        dic = opsc.opsc_easy("positive", "slot", w=rl + r,r=r/2, pos=[0,rl/2,0],rot=[0,0,90])
        objects.append(dic)
        dic = opsc.opsc_easy("positive", "hole", r=rl/2, pos=[0,rl,0],rot=[0,0,0])
        objects.append(dic)

        name = "slot_screwhole_m" + str(r)
        if save_file:
            save_lib(name,objects)
        do[name] = opsc.opsc_get_object(objects)



def save_lib(name,objects):
    opsc.opsc_make_object("parts\\" + name + "\\part.scad",objects, save_type="all")


