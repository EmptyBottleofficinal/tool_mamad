import os , pygame , time , random , webbrowser
from playsound3 import playsound


def rockpapersissor():
    bot=random.randint(1,3)
    try:
        player=int(input("1.rock 2.paper 3.sissor:"))
    except:
        print("error")
    if player==1 and bot==2 or player==2 and bot==3 or player==3 and bot==1:
        print("you win")
        startsound = os.path.abspath("win.wav")
        playsound(startsound)
    else:
        print("you lose")
        startsound = os.path.abspath("lose.wav")
        playsound(startsound)


def numberslimit(min,max):
    try:
        bot=(random.randint(min,max))
        tryy=0
        player=None
        while True:
            player=int(input(f"try:{tryy}  "))
            if player>bot:
                print("smaller")
                startsound = os.path.abspath("wrong.wav")
                playsound(startsound)
                tryy=tryy+1
            elif player<bot:
                print("bigger")
                startsound = os.path.abspath("wrong.wav")
                playsound(startsound)
                tryy=tryy+1
            else:
                print('you win')
                startsound = os.path.abspath("win.wav")
                playsound(startsound)
                exit()
    except KeyboardInterrupt:
        print("bye")
    except TypeError:
        print("error")
    except ValueError:
        print("error")


#play sound--
def sound(a):
    startsound = os.path.abspath(a)
    playsound(startsound)
try:
    sound("start.wav")

    #user choose--
    choose=input("1.music player/sound player\n2.time\n3.window maker\n4.random\n5.caculator\n6.word repeater\n7.games\n8.url\n9.exit\n")
    sound('c.wav')
    try:
        choose=int(choose)
    except:
        print("error")

    #music player
    if choose==1:
        choose=input("sound: (should be next to the main.py)")
        choose = os.path.abspath(choose)

        if os.path.exists(choose):
            try:
                playsound(choose)
            except:
                print("error")
                exit()
        else:
            print("error")
            exit()
    #timer
    elif choose==2:
        choose=input("1.timer 2.stopwatch")
        sound('c.wav')
        if choose=="1":
            try:
                hour=input("hours: ?? minutes: ?? second: ??")
                hour=int(hour)

                minutes=input(f"hours: {hour} minutes: ?? second: ??")
                minutes=int(minutes)

                second=input(f"hours: {hour} minutes: {minutes} second: ??")
                second=int(second)

                hour=hour * 60
                minutes=minutes + hour
                minutes=minutes * 60
                second=second+minutes
                time.sleep(second)

                print("crlt + c to exit")

                while True:
                    sound('timer.wav')
                    time.sleep(0.4)

            except KeyboardInterrupt:
                print("bye")
                exit()
            except:
                print("error")
                exit()
        elif choose=="2":
            print("crlt + c if you want to stop")
            hour=0
            minutes=0
            second=0
            try:
                while True:
                    time.sleep(1)
                    second=second+1
                    if second==60:
                        second=second-60
                        minutes=minutes+1
                    elif minutes==60:
                        minutes=minutes-60
                        hour=hour+1
                    print(f"{hour}:{minutes}:{second}")
            except KeyboardInterrupt:
                print("bye")
                exit()
        else:
            print("error")
            exit()
    elif choose==3:

        try:
            #get input
            color1=input("color 1:random 2:choose")
            sound('c.wav')
            #--------------------------------------
            #color:random 1
            if color1 == "1":
                colorall=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            #--------------------------------------------------------------------------------
            #color:user input 2
            elif color1 == "2":
                color1=input("rgb red: (0,225)")
                color2=input("rgb green: (0,225)")
                color3=input("rgb blue: (0,225)")
                color1=int(color1)
                color2=int(color2)
                color3=int(color3)
                colorall=(color1,color2,color3)
            #------------------------------------
            #else
            else:
                print("error:" ,color1 ,"is not allowed put 1 or 2")
                exit()
            #-------------------------------------
            #input
            dis1=input("display 1:random 2:choose")
            sound('c.wav')
            #-------------------------------------
            #display:random 1
            if dis1=="1":
                dis1=random.randint(100,900)
                dis2=random.randint(100,900)
            #-------------------------------------
            #display:user input 2
            elif dis1=="2":
                dis1=input("display 1: (number only)")
                dis2=input("display 2: (number only)")
                dis1=int(dis1)
                dis2=int(dis2)
            #-------------------------------------
            #else
            else:
                print("error:" ,dis1 ,"is not allowed put 1 or 2")
                exit()
            #-------------------------------------
            #input caption or title (whatever)
            cap=input("caption:")
            sound('c.wav')
            #-------------------------------------
            #start
            pygame.init()
            #-------------------------------------
            #display
            win=pygame.display.set_mode((dis1,dis2))
            #---------------------------------------
            #caption or title (whatever)
            pygame.display.set_caption(cap)
            #---------------------------------------
            #run or "un"run
            run=True
            while run:
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT:
                        run=False
            #----------------------------------------
            #color
                win.fill(colorall)
                pygame.display.flip()
            #----------------------------------------
            #exit
            pygame.quit()
            #----------------------------------------------------
            #error
        except:
            print("error: something is wrong")
            sound('error.wav')
    #--------------------------------------------
    elif choose==4:
        choose=input("1.word 2.number")
        sound('c.wav')
        if choose=="1":
            l=[]
            print("crlt + c if you done")
            try:
                while True:
                    word=input(f"word are {l}:")
                    l.append(word)
            except KeyboardInterrupt:
                word=len(l) - 1
                print(l[random.randint(0,word)])
        elif choose=="2":
            min=input("min:")
            sound('c.wav')
            max=input("max:")
            sound('c.wav')
            try:
                min=int(min)
                max=int(max)
                print(random.randint(min,max))
            except:
                print("error")
    elif choose==5:
        choose=input("1.plus 2.minus 3.multiply 4.divided 5.power 6.average")
        sound('c.wav')
        def average():
            try:
                num=[]
                print("ctrl+c if you done")
                while True: 
                    if len(num)==0:
                        num.append(int(input("numbers:[empty]")))
                    else:
                        num.append(int(input(f"numbers:{num} ")))
            except KeyboardInterrupt:
                try:
                    var=0
                    all=0
                    while True:
                        all=all+num[var]
                        var=var+1
                except:
                        try:
                            print(all/len(num))
                        except:
                            print("error")
            except:
                print("error")
        try:
            choose=int(choose)
            if choose>=1 and choose<=6:
                if choose>=1 and choose<=5:
                    num1=input("num 1:")
                    num1=int(num1)
                    num2=input("num 2:")
                    num2=int(num2)

                    if choose==1:
                        print(num1+num2)
                    elif choose==2:
                        print(num1-num2)
                    elif choose==3:
                        print(num1*num2)
                    elif choose==4:
                        print(num1/num2)
                    elif choose==5:
                        print(num1**num2)
                else:
                    average()
                        
            else:
                print("error")
                exit()
        except:
            print("error")
    elif choose==6:
        try:
            num=input('num:\n')
            num=int(num)
            strr=input("word:\n")
            strr=f"{strr} "
            print(strr*num) 
            input()
        except MemoryError:
            print("\ntoo much heavy")
            exit()
        except ValueError:
            print("\nnumber only")
            exit()
        except KeyboardInterrupt:
            print("\nbye")
            exit()
        except:
            print("SOMETHING WENT WRONG")
    elif choose==7:
        choose=input("1.guess the number 2.rock paper sissor 3.others")
        if choose=="1":
            choose=input("1.easy(1,10)\n2.normal(1,100)\n3.hard(1,200)\n4.custom")
            if choose=='1':
                numberslimit(1,10)
            elif choose=='2':
                numberslimit(1,100)
            elif choose=='3':
                numberslimit(1,200)
            else:
                min=input("min:")
                max=input("max:")
                numberslimit(int(min),int(max))
        elif choose=='2':
            rockpapersissor()
        elif choose=='3':
            choose=input('1.rocket driving\n2.space monster\n3.gun man\n4.h1omtik\n5.ping pong')
            if choose=='1':
                webbrowser.open(os.path.abspath('annoying space.html'))
            elif choose=='2':
                webbrowser.open(os.path.abspath('game_sc(araz remix).html'))
            elif choose=='3':
                webbrowser.open(os.path.abspath('gun man.html'))
            elif choose=='4':
                webbrowser.open(os.path.abspath('h1omtik.html'))
            elif choose=='5':
                webbrowser.open(os.path.abspath('ping pong.html'))
            else:
                print("error")
        else:
            print("error")
            exit()

    elif choose==8:
        webbrowser.open(input())
    elif choose==9:
        print('bye')
        exit()
except:
    print("something is wrong")
    playsound('error.wav')
    exit()