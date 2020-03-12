####     INSECURE    ####

import xml.dom

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
        print("File "+str(file_name)+"selected for overwrite.")
    else:
        file_name=input("What is the new file's name?\n--->")
        file_exist=test_file_existence(file_name)
        if file_exist==True:
            print("File "+str(file_name)+" exists.\nChoese another file.")
            file_name==input("What file should be created?--->")
            file_exist=test_file_existence(file_name)
        print("File "+str(file_name)+"will be created")
    abort=input("Abort?(Y/N)\n---->")
    if abort=="Y":
        exit()
    print("continuing")
    system_setting=set_system()    
    print(str(system_settings))




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
    bodies=input("Bodies?")
    planets=input("planets?")
    asteroids=input("asteroid?")
    colonies=input("colonies?")
    POI=input("POI?")
    jump_points("Jump?")
    result={"bodies":bodies,"planets":planets,"asteroids":asteroids,"colonies":colonies,"POI":POI,"FTL":jump_points}
    return(result)






if 1==1:
    main()



    
