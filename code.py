from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys, os
import subprocess as sp
import tkinter as tk
import time


from tkinter import *

if "chromedriver" not in os.environ:
    newPath = os.path.realpath("chromedriver.exe")
    sys.path.append(newPath)


width = 400
height = 300
global counter
global UsrPwn
UsrPwn = []
counter = 0

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        def logIn():
            def returnUser():
                print(a.get())
                if len(a.get()) != 0 and len(b.get()) != 0:
                    global UsrPwn
                    UsrPwn.append([a.get(), b.get()])
                    T = Text(self, height=2, width=30)
                    T.pack()
                    global counter
                    T.place(x=45, y=(7 + counter))
                    counter += 50
                    T.insert(END, "username: " + UsrPwn[-1][0] + "\npassword: " + UsrPwn[-1][1])
                    window.destroy
            window = tk.Toplevel(root)
            window.geometry('200x100')
            a = tk.Entry(window, text="username")
            b = tk.Entry(window, text="pass")
            c = Button(window, text="add account", command=returnUser)
            a.pack()
            b.pack()
            c.pack()

        # creating a button instance
        quitButton = Button(self, text="Exit", command=root.destroy)
        PlussButton = Button(self, text="Add account", command=logIn)
        MinusButton = Button(self, text="Remove account", command=root.destroy)
        global UsrPwn
        def startcheck():
            def check(usernamestr, passwordstr):

                browser = webdriver.Chrome()

                browser.get(('https://darkorbit.com/'))

                username = browser.find_element_by_id('bgcdw_login_form_username')
                username.send_keys(usernamestr)

                password = browser.find_element_by_id('bgcdw_login_form_password')
                password.send_keys(passwordstr)
                password.send_keys(Keys.RETURN)

                logged_in_page = browser.page_source

                uridium_tag =  "User.Parameters"
                position = logged_in_page.find(uridium_tag)
                uridium_amount =  logged_in_page[position + 31:position + 100]
                new = uridium_amount.split(",")
                uridium = ''.join(x for x in new[0] if x.isdigit())
                credit = ''.join(x for x in new[1] if x.isdigit())

                def rchop(thestring, ending):
                  if thestring.endswith(ending):
                    return thestring[:-len(ending)]
                  return thestring
                PATH = rchop(os.path.realpath(__file__), 'code.py') + "uridium_account"

                text_file = open(PATH, "r+")
                text_string = text_file.read()
                wantToWrite = usernamestr + ": uridium: %s   credit: %s " % (uridium, credit) + "\n"
                text_file.write(wantToWrite)

                browser.close()

            global UsrPwn
            def rchop(thestring, ending):
                if thestring.endswith(ending):
                    return thestring[:-len(ending)]
                return thestring
            PATH = rchop(os.path.realpath(__file__), 'code.py') + "uridium_account"
            f = open(PATH, 'r+')
            f.truncate()
            for element in UsrPwn:
                check(element[0],element[1])

            def rchop(thestring, ending):
              if thestring.endswith(ending):
                return thestring[:-len(ending)]
              return thestring
            PATH = rchop(os.path.realpath(__file__), 'code.py') + "uridium_account"

            programName = "notepad.exe"
            fileName = PATH
            sp.Popen([programName, fileName])

        check = Button(self, text="check all", command=startcheck)
        # placing the button on my window
        quitButton.place(x=5, y=5)
        PlussButton.place(x=3*width / 4, y=5)
        MinusButton.place(x=3*width / 4, y=35)
        check.place(x=3*width / 4, y=65)

root = Tk()

#size of the window
root.geometry(str(width) + "x" + str(height))

app = Window(root)
root.mainloop()  

#display hide