from tkinter import *
from tkinter import ttk
import math
def Open_Equalation_Window():
    Equalation_window=  Toplevel(window)
    Equalation_window.geometry('600x400')
    Equalation_window.resizable(False , False)
    Equalation_window.config(bg='blue')
    Label_text_Equalation_window = Label(Equalation_window,text= 'Enter your equalation:')
    Equalation_Entry = Entry(Equalation_window)
    Equalation_Entry.place(relx= .5, rely= .1, anchor= CENTER , width=250)
    def Get_Info_And_Calculate():
       Value = Equalation_Entry.get()
       print(Value)
       Text_need = str()
       Base_Equalation = Value
       Bridge = ''
       Bridge_2 = ''
       Left_List = []
       Right_List = []
       Alternative_for_i = ''
       Sample_Equalation = (Base_Equalation.split('='))
       Right_Equalation = Sample_Equalation.pop(1)
       Len_Right_Equalation = len(Right_Equalation)
       Len_Variable = 0
       All_List = []
       a = 0
       b = 0
       c = 0
       # first we find left side of our equalation  :)  ('_')   (:
       for i in Base_Equalation:  
           if i == '=':
                Left_List += [Bridge]
                break
           if i == '-' and Bridge == '':
                Bridge += i
           elif i == '-':
                Left_List += [Bridge]
                Bridge = '' 
                i == Alternative_for_i
           elif i == '+':
                Left_List += [Bridge]
                Bridge = ''
           elif i == '=':
                break
           else:
                Bridge += i  
           Alternative_for_i == i
        # Second we find Right side of our equalation  :)   ('_')   (:
       for j in Right_Equalation:
            if j == '-':
                Right_List += [Bridge_2]
                Bridge_2 = '-'
            elif j == '+':
                Right_List += [Bridge_2]
                Bridge_2 = ''
            else:
                Bridge_2 += j 
            Alternative_for_j = j
            Len_Variable += 1
            if Len_Variable == Len_Right_Equalation:
                Right_List += [Bridge_2]
        # Now change the sign of Right_List arguments and move them to All_List and add Left_List to All_List too  :)   ('_')   (:
       for v in Left_List:
            All_List += [v]
       for z in Right_List:
            for m in z:
                if m == '-':
                    z = z[1:]
                    All_List += [z]
                    break
                else:
                    To_Add = '-'
                    z = To_Add + z
                    All_List += [z]
                    break
        # Now find a,b,c  :)   ('_')   (:
       for n in All_List:
            Len_n = len(n)
            Bridge_3 = 0
            for s in n:
                Bridge_3 += 1
                if Bridge_3 == Len_n and s == '*':
                    n = n.replace('x*','')
                    if n == '':
                        a = float(1)
                    else:
                        a += float(n)
                elif Bridge_3 == Len_n and s == 'x':
                    n = n.replace('x','')
                    if n == '':
                        a = float(1)            
                    else:
                        b += float(n)
                elif Bridge_3 == Len_n and s != 'x' and s != '*':
                    c += float(n)
        # Now we find Delta  :)   ('_')   (:
       Delta = (b**2) - (4*a*c)
        #At Last we solve our equalation  :)   ('_')   (:
       try:
            X_1 = (((-1)*b) - (math.sqrt(Delta))) / (2*a)
       except ValueError:
            print('The equation does not have a defined root')
       try:
            X_2 = (((-1)*b) + (math.sqrt(Delta))) / (2*a)
       except ValueError:
            print('The equation does not have a defined root')  
        # And then we go for output  :)   ('_')   (:
       try:
            if X_1 != X_2:
                print('The equation has two distinct solutions')
                print(f'X_1 = {X_1}')
                print(f'X_2 = {X_2}')
            elif X_1 == X_2:
                print('The equation has two double solutions')
                print(f'X = {X_1}')
            else:
                print('The equation is not generalized and has no roots')
       except ValueError and NameError:
            print('The equation does not have a defined root')
       if Delta == 0:
            Output_Text = Label(Equalation_window , text='The equation has two double solutions:')
            Output_Text_X_1 = Label(Equalation_window , text=str(X_1))
            Output_Text_X_2 = Label(Equalation_window , text='',fg= 'white', bg='blue')
           # with open('C:\Users\user1\Desktop\پارسا\Python 1402\Equalation Solver final\Data.txt','a') as Data:
            # Data.write(f"/n{Base_Equalation}/nThe equation has two double solutions/nX1 = {X_1}/n-------------------------------------------------")
       elif Delta >= 0:
           Output_Text = Label(Equalation_window , text='The equation has two distinct solutions:')
           Output_Text_X_1 = Label(Equalation_window , text=str(X_1))
           Output_Text_X_2 = Label(Equalation_window , text=str(X_2))
        #   with open('C:\Users\user1\Desktop\پارسا\Python 1402\Equalation Solver final\Data.txt','a') as Data:
         #   Data.write(f"/n{Base_Equalation}/nThe equation has two distinct solutions/nX1 = {X_1}/nX2 = {X_2}/n-------------------------------------------------")
       else:
           Output_Text= Label(Equalation_window , text='The equation is not generalized and has no roots')
           Output_Text_X_1=Label(Equalation_window , text='',fg= 'white', bg='blue')
           Output_Text_X_2 = Label(Equalation_window , text='',fg= 'white', bg='blue')
          # with open('C:\Users\user1\Desktop\پارسا\Python 1402\Equalation Solver final\Data.txt','a') as Data:
           # Data.write(f"/n{Base_Equalation}/nThe equation is not generalized and has no roots")

       Output_Text.place(relx=.5 , rely= .3 , relwidth= .5 , anchor=CENTER)
       Output_Text_X_1.place(relx=.5,rely=.4 ,relwidth=.5,anchor=CENTER)
       Output_Text_X_2.place(relx =.5,rely=.5 , relwidth=.5 , anchor=CENTER)

        # Nicly done :) ------------- (:    
    Submit_Button = Button(Equalation_window,command=Get_Info_And_Calculate,height=2,width=10,text='submit')
    Submit_Button.place(relx= .5, rely= .2, anchor= CENTER)
    Importent_note = Label(Equalation_window,text='*Please use only small (x) for variable and do not use space and ude (*) for power 2 ',).place(relx=.5,rely=.9,relwidth=.75,anchor=CENTER)
    Thanks = Label(Equalation_window , text='(: Thank You :)').place(relx=.5,rely=.95,relwidth=.15,anchor=CENTER)



window = Tk()
window.title('Equalation solver V1.0')
window.geometry("800x600")

window.configure(bg = 'dark blue')
Label_text_main = Label(window , text='Find your soloution EASY!!!!!!!!!    :)', bg='yellow', fg='black',font='Arial',).pack()
Label_Thanks = Label(window,text='Thank you for using our app.Please note that it is our first app and we will be honored to hear and use your valuable comments.', bg='yellow', fg='black',font='Arial').place(relx=.5 , rely=.9,anchor=CENTER)
Label_Thanks_2 = Label(window,text=' So if you have any idea about our project please ontact us on this email:(mythic.development.co@gmail.com) or contact us in github: (ParsaPSJ)', bg='yellow', fg='black',font='Arial').place(relx=.5 , rely=.95,anchor=CENTER)
butt_Equalation = Button(window,bg = 'yellow', text='Click to solve',bd='8',height=22 , width=40,command=Open_Equalation_Window).place(relx = .5 , rely=.5 , anchor=CENTER , relheight=.56)
#butt_History = Button(window , bg = 'yellow' , text = 'Click for history',bd = '8',height=22, width=40,).place(relx = .8 , rely=.5 , anchor=CENTER , relheight=.56)
#butt_clean = Button(window, bg='yellow', text= 'Click to clean history',bd = '8', height=30).place(relx = .5 , rely=.5 , anchor=CENTER , relheight=.56)

window.mainloop()