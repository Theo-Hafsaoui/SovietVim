import os
import copy
import time
adrr="./NSA_NETWORK/brake_liability "

legal_motion={"h":1,"j":6,"k":1,"l":15,"gf":5,"f.":5,"fa":5,"fb":5,"fc":5,"fd":5,"fe":5,"ff":5,"fg":5,"fh":5,
              "fi":5,"fj":5,"fk":5,"fl":5,"fm":5,"fn":5,"fo":5,"fp":5,"fq":5,"fr":5,"fs":5,"ft":5,"fu":5,"fv":5,
              "fw":5,"fx":5,"fy":5,"fz":5,"f/":5,"gg":1,"G":2,"x":2,"di]":1,"di[":1,"di(":1,"di)":1,"di]":1,
              "vi[":1,"vi(":1,"vi)":1,"vw":1,"vW":1,"vt]":1,"vt[":1,"vt(":1,"vt)":1,"$":1,"0":1,"{":1,"}":1,
              "5gg":1,"4gg":1,"3gg":1,"2gg":1,"1gg":1,"6gg":1,"7gg":1,"8gg":1,"9gg":1,"10gg":1,"%":1,"^":1,"*":1,
              "da]":1,"da[":1,"da(":1,"da)":1,"da]":1,"10gg":1,"11gg":1,"12gg":1,"13gg":1,"14gg":1,"15gg":1,"f[":1,"f]":1,"n2":100,"n3":100,"n4":100,"n5":100}
sv=copy.deepcopy(legal_motion)

def add_motion(motions,nb_motion):
    global adrr
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
        elif (current_motion[0]=="n"):
            print(current_motion)
            if (current_motion=="n2"):
                adrr="./NSA_NETWORK/sanctuary_auditor "
                print("switch to lvl 2")
            elif (current_motion=="n3"):
                adrr="./NSA_NETWORK/habit_makeup "
                print("switch to lvl 3")
            elif (current_motion=="n4"):
                adrr="./NSA_NETWORK/racism_dialogue "
                print("switch to lvl 4")
            elif (current_motion=="n5"):
                adrr="./NSA_NETWORK/trace_et "
                print("switch to lvl 5")
            else:
                print("Not a correct name of level")
            i-=1
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
    if(os.system("cp vimrc ~/ ")==0):
        print("instalation vimrc[",end="")
        print("\033[92m {}\033[00m" .format("ok"),end="")
        print(" ]")
        time.sleep(1)

if __name__ == "__main__":
    prepare()
    print (adrr)
    motions=""
    nb_motion=30
    while(True):
        print_title()
        motions=add_motion(motions,nb_motion)
        os.system("vim "+adrr+"-c"+motions)
        os.system("clear")
        legal_motion=copy.deepcopy(sv)
        print(motions)
        motions=""
