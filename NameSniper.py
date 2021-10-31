# Cardboard#5655's opensourced Minecraft NameSniper 2020

# import modules
import requests, time, os, sys
from tkinter import *
from PIL import ImageTk, Image, ImageSequence
import datetime as dt
from datetime import datetime
    
# User-Agent
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'


# Gui
class GUI:
    def __init__(self, window):
        
        self.we = Button(window,text='Block Method',command=GUI.buildtoken)
        self.we.place(x=90, y=120)

        self.we2 = Button(window,text='Namechange Method',command=GUI.buildname)
        self.we2.place(x=200, y=120)
        
        self.sm = Button(window,text='Quit Program', command=sys.exit)
        self.sm.place(x=155, y=300)
        
    # Build the menu
    def buildname():
        global A1, A2, A3, A4, E1, E2, E3, E4, we2, P, E6, E7, PP
        
        try:
            GUI.removethis1()
        except Exception:
            pass
        try:
            GUI.removethis2()
        except Exception:
            pass
        try:
            GUI.removebegin()
        except Exception:
            pass
        A1 = Label(window,text='Target')
        A1.place(x=10,y=180)
        E1 = Entry(window, bd =5)
        E1.place(x=10,y=200)
        
        
        A2 = Label(window,text='Bearer Key')
        A2.place(x=250,y=180)
        E2 = Entry(window, bd =5)
        E2.place(x=250,y=200)

        A3 = Label(window,text='Username')
        A3.place(x=10,y=260)
        E3 = Entry(window, bd =5)
        E3.place(x=10,y=280)

        A4 = Label(window,text='Password')
        A4.place(x=250,y=260)
        E4 = Entry(window, bd =5)
        E4.place(x=250,y=280)
        
        E6 = Label(window,text='Time of Availability')
        E6.place(x=10,y=340)
        P = Entry(window, bd =5)
        P.place(x=10,y=360)
        P.insert(0, dt.datetime.now().strftime("%H:%M:%S"))
        
        E7 = Label(window,text='Run Before Release Time')
        E7.place(x=250,y=340)
        PP = Entry(window, bd =5)
        PP.place(x=250,y=360)
        PP.insert(0, '.935')

        
        we2 = Button(window,text='Insert Info',command=GUI.insertinfo)
        we2.place(x=165, y=200)
        
        
    # Build the menu
    def buildtoken():
        global C1, W1, C2, W2, we3, Z1, P1, PP, W3

        try:
            GUI.removethis1()
        except Exception:
            pass
        try:
            GUI.removethis2()
        except Exception:
            pass
        try:
            GUI.removebegin()
        except Exception:
            pass
        C1 = Label(window,text='Target')
        C1.place(x=10,y=180)
        W1 = Entry(window, bd =5)
        W1.place(x=10,y=200)
        
        C2 = Label(window,text='Bearer Key')
        C2.place(x=250,y=180)
        W2 = Entry(window, bd =5)
        W2.place(x=250, y=200)
        
        
        Z1 = Label(window,text='Time of Availability')
        Z1.place(x=10,y=340)
        P1 = Entry(window, bd =5)
        P1.place(x=10,y=360)
        P1.insert(0, dt.datetime.now().strftime("%H:%M:%S"))
        
        W3 = Label(window,text='Run Before Release Time')
        W3.place(x=250,y=340)
        PP = Entry(window, bd =5)
        PP.place(x=250,y=360)
        PP.insert(0, '.935')
        
        we3 = Button(window,text='Insert Info',command=GUI.insertinfotoken)
        we3.place(x=165, y=200)


    # Removes menu of NameChange Method
    def removethis1():
        A1.destroy()
        E1.destroy()
        A2.destroy()
        E2.destroy()
        A3.destroy()
        E3.destroy()
        A4.destroy()
        E4.destroy()
        we2.destroy()
        E6.destroy()
        P.destroy()
        E7.destroy()
        PP.destroy()
        
    # Removes menu of Blank Method
    def removethis2():
        C1.destroy()
        W1.destroy()
        we3.destroy()
        W2.destroy()
        C2.destroy()
        P1.destroy()
        Z1.destroy()
        PP.destroy()
        W3.destroy()

    # Removes the begin button
    def removebegin():
        we.destroy()
        
    # Updates info
    def insertinfo():
        global username, password, profileid, auth, we

        # Inputs
        username = E1.get() # Target

        toke = E2.get() # Bearer Key

        try:
            ff = E3.get()
            us = req=requests.get(f'https://api.mojang.com/user/profile/agent/minecraft/name/{ff}').json()
            profileid = us['id'] # Profile ID / Trimmed UUID
        except Exception:
            print("That username that doesn't exist!")
            profileid = ''
        password = E4.get() # Password

        auth = 'Bearer ' + toke

        # Don't have empty lines
        if username == '':
            print('Missing Target Username!')
        elif toke == '':
            print('Missing Bearer Key!')
        elif profileid == '':
            print('Username!')
        elif password == '':
            print('Missing Password!')
        else:
            we = Button(window,text='Begin',command=GUI.name)
            we.place(x=175, y=250)
            
    # Updates info  
    def insertinfotoken():
        global target, auth, we

        # Inputs
        target = W1.get() # Target

        token = W2.get() # Bearer Key

        auth = 'Bearer ' + token

        # Don't have empty lines
        if target == '':
            print('Missing Target Username!')
        elif token == '':
            print('Missing Bearer Key!')
        else:
            we = Button(window,text='Begin',command=GUI.block)
            we.place(x=175, y=250)

    # Change the name
    def name():
        try:
            TimeOfAvailability = P.get()
            h = TimeOfAvailability.split(':')[0]
            m = TimeOfAvailability.split(':')[1]
            s = TimeOfAvailability.split(':')[2]
            if m == '00' and s == '00':
                if int(h) < 11:
                    hh = int(h) - 1
                    hh = '0' + str(hh)
                else:
                    hh = int(h) - 1
                    hh = str(hh)
                date = hh + ':59:59'
            elif s == '00':
                if int(m) < 11:
                    mm = int(m) - 1
                    mm = '0' +  str(mm)
                else:
                    mm = int(m) - 1
                    mm = str(mm)
                date = h + ':' + mm + ':59'
                
            else:
                if int(s) < 11:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + '0' + str(ss)
                else:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + str(ss)
            
            while True:
                # Grab the time right now
                now = dt.datetime.now().strftime("%H:%M:%S")
                    
                if now == date:
                    if '.' in PP.get():
                        time.sleep(float(PP.get()))
                    else:
                        time.sleep(int(PP.get()))
                    # Change the username
                    for i in range(3):
                        s=requests.post(f'https://api.mojang.com/user/profile/{profileid}/name', headers={'Authorization': auth,'User-Agent': useragent}, json={"name": username,"password": password})
                        if s.status_code == 204:
                            print(f'{username} is now yours!')
                            break
                        print(s.status_code)
                        print(s.text)
                    break

        except Exception as e:
            print(e)
            
    # Block the name
    def block():
        try:
            TimeOfAvailability = P1.get()
            h = TimeOfAvailability.split(':')[0]
            m = TimeOfAvailability.split(':')[1]
            s = TimeOfAvailability.split(':')[2]
            if m == '00' and s == '00':
                if int(h) < 11:
                    hh = int(h) - 1
                    hh = '0' + str(hh)
                else:
                    hh = int(h) - 1
                    hh = str(hh)
                date = hh + ':59:59'
            elif s == '00':
                if int(m) < 11:
                    mm = int(m) - 1
                    mm = '0' +  str(mm)
                else:
                    mm = int(m) - 1
                    mm = str(mm)
                date = h + ':' + mm + ':59'
                
            else:
                if int(s) < 11:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + '0' + str(ss)
                else:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + str(ss)
            while True:
                now = dt.datetime.now().strftime("%H:%M:%S")
                if now == date:
                    if '.' in PP.get():
                        time.sleep(float(PP.get()))
                    else:
                        time.sleep(int(PP.get()))
                    for i in range(3):
                        r=requests.put(f'https://api.mojang.com/user/profile/agent/minecraft/name/{target}', headers={'Authorization': auth,'User-Agent': useragent})
                        if r.status_code == 204:
                            print(f'{target} is now yours!')
                            break
                        print(r.status_code)
                        print(r.text)
                    break
        except Exception as e:
            print(e)
            
# Define parent
window=Tk()

# Define title
window.title('Minecraft NameSniper')

# Define Icon
r = requests.get('https://cdn.discordapp.com/attachments/673276807918649422/678376163244113920/ez.ico')
with open('ez.ico', 'wb') as f:
    f.write(r.content)
imgicon = PhotoImage('ez.ico')
window.tk.call('wm', 'iconphoto', window._w, imgicon)  
os.remove("ez.ico")



# Define size of 
window.geometry("400x400")
window.resizable(0,0)

# Define Banner
img_data = requests.get('https://cdn.discordapp.com/attachments/673276807918649422/678526638543208448/gg.png').content
with open('gg.png', 'wb') as f:
    f.write(img_data)
img = ImageTk.PhotoImage(Image.open('gg.png'))
img1 = Label(image=img)
img1.place(x=0,y=0)
os.remove('gg.png')

# Run Program
root = GUI(window)
window.mainloop()
