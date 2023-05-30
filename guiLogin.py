from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label, Image, Toplevel
from pathlib import Path
import emoji
import tkinter
import sqlite3
# Ne conectam la baza de date]
conn = sqlite3.connect('SmartRecipeDatabase1.db')
 
# Creem un cursor cursor 
cursor = conn.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assetsLogin\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Login():
    print('it works')
    LoginF()

def Register():
    print('it works')

def ChangeState(text,var):
    var.set(text)
    return 1

myValue = 0
myEmoji = emoji.emojize(':face_without_mouth:')
def passView(entry_1, button_5, image_image_5, image_image_6):
    global myValue
    if myValue == 0:
        button_5.config(image=image_image_5)
        entry_1.config(show= "")
        myValue = 1
    else:
        button_5.config(image= image_image_6)
        entry_1.config(show= f"{myEmoji}")
        myValue = 0
     




def getUserData(entry_2,entry_1,var,varPass,varUser):
    cursor.execute('select * from UsersView')
    rows = cursor.fetchall()
    for row in rows:
        if entry_2.get() == row[0]:
            if entry_1.get() == row[1]:
                ChangeState(f"Log in Successfully {entry_2.get()} ",var)
            else:
                ChangeState('Wrong Password',var)
        else:
            ChangeState('Wrong Datas',var)
    ChangeState('',varPass)
    ChangeState('',varUser)        
    return 0




def LoginF():


    window = Tk()
    
    window.geometry("1366x768")
    window.configure(bg = "#FFFFFF")

    var=tkinter.StringVar(window)
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 668,
        width = 1266,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.create_rectangle(
        50.0,
        43.0,
        1316.0,
        711.0,
        fill="#F2E3DB",
        outline="")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        50.0,
        50.0,
        1316.0,
        718.0,
        fill="#F2E3DB",
        outline="")
    canvas.create_text(
        906.0,
        290.0,
        anchor="nw",
        text="Username",
        fill="#E86A33",
        font=("Basic Regular", 12 * -1)
    )

    canvas.create_text(
        906.0,
        345.0,
        anchor="nw",
        text="Password",
        fill="#E86A33",
        font=("Basic Regular", 12 * -1)
    )
    # Main photo
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        436.0,
        384.0,
        image=image_image_1
    )
    image_image_5 = PhotoImage(
        file=relative_to_assets("show.png"))
    image_image_6 = PhotoImage(
        file=relative_to_assets("hide.png"))
    canvas.create_text(
        904.0,
        590.0,
        anchor="nw",
        text="Forgot passwod?",
        fill="#E86A33",
        font=("Basic Regular", 14 * -1)
    )

    # Password entry
    varPass = tkinter.StringVar()
    entry_1 = Entry(
        bd=0,
        bg="#bfdcc3",
        fg="#000716",
        highlightthickness=0,
        show = f"{myEmoji}",
        textvariable=varPass,
    )
    entry_1.place(
        x=905.0,
        y=360.0,
        width=280.0,
        height=32.0
    )
    button_5 = Button(
        borderwidth=0,
        highlightthickness=0,
        command=lambda: passView(entry_1, button_5, image_image_5, image_image_6),
        relief="flat",
        text = "",
        activebackground = "#92a995",
        bg = "#bfdaaa",
        image=image_image_5
    )
    button_5.place(
        x=1185.0,
        y=360.0,
        width=32.0,
        height=32.0
    )

    # Username Entry
    varUser = tkinter.StringVar()
    entry_2 = Entry(
        bd=0,
        bg="#bfdcc3",
        fg="#000716",
        highlightthickness=0,
        exportselection = 1,
        textvariable = varUser,
    )
    entry_2.place(
        x=905.0,
        y=306.0,
        width=312.0,
        height=32.0
    )

    entry_4 = Label(
        bd=0,
        bg="#f2e3db",
        fg="#000716",
        textvariable= var,
        highlightthickness=0
    )
    entry_4.place(
        x=906.0,
        y=400.0,
        width=312.0,
        height=32.0
    )


    # Ok Button
    button_1 = Button(
        borderwidth=0,
        highlightthickness=0,
        command=lambda :getUserData(entry_2, entry_1,var, varPass, varUser),
        relief="flat",
        text = "OK",
        activebackground = "#92a995",
        bg = "#507b57",
        fg = "#FFFFFF"
    )
    button_1.place(
        x=1060.0,
        y=581.0,
        width=156.00634765625,
        height=39.0
    )
    canvas.create_text(
        904.0,
        220.0,
        anchor="nw",
        text="Welcome",
        fill="#000000",
        font=("Basic Regular", 36 * -1)
    )
    button_4 = Button(
        text="Forgot passwrod?",
        fg="#E86A33",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ChangeState("It's your Problem:)",var),
        relief="flat",
        bg="#f2e3db",
        activebackground = "#f2e3db"
    )
    button_4 .place(
        x = 904.0,
        y = 580.0,        
        width=156.00634765625,
        height=39.0
    )
    # Register Button
    button_2 = Button(
        bg = "#bfdcc3",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Register(),
        relief="ridge",
        text= "Register",
        activebackground = "#92a995"
    )
    button_2.place(
        x=1060.0,
        y=142.0,
        width=157.0,
        height=40.0
    )

    canvas.create_text(
        1060.0,
        143.0,
        anchor="nw",
        text="Register",
        fill="#000000",
        font=("Basic Regular", 15 * -1)
    )
    # Login button
    button_3 = Button(
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Login(),
        relief="flat",
        text = "Login",
        activebackground = "#92a995",
        bg = "#507b57",
        fg = "#FFFFFF"
    )
    button_3.place(
        x=904.0,
        y=142.0,
        width=156.0,
        height=40.0
    )


    
    canvas.create_text(
        904.0,
        143.0,
        anchor="nw",
        text="Login",
        fill="#FFFFFF",
        font=("Basic Regular", 15 * -1)
    )

    canvas.create_text(
        904.0,
        92.0,
        anchor="nw",
        text="Smart Recipes",
        fill="#E86A33",
        font=("Basic Regular", 40 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
    return 1

