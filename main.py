import math
import random
#name and type
#set players points and lifes and a looping agent
life = 3
tape=["plus","minus","multi","divide"]
#show label about game
print("Welcome to a math challenge by ThanhTails and we117113!!")
print("You need to write the answer in your console.")
print("Sorry, we have to operate circle perimeter as x3 because of base 10 engine.")
print("There were two types: arithmetic and geometry.")
name=str(input("Please enter your name:"))
point=0
#def wrong
def wrong():
    print("WRONG ANSWER!!!!!")
#def correct
def right():
    print("\nGreat job, you got it right!")
#bonus
def bonus():  
  a=int(random.randint(1000,1700))
  b=int(random.randint(900,1600))
  print(a,"+(plus)",b,"=?")
  ans=int(a+b)
  enter_ans=int(input("enter your answer:"))
  if enter_ans==ans:
      right()
      okokok()
#Invimulti
def okokok():
  ok1=str(input("Please enter your name:"))
  ok2=str(input("Do you like this project?"))
  if ok2=="yes":
    ok3=str(input("Do you want to co-operate to develop?"))
    if ok3=="yes":
      print("Email we117113official@gmail.com your email and I will add you.")
  ended()
math_type=str(input("please enter your math type(or stop):"))
while True:#engine
    #normal type
    if math_type=="arithmetic" or math_type=="ARITHMETIC":
        print("arithmetic type")
        #input difficulty
        difficulty=str(input("enter your difficulty:easy,normal,hard,harder or insane(next update have more)?\nType difficulty here:"))
        if difficulty=="easy" or difficulty=="EASY":#easy
            print("easy::start")

            a=int(random.randint(-50,50))
            b=int(random.randint(-50,50))
            qtape=random.choice(tape)
            if qtape=="plus":
                print(a,"+(plus)",b,"=?")
                ans=int(a+b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=5
                else:
                    wrong()
                    life-=1
            elif qtape=="minus":
                print(a,"-(minus)",b,"=?")
                ans=int(a-b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=5
                else:
                    wrong()
                    life-=1
                    wrong()
            elif qtape=="multi":
                print(a,"*(multi)",b,"=?")
                ans=int(a*b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=5
                else:
                    wrong()
                    life-=1
                    wrong()
            elif qtape=="divide":
                print(a,"/(divide)",b,"=?")
                ans=a//b
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=5
                else:
                    wrong()
                    life-=1
        elif difficulty=="normal" or difficulty=="NORMAL":#normal
            print("normal::start")

            a=int(random.randint(-100,100))
            b=int(random.randint(-100,100))
            qtape=random.choice(tape)
            if qtape=="plus":
                print(a,"+(plus)",b,"=?")
                ans=int(a+b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=10
                else:
                    wrong()
                    life-=1
            elif qtape=="minus":
                print(a,"-(minus)",b,"=?")
                ans=int(a-b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=10
                else:
                    wrong()
                    life-=1
            elif qtape=="multi":
                print(a,"*(multi)",b,"=?")
                ans=int(a*b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    print("RIGHT ANSWER!!!! GREAT JOB")
                    print("the answer is:",ans)
                    point+=10
                else:
                    wrong()
                    life-=1
            elif qtape=="divide":
                print(a,"/(divide)",b,"=?")
                ans=a//b
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=10
                else:
                    wrong()
                    life-=1
        elif difficulty=="hard" or difficulty=="HARD":#hard
            print("hard::start")

            a=int(random.randint(-500,500))
            b=int(random.randint(-500,500))
            qtape=random.choice(tape)
            if qtape=="plus":
                print(a,"+(plus)",b,"=?")
                ans=int(a+b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=15
                else:
                    wrong()
                    life-=1
            elif qtape=="minus":
                print(a,"-(minus)",b,"=?")
                ans=int(a-b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=15
                else:
                    wrong()
                    life-=1
            elif qtape=="multi":
                print(a,"*(multi)",b,"=?")
                ans=int(a*b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=15
                else:
                    wrong()
                    life-=1
            elif qtape=="divide":
                print(a,"/(divide)",b,"=?")
                ans=a//b
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=15
                else:
                    wrong()
                    life-=1
        elif difficulty=="harder" or difficulty=="HARDER":#harder
            print("harder::start")

            a=int(random.randint(-750,750))
            b=int(random.randint(-750,750))
            qtape=random.choice(tape)
            if qtape=="plus":
                print(a,"+(plus)",b,"=?")
                ans=int(a+b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=20
                else:
                    wrong()
                    life-=1
            elif qtape=="minus":
                print(a,"-(minus)",b,"=?")
                ans=int(a-b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=20
                else:
                    wrong()
                    life-=1
            elif qtape=="multi":
                print(a,"*(multi)",b,"=?")
                ans=int(a*b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=20
                else:
                    wrong()
                    life-=1
            elif qtape=="divide":
                print(a,"/(divide)",b,"=?")
                ans=a//b
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=20
                else:
                    wrong()
                    life-=1
        elif difficulty=="insane" or difficulty=="insane":#insane
            print("insane::start")

            a=int(random.randint(-1000,1000))
            b=int(random.randint(-1000,1000))
            qtape=random.choice(tape)
            if qtape=="plus":
                print(a,"+(plus)",b,"=?")
                ans=int(a+b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=25
                else:
                    wrong()
                    life-=1
            elif qtape=="minus":
                print(a,"-(minus)",b,"=?")
                ans=int(a-b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=25
                else:
                    wrong()
                    life-=1
            elif qtape=="multi":
                print(a,"*(multi)",b,"=?")
                ans=int(a*b)
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=25
                else:
                    wrong()
                    life-=1
            elif qtape=="divide":
                print(a,"/(divide)",b,"=?")
                ans=a//b
                enter_ans=int(input("enter your answer:"))
                if enter_ans==ans:
                    right()
                    point+=25
                else:
                    wrong()
                    life-=1
    
    elif math_type=="stop" or math_type=="STOP":
        print("\nBye bye")
        break
    elif math_type=="equation" or math_type=="EQUATION":# type calculation:equation
        number_of_equation=int(input("\nenter your number of equation(this version have only 1):"))
        if number_of_equation==1:
                difficulty=str(input("enter your difficulty:easy,normal,hard,harder or insane, or NIGHTMARE (arithmetic only) (next update have more)?\nType difficulty here:"))
                if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    a=int(random.randint(-50,50))
                    b=int(random.randint(-50,50))
                    if a==0:
                        if b==0:
                            ans="1"
                        else:
                            ans="0"
                    else:
                        ans=int(-b/a)
                    print("a=",a,"\nb=",b)
                    enter_ans=int(input("enter your answer:"))
                    if enter_ans==ans:
                        right()
                        point+=10
                    else:
                        wrong()
                        life-=1
                elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
                    print("\nMedium/Normal")
                    a=int(random.randint(-100,100))
                    b=int(random.randint(-100,100))
                    if a==0:
                        if b==0:
                            ans="1"
                        else:
                            ans="0"
                    else:
                        ans=int(-b/a)
                    print("a=",a,"\nb=",b)
                    enter_ans=int(input("enter your answer:"))
                    if enter_ans==ans:
                        right()
                        point+=15
                    else:
                        wrong()
                        life-=1
                elif difficulty=="hard" or difficulty=="HARD":#dif:hard
                    print("\nHard")
                    a=int(random.randint(-500,500))
                    b=int(random.randint(-500,500))
                    if a==0:
                        if b==0:
                            ans="1"
                        else:
                            ans="0"
                    else:
                        ans=int(-b/a)
                    print("a=",a,"\nb=",b)
                    enter_ans=int(input("enter your answer:"))
                    if enter_ans==ans:
                        right()
                        point+=20
                    else:
                        wrong()
                        life-=1
                elif difficulty=="harder" or difficulty=="HARDER":#if:harder
                    print("\nHarder")
                    a=int(random.randint(-750,750))
                    b=int(random.randint(-750,750))
                    if a==0:
                        if b==0:
                            ans="1"
                        else:
                            ans="0"
                    else:
                        ans=int(-b/a)
                    print("a=",a,"\nb=",b)
                    enter_ans=int(input("enter your answer:"))
                    if enter_ans==ans:
                        right()
                        point+=25
                    else:
                        wrong()
                        life-=1
                elif difficulty=="insane" or difficulty=="INSANE":
                    a=int(random.randint(-1000,1000))
                    b=int(random.randint(-1000,1000))
                    if a==0:
                        if b==0:
                            ans="1"
                        else:
                            ans="0"
                    else:
                        ans=int(-b/a)
                    print("a=",a,"\nb=",b)
                    enter_ans=int(input("enter your answer:"))
                    if enter_ans==ans:
                        right()
                        point+=30
                    else:
                        wrong()
                        life-=1
    elif math_type=="geometry" or math_type=="GEOMETRY":
      g_type=input("Enter your shape: ")
      g_cal=input("Choose area or perimeter?")
      if g_type=="square":
        if g_cal=="area":
          print("Area")
          difficulty=input("Choose difficulty: ")
          if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    a=int(random.randint(10,50))
                    print("The edge is: ",a)
                    ans=a**2
                    enter_ans=int(input("Enter your answer:"))
                    if ans==enter_ans:
                      print("Correct!!!\nThe answer is:",ans)
                      point+=5
                    else:
                      print("Incorect\n The answer is: ",ans)
                      life-=1

          elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
            print("\nMedium/Normal")
            edge=int(random.randint(0,100))
            print("The edge is: ",edge)
            ans=edge**2
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              print("Correct!!!\nThr answer is: ",ans)
              point+=10
            else:
              print("Incorrect! \n The answer is: ",ans)
              life-=1
          elif difficulty=="hard" or difficulty=="HARD":#dif:hard      
            print("\nHard")
            a=int(random.randint(101,500))
            print("The edge is: ",a)
            ans=a**2
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=15
            else:
              wrong()
              life-=1
            
            
          elif difficulty=="harder" or difficulty=="HARDER":#if:harder
            print("\nHarder")
            a=int(random.randint(501,750))
            print("The edge is: ",a)
            ans=a**2
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=20
            else:
              wrong()
              life-=1
          elif difficulty=="insane" or difficulty=="INSANE":
            a=int(random.randint(751,1000))
            print("The edge is: ",a)
            ans=a**2
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=30
            else:
              wrong()
              life-=1
        if g_cal=="perimeter":
          print("Perimeter")
          difficulty=input("Choose difficulty: ")
          if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    a=int(random.randint(-50,50))
                    print("The edge is: ",a)
                    ans=a*4
                    enter_ans=int(input("Enter your answer:"))
                    if ans==enter_ans:
                      print("Correct!!!\nThe answer is:",ans)
                      point+=5
                    else:
                      print("Incorect\n The answer is: ",ans)
                      life-=1

          elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
            print("\nMedium/Normal")
            edge=int(random.randint(-100,100))
            print("The edge is: ",edge)
            ans=edge**2
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              print("Correct!!!\nThr answer is: ",ans)
              point+=10
            else:
              print("Incorrect! \n The answer is: ",ans)
              life-=1
          elif difficulty=="hard" or difficulty=="HARD":#dif:hard      
            print("\nHard")
            a=int(random.randint(-500,500))
            print("The edge is: ",a)
            ans=a*4
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=15
            else:
              wrong()
              life-=1
            
            
          elif difficulty=="harder" or difficulty=="HARDER":#if:harder
            print("\nHarder")
            a=int(random.randint(-750,750))
            print("The edge is: ",a)
            ans=a*4
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=20
            else:
              wrong()
              life-=1
          elif difficulty=="insane" or difficulty=="INSANE":
            a=int(random.randint(-1000,1000))
            print("The edge is: ",a)
            ans=a*4
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=30
            else:
              wrong()
              life-=1
      elif g_type=="rectangle":
        if g_cal=="area":
          print("Area")
          difficulty=input("Choose difficulty: ")
          if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    a=int(random.randint(0,50))
                    b=int(random.randint(0,50))
                    print("Length= ",a,"Width=",b)
                    ans=a*b
                    enter_ans=int(input("Enter your answer:"))
                    if ans==enter_ans:
                      print("Correct!!!\nThe answer is:",ans)
                      point+=5
                    else:
                      print("Incorect\n The answer is: ",ans)
                      life-=1

          elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
            print("\nMedium/Normal")
            a=int(random.randint(51,100))
            b=int(random.randint(51,100))
            print("Length= ",a,"Height=",b)
            ans=a*b
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              print("Correct!!!\nThr answer is: ",ans)
              point+=10
            else:
              print("Incorrect! \n The answer is: ",ans)
              life-=1
          elif difficulty=="hard" or difficulty=="HARD":#dif:hard      
            print("\nHard")
            a=int(random.randint(101,500))
            b=int(random.randint(101,500))
            print("Length=",a,"Width",b)
            ans=a*b
            enter_ans=int(input("Enter your answer: "))
            if enter_ans==ans:
              right()
              point+=15
            else:
              wrong()
              life-=1
            
            
          elif difficulty=="harder" or difficulty=="HARDER":#if:harder
            print("\nHarder")
            a=int(random.randint(501,750))
            b=int(random.randint(501,750))
            print("Width= ",a,"Height=",b)
            ans=a*b
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=20
            else:
              wrong()
              life-=1
          elif difficulty=="insane" or difficulty=="INSANE":
            print("Insane")
            a=int(random.randint(751,1000))
            b=int(random.randint(751,1000))
            print("Width= ",a,"Height=",b)
            ans=a*b
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=30
            else:
              wrong()
              life-=1
        elif g_cal=="perimeter":
          print("Perimeter")
          difficulty=input("Choose difficulty: ")
          if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    a=int(random.randint(0,50))
                    b=int(random.randint(0,50))
                    print("The edge is: ",a)
                    ans=(a+b)*2
                    enter_ans=int(input("Enter your answer:"))
                    if ans==enter_ans:
                      print("Correct!!!\nThe answer is:",ans)
                      point+=5
                    else:
                      print("Incorect\n The answer is: ",ans)
                      life-=1

          elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
            print("\nMedium/Normal")
            a=int(random.randint(51,100))
            b=int(random.randint(51,100))
            print("The edge is: ",a)             
            ans=(a+b)*2
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              print("Correct!!!\nThr answer is: ",ans)
              point+=10
            else:
              print("Incorrect! \n The answer is: ",ans)
              life-=1
          elif difficulty=="hard" or difficulty=="HARD":#dif:hard      
            print("\nHard")
            a=int(random.randint(101,500))
            b=int(random.randint(101,500))
            print("The edge is: ",a)
            ans=(a+b)*2
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=15
            else:
              wrong()
              life-=1
            
            
          elif difficulty=="harder" or difficulty=="HARDER":#if:harder
            print("\nHarder")
            a=int(random.randint(501,750))
            b=int(random.randint(501,750))
            print("The edge is: ",a)
            ans=(a+b)*2
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=20
            else:
              wrong()
              life-=1
          elif difficulty=="insane" or difficulty=="INSANE":
            print("Insane")
            a=int(random.randint(751,1000))
            b=int(random.randint(751,1000))
            print("The edge is: ",a)
            ans=(a+b)*2
            enter_ans=int(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=30
            else:
              wrong()
              life-=1
      elif g_type=="circle":
        if g_cal=="area":
          print("Area")
          difficulty=input("Choose difficulty: ")
          if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    r=int(random.randint(0,50))
                    print("Radius= ",r)
                    ans=float((r**2)*3.14)
                    enter_ans=float(input("Enter your answer:"))
                    if ans==enter_ans:
                      print("Correct!!!\nThe answer is:",ans)
                      point+=5
                    else:
                      print("Incorect\n The answer is: ",ans)
                      life-=1

          elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
            print("\nMedium/Normal")
            r=int(random.randint(51,100))
            print("Radius= ",r)
            ans=float((r**2)*3.14)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              print("Correct!!!\nThr answer is: ",ans)
              point+=10
            else:
              print("Incorrect! \n The answer is: ",ans)
              life-=1
          elif difficulty=="hard" or difficulty=="HARD":#dif:hard      
            print("\nHard")
            r=int(random.randint(101,500))
            print("Radius= ",r)
            ans=float((r**2)*3.14)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=15
            else:
              wrong()
              life-=1
            
            
          elif difficulty=="harder" or difficulty=="HARDER":#if:harder
            print("\nHarder")
            r=int(random.randint(501,750))
            print("Radius= ",r)
            ans=float((r**2)*3.14)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=20
            else:
              wrong()
              life-=1
          elif difficulty=="insane" or difficulty=="INSANE":
            print("Insane")
            r=int(random.randint(751,1000))
            print("Radius= ",r)
            ans=float((r**2)*3.14)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=30
            else:
              wrong()
              life-=1
        elif g_cal=="perimeter":
          print("Perimeter")
          difficulty=input("Choose difficulty: ")
          if difficulty=="easy" or difficulty=="EASY":#dif: easy
                    print("\n Easy")
                    r=int(random.randint(0,50))
                    print("Radius= ",r)
                    ans=float(r*3)
                    enter_ans=float(input("Enter your answer:"))
                    if ans==enter_ans:
                      print("Correct!!!\nThe answer is:",ans)
                      point+=5
                    else:
                      print("Incorect\n The answer is: ",ans)
                      life-=1

          elif difficulty=="normal" or  difficulty=="NORMAL":#dif:normal/medium
            print("\nMedium/Normal")
            r=int(random.randint(51,100))
            print("Radius= ",r)
            ans=float(r*3)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              print("Correct!!!\nThr answer is: ",ans)
              point+=10
            else:
              print("Incorrect! \n The answer is: ",ans)
              life-=1
          elif difficulty=="hard" or difficulty=="HARD":#dif:hard      
            print("\nHard")
            r=int(random.randint(101,500))
            print("Radius= ",r)
            ans=float(r*3)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=15
            else:
              wrong()
              life-=1
          elif difficulty== "harder" or difficulty=="HARDER":
            print("\nHarder")
            r=int(random.randint(501,750))
            print("Radius= ",r)
            ans=float(r*3)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=20
            else:
              wrong()
              life-=1
          elif difficulty=="insane" or difficulty=="INSANE":
            print("Insane")
            r=int(random.randint(501,1000))
            print("Radius= ",r)
            ans=float(r*3)
            enter_ans=float(input("Enter your answer:"))
            if enter_ans==ans:
              right()
              point+=30
            else:
              wrong()
              life-=1     
    else:           
        print("invalid type!! Try again")
    print("\nHere is yout points and life:")#players points and life
    print("\n\n",name,":", "life:",life,"\n\tpoints:",point,"\n")
if life=="0":
  bonus()
def ended():
  print("Thank you\n and")
  print("Bye!")    
