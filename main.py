import os
import copy
import time

legal_motion={"h":1,"j":6,"k":1,"l":15,"gf":5,"f.":5,"fa":5,"fb":5,"fc":5,"fd":5,"fe":5,"ff":5,"fg":5,"fh":5,
              "fi":5,"fj":5,"fk":5,"fl":5,"fm":5,"fn":5,"fo":5,"fp":5,"fq":5,"fr":5,"fs":5,"ft":5,"fu":5,"fv":5,
              "fw":5,"fx":5,"fy":5,"fz":5,"f/":5,"gg":1,"G":2,"x":2,"di]":1,"di[":1,"di(":1,"di)":1,"di]":1,
              "vi[":1,"vi(":1,"vi)":1,"vw":1,"vW":1,"vt]":1,"vt[":1,"vt(":1,"vt)":1,"$":1,"0":1,"{":1,"}":1,
              "5gg":1,"4gg":1,"3gg":1,"2gg":1,"1gg":1,"6gg":1,"7gg":1,"8gg":1,"9gg":1,"10gg":1,"%":1,"^":1,"*":1,
              "da]":1,"da[":1,"da(":1,"da)":1,"da]":1,"10gg":1,"11gg":1,"12gg":1,"13gg":1,"14gg":1,"15gg":1,"f[":1,"f]":1}
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
        os.system("vim ./NSA_NETWORK/brake_liability -c"+motions)
        os.system("clear")
        legal_motion=copy.deepcopy(sv)
        print(motions)
        motions=""
