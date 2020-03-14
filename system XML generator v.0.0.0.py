####     INSECURE    ####

import xml.dom
import random

def main():
    print("Warning \nThis program is vulnerable to attack from malicous files\nbe careful")
    print("-------------\nsystem xml gen prototype")
    mode=setting()
    file_name="a"
    if mode=="O":
        file_name==input("What file should be overwritten?\n--->")
        file_exist=test_file_existence(file_name)
        if file_exist==False:
            while file_exist==False:
                print("File "+str(file_name)+" does not exist.\nChoese another file.")
                file_name==input("What file should be overwritten?--->")
                file_exist=test_file_existence(file_name)
        print("File "+str(file_name)+" selected for overwrite.")
    else:
        file_name=input("What is the new file's name?\n--->")
        file_exist=test_file_existence(file_name)
        if file_exist==True:
            print("File "+str(file_name)+" exists.\nChoese another file.")
            file_name==input("What file should be created?--->")
            file_exist=test_file_existence(file_name)
        print("File "+str(file_name)+" will be created")
    abort=input("Abort?(Y/N)\n---->")
    if abort=="Y":
        exit()
    print("continuing")
    system_setting=set_system()    
    print(str(system_setting))
    system_data=system_gen(system_setting)




def setting():
    mode=input("Overwrite or Create new file? (O/C) --->")
    setting_correct=False
    if mode=="O" or mode=="C":
        setting_correct=True
    else:
        while setting_correct==False:
            print("Incorrect option")
            mode=input("Overwrite or Create new file? (O/C) --->")
            if mode=="O" or mode=="C":
                setting_correct=True
    print("Done")
    return(mode)







def test_file_existence(file_name):
    try:
        file=open(file_name,"r")
        file_exist=True
        file.close()
    except FileNotFoundError:
        file_exist=False
    return(file_exist)





def set_system():
    system_id=input("system id?")
    bodies=input("Bodies?")
    planets=input("planets?")
    objects=input("objects?")
    colonies=input("colonies?")
    POI=input("POI?")
    jump_points=input("Jump?")
    seed=input("Seed?\nmust be int")
    result={"system id":system_id,"bodies":bodies,"planets":planets,"objects":objects,"colonies":colonies,"POI":POI,"FTL":jump_points,"seed":seed}
    return(result)




def system_gen(settings):
    bodies_amt=int(settings["bodies"])              ### central bodies(eg the Sun,a blackhole,pulsar/s,etc)
    planets_amt=int(settings["planets"])
    objects_amt=int(settings["objects"])            ### for things that orbit(eg asteroids)
    colonies_amt=int(settings["colonies"])          ### stores data abt any colony wheter artfical plaetbound or otherwise
    POI_amt=int(settings["POI"])                    ### for any other objs that do not have a orbit and is not any other category
    FTL_amt=int(settings["FTL"])                    ### for any FTL related areas
    system_id=settings["system id"]
    bodies={"amt":bodies_amt}
    planets={"amt":planets_amt}
    objects={"amt":objects_amt}
    colonies={"amt":colonies_amt}
    POI={"amt":POI_amt}
    FTL={"amt":FTL_amt}
    i=0
    seed=int(settings["seed"])
    random.seed(seed)
    size=random.randint(50,1000)
    while i<bodies_amt:
        i=i+1
        body_id=str("body "+str(i))
        body_name=random.randint(0,100)             ###use random inputs here as placeholders
        body_type=random.randint(0,9)
        body_extra=random.randint(0,1000)
        body_data={"name":body_name,"id":body_id,"type":body_type,"extra":body_extra}
        bodies[str(i)]=body_data
    print(str(bodies))
    i=0
    pi=3.14159265
    while i<planets_amt:
        i=i+1
        planet_id=str("planet "+str(i))
        planet_name=random.randint(0,100)
        planet_type=random.randint(0,9)
        planet_orbit_range=random.randint(20,size)  ###use to get orbit data TODO: make it so orbits are ordered for easier processing
        planet_orbit_bearing=random.randint(0,360000)/1000    ###assume that we only need 6 decimal places -replace with degrees?
        planet_extra=random.randint(0,1000)                     ###replaced with bearing in degree --must calc pos using orbit data
        planet_data={"name":planet_name,"id":planet_id,"type":planet_type,"orbit range":planet_orbit_range,"orbit bearing":planet_orbit_bearing,"extra":planet_extra}
        planets[str(i)]=planet_data
    print(str(planets))
    i=0
    while i<objects_amt:
        i=i+1
        object_id=str("object "+str(i))
        object_name=random.randint(0,100)
        object_type=random.randint(0,9)
        object_orbit_range=random.randint(30,size)
        object_orbit_bearing=random.randint(0,360000)/1000
        object_extra=random.randint(0,1000)
        object_data={"name":object_name,"id":object_id,"type":object_type,"orbit range":object_orbit_range,"orbit bearing":object_orbit_bearing,"extra":object_extra}
        objects[str(i)]=object_data
    print(str(objects))
    i=0
    while i<colonies_amt:
        i=i+1
        colony_id=str("colony "+str(i))
        colony_name=random.randint(0,100)
        colony_type=random.randint(0,9)     ### later determines whether orbit info is used
        colony_orbit_range=random.randint(20,size)
        colony_orbit_bearing=random.randint(0,360000)/1000
        colony_extra=random.randint(0,1000)
        colony_data={"name":colony_name,"id":colony_id,"type":colony_type,"orbit range":colony_orbit_range,"orbit bearing":colony_orbit_bearing,"extra":colony_extra}
        colonies[str(i)]=colony_data
    print(str(colonies))
    i=0
    while i<POI_amt:
        i=i+1
        POI_id=str("POI "+str(i))
        POI_name=random.randint(0,100)
        POI_type=random.randint(0,50)       ###factor in anomalies
        POI_orbit_range=random.randint(20,size)
        POI_orbit_bearing=random.randint(0,360000)/1000
        POI_extra=random.randint(0,1000)
        POI_data={"name":POI_name,"id":POI_id,"type":POI_type,"orbit range":POI_orbit_range,"orbit bearing":POI_orbit_bearing,"extra":POI_extra}
        POI[str(i)]=POI_data
    print(str(POI))
    while i<FTL_amt:
        i=i+1
        FTL_id=str("POI "+str(i))
        FTL_name=random.randint(0,100)
        FTL_type=random.randint(0,50)       ###factor in anomalies
        FTL_orbit_range=random.randint(20,size+600)
        FTL_orbit_bearing=random.randint(0,360000)/1000
        FTL_extra=random.randint(0,1000)
        FTL_data={"name":FTL_name,"id":FTL_id,"type":FTL_type,"orbit range":FTL_bearing,"extra":FTL_extra}
        FTL[str(i)]=POI_data
    print(str(FTL))
    system_data={"system id":system_id,"bodies":bodies,"planets":planets,"objects":objects,"colonies":colonies,"POI":POI,"FTL":FTL}
    print("Done")
    print(str(system_data))
    return(system_data)




if 1==1:
    main()



    
