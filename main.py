import os
import copy
import time

legal_motion={"h":1,"j":1,"k":1,"l":1,"gf":3}
sv=copy.deepcopy(legal_motion)

def add_motion(motions,nb_motion):
    print("Votre solution:")
    i=0
    while(i<nb_motion):
        print("", i,":", end="")
        current_motion=input("")
        if((len(current_motion))==0):
            break
        if (current_motion not in legal_motion):
            print("Mouvement interdit")
            i=0
            motions=""
            continue
        elif(legal_motion[current_motion]==0):
            print("Mouvement epuiser")
            i-=1
        else:
            legal_motion[current_motion]-=1
            current_motion+="gs:call Curse()\n"
            motions+=current_motion
        i+=1
    return "\"let @g=\\\""+motions+"\\\"\""

def print_title():
    l=["  / ____|          (_)    | \ \    / (_)                      -. .",
       " | (___   _____   ___  ___| |\ \  / / _ _ __ ___          _____   ',' ,",
       "  \___ \ / _ \ \ / / |/ _ \ __\ \/ / | | '_ ` _ \      ,'     ,'   ', ',",
       "  ____) | (_) \ V /| |  __/ |_ \  /  | | | | | | |   ,'     ,'      |  |",
       " |_____/ \___/ \_/ |_|\___|\__| \/   |_|_| |_| |_|  \\       \\       |  |",
       "                              INFO    TOULON          \\ /^\\   \\    ,' ,'",
       "                                                            \\   \\ ,' ,'",
       "                                                      / ~-.___\\.-'  ,'",
       "                                                    /   .______.- ~ \\",
       "                                                  /   /'          \\   \\",
       "                                                  \\./               \\/'",
       "                                                  ",]
    for i in l:
        print("\033[91m {}\033[00m" .format(i))

def prepare():
    if(os.system("cp vimrc ~/.vim/ ")==0):
        print("instalation vimrc[",end="")
        print("\033[92m {}\033[00m" .format("ok"),end="")
        print(" ]")
        time.sleep(1)

if __name__ == "__main__":
    prepare()
    motions=""
    nb_motion=30
    while(True):
        print_title()
        motions=add_motion(motions,nb_motion)
        os.system("vim ./test_laby -c"+motions)
        os.system("clear")
        legal_motion=copy.deepcopy(sv)
        print(motions)
        motions=""
