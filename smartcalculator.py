from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l



def toggle_eyes():
    current_color = c.itemcget(eye_left,'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left , 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left , state = new_state)
    c.itemconfigure(pupil_right , state = new_state)
    c.itemconfigure(eye_left , fill = new_color)
    c.itemconfigure(eye_right , fill = new_color)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left , 10,-5)
        c.move(pupil_right , -10,-5)
        c.crossed_eyes = True
    else:
        c.move(pupil_left , -10,5)
        c.move(pupil_right , 10,5)
        c.crossed_eyes = False

def toggle_tongue():
    if not c.tonque_out:
        c.itemconfigure(tongue_tip , state = NORMAL)
        c.itemconfigure(tongue_main , state = NORMAL)
        c.tonque_out = True
    else:
        c.itemconfigure(tongue_tip , state = HIDDEN)
        c.itemconfigure(tongue_main , state = HIDDEN)
        c.tonque_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pupils)
    return

def show_happy(event):
    if(20<= event.x and event.x <= 350) and (20<= event.y and event.y <= 350):
        c.itemconfigure(cheek_left , state = NORMAL)
        c.itemconfigure(cheek_right , state = NORMAL)
        c.itemconfigure(mouth_happy , state = NORMAL)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        c.happy_level = 10
    return

def hide_happy(event):
    c.itemconfigure(cheek_left , state = HIDDEN)
    c.itemconfigure(cheek_right , state = HIDDEN)
    c.itemconfigure(mouth_happy , state = HIDDEN)
    c.itemconfigure(mouth_normal , state = NORMAL)
    c.itemconfigure(mouth_sad, state = HIDDEN)
    return

def sad():
    if c.happy_level == 0 :
        c.itemconfigure(mouth_happy , state = HIDDEN)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad , state = NORMAL)
    else:
        c.happy_level -= 1
    win.after(500,sad)


operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add , 'ADDED':add,'+':add,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub, 'SUBTRACTED' : sub, '-':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul, 'MULTIPLIED' : mul,'*':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div,'DIVIDED':div,'/':div, 'MOD':mod ,'%':mod,
                  'REMAINDER':mod , 'MODULUS':mod}

win = Tk()

win.geometry('600x670')
win.title('Smart Tiya')
win.configure(bg='#14213d')


c = Canvas(win , width=400 , height=400)
c.configure(bg='#14213d' , highlightthickness=0)

c.body_color = '#ffd32a'

body = c.create_oval(55,20,320,300,outline=c.body_color , fill=c.body_color)
foot_left = c.create_oval(65,280,145,310 , outline=c.body_color , fill=c.body_color)
foot_right = c.create_oval(225,280,305,310 , outline=c.body_color , fill=c.body_color)

ear_left = c.create_polygon(78,80,78,10,165,70,outline=c.body_color , fill=c.body_color)
ear_right = c.create_polygon(230,45,289,10,289,70,outline=c.body_color , fill=c.body_color)

eye_left = c.create_oval(120,110,150,170,outline='black' , fill='white')
pupil_left = c.create_oval(130,145,140,155,outline='black' , fill='black')
eye_right = c.create_oval(230,110,260,170,outline='black' , fill='white')
pupil_right = c.create_oval(240,145,250,155,outline='black' , fill='black')

mouth_normal = c.create_line(160,230,190,250,220,230,smooth=1 , width=2 , state=NORMAL)
mouth_happy = c.create_line(160,230,190,265,220,230,smooth=1 , width=2 , state=HIDDEN)
mouth_sad = c.create_line(160,230,190,212,220,230,smooth=1 , width=2 , state=HIDDEN)

tongue_main = c.create_rectangle(160,230,220,270,outline='red' , fill='red',state=HIDDEN)
tongue_tip = c.create_oval(160,255,220,280,outline='red' , fill='red',state=HIDDEN)

cheek_left = c.create_oval(70,180,120,230,outline='pink' , fill='#d63031',state=HIDDEN)
cheek_right = c.create_oval(255,180,305,230,outline='pink' , fill='#d63031',state=HIDDEN)

c.place(x=110,y=90)

c.bind('<Motion>' , show_happy)
c.bind('<Leave>' , hide_happy)
c.bind('<Double-1>' , cheeky)

c.crossed_eyes = False
c.tonque_out = False
c.happy_level = 10

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')



l1 = Label(win , text='Hello! My name is Tiya',width=26 ,font=("Arial", 18))
l1.place(x=110,y=10)
l2 = Label(win , text='I am a Smart Calculator' , padx=3,font=("Arial", 12))
l2.place(x=215,y=55)
l3 = Label(win , text='How can i help you?',font=("Arial", 12))
l3.place(x=225,y=430)

textin = StringVar()
e1 = Entry(win , width=30, textvariable = textin,font=("Arial", 17))
e1.place(x=105,y=465)

b1 = Button(win , text='Just this' ,command=calculate,font=("Arial", 9))
b1.place(x=270,y=505)

list = Listbox(win,width=30,height=3,font=("Arial", 18))
list.place(x=105,y=540)

win.after(1000,blink)
win.after(5000,sad)

win.resizable(0, 0) 
win.mainloop()
