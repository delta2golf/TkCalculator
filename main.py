from tkinter import *
from tkinter import messagebox

lastupdate = "7/5/2017"


def main():
    root = Tk()
    tnum = DoubleVar()
    nextop = StringVar()

    root.title("Jared's Calculator")
    root.resizable(width=False, height=False)
    root.geometry("170x200")

    # Inserts text to the end of calculators display field
    # Clears the field if text starts with a char
    def pushfield(text):
        if field.get() and field.get()[0].isalpha():
            field.config(state="normal")
            field.delete(0, "end")
            field.insert(0, text)
            field.config(state="readonly")
        else:
            field.config(state="normal")
            field.insert("end", text)
            field.config(state="readonly")

    # Same implementation as above, for temp. operand field
    def pushtemp(text):
        # tempfield.delete(0, "end")
        field.config(state="normal")
        tempfield.insert("end", text)
        field.config(state="readonly")

    # Saves first operand to tnum and operator to nextop
    def setop(op):
        try:
            tnum.set(float(field.get()))
            field.config(state="normal")
            tempfield.config(state="normal")
            field.delete(0, "end")
            nextop.set(op)
            pushtemp(tnum.get())
            field.config(state="readonly")
            tempfield.config(state="readonly")
        except (TypeError, ValueError):
            pass

    # Computes the answer based on nextop
    # Resets field/tempfield to display the answer
    def eqop(event):
        op = nextop.get()
        tempfield.config(state="normal")
        field.config(state="normal")
        tempfield.delete(0, "end")
        try:
            if op == "+":
                tans = tnum.get() + float(field.get())
                field.delete(0, "end")
                field.insert(0, tans)
            elif op == "-":
                tans = tnum.get() - float(field.get())
                field.delete(0, "end")
                field.insert(0, tans)
            elif op == "*":
                tans = tnum.get() * float(field.get())
                field.delete(0, "end")
                field.insert(0, tans)
            elif op == "/":
                tans = tnum.get() / float(field.get())
                field.delete(0, "end")
                field.insert(0, tans)
            elif op == "^":
                tans = tnum.get() ** float(field.get())
                field.delete(0, "end")
                field.insert(0, tans)
            nextop.set(nextop.get())
        except (TypeError, IndexError):
            # Nothing can/should be done
            pass
        except ValueError:
            field.delete(0, "end")
            nextop.set("")
            field.insert(0, "Incorrect format.")
        tempfield.config(state="readonly")
        field.config(state="readonly")

    # Deletes the last character in field
    def delop(event):
        field.config(state="normal")
        field.delete(len(field.get())-1, "end")
        field.config(state="readonly")

    # Clears the field, tempfield, and nextop
    def clrop(event):
        nextop.set("")
        field.config(state="normal")
        tempfield.config(state="normal")
        tempfield.delete(0, "end")
        field.delete(0, "end")
        field.config(state="readonly")
        tempfield.config(state="readonly")

    # Displays an info msg box which gives some basic program info
    def infomsg():
        infomessage = "A simple calculator made by Jared Jacobson.\nUsing Tkinter and Python 3.4.\n" \
                      "Last updated: " + lastupdate
        messagebox.showinfo("Info", infomessage)

    # Menu navigation bar
    menubar = Menu(root)
    menubar.add_command(label="Info", command=infomsg)
    menubar.add_command(label="Quit", command=root.quit)
    root.configure(menu=menubar)

    # Main display field
    fieldtext = StringVar()
    fieldtext.set("Welcome to my calculator!")
    field = Entry(root, state="readonly", textvariable=fieldtext)
    field.grid(row=1, column=1, columnspan=3, ipadx=10, padx=10)

    # Temp number field
    tempftext = StringVar()
    tempfield = Entry(root, state="readonly", textvariable=tempftext)
    tempfield.grid(row=0, column=1, columnspan=3)

    # Number buttons
    b1 = Button(root, text="1")
    b1.grid(row=2, column=1, ipadx=10)
    b2 = Button(root, text="2")
    b2.grid(row=2, column=2, ipadx=10)
    b3 = Button(root, text="3")
    b3.grid(row=2, column=3, ipadx=10)
    b4 = Button(root, text="4")
    b4.grid(row=3, column=1, ipadx=10)
    b5 = Button(root, text="5")
    b5.grid(row=3, column=2, ipadx=10)
    b6 = Button(root, text="6")
    b6.grid(row=3, column=3, ipadx=10)
    b7 = Button(root, text="7")
    b7.grid(row=4, column=1, ipadx=10)
    b8 = Button(root, text="8")
    b8.grid(row=4, column=2, ipadx=10)
    b9 = Button(root, text="9")
    b9.grid(row=4, column=3, ipadx=10)
    b0 = Button(root, text="0")
    b0.grid(row=5, column=2, ipadx=10)
    bdot = Button(root, text=".")
    bdot.grid(row=7, column=1, ipadx=10)

    # Number button bindings
    b1.bind("<Button-1>", lambda e: pushfield("1"))
    b2.bind("<Button-1>", lambda e: pushfield("2"))
    b3.bind("<Button-1>", lambda e: pushfield("3"))
    b4.bind("<Button-1>", lambda e: pushfield("4"))
    b5.bind("<Button-1>", lambda e: pushfield("5"))
    b6.bind("<Button-1>", lambda e: pushfield("6"))
    b7.bind("<Button-1>", lambda e: pushfield("7"))
    b8.bind("<Button-1>", lambda e: pushfield("8"))
    b9.bind("<Button-1>", lambda e: pushfield("9"))
    b0.bind("<Button-1>", lambda e: pushfield("0"))
    bdot.bind("<Button-1>", lambda e: pushfield("."))

    # Operation buttons
    bplus = Button(root, text="+")
    bplus.grid(row=5, column=1, ipadx=10)
    bsub = Button(root, text="-")
    bsub.grid(row=5, column=3, ipadx=10)
    bmul = Button(root, text="*")
    bmul.grid(row=6, column=1, ipadx=10)
    bdiv = Button(root, text="/")
    bdiv.grid(row=6, column=3, ipadx=10)
    bexp = Button(root, text="^")
    bexp.grid(row=6, column=2, ipadx=10)
    be = Button(root, text="=")
    be.grid(row=7, column=3, ipadx=10)
    bclr = Button(root, text="Clear")
    bclr.grid(row=7, column=2)

    # Operation button bindings
    bplus.bind("<Button-1>", lambda e: setop("+"))
    bsub.bind("<Button-1>", lambda e: setop("-"))
    bmul.bind("<Button-1>", lambda e: setop("*"))
    bdiv.bind("<Button-1>", lambda e: setop("/"))
    bexp.bind("<Button-1>", lambda e: setop("^"))
    be.bind("<Button-1>", eqop)
    bclr.bind("<Button-1>", clrop)

    # Keyboard bindings
    root.bind("1", lambda e: pushfield("1"))
    root.bind("2", lambda e: pushfield("2"))
    root.bind("3", lambda e: pushfield("3"))
    root.bind("4", lambda e: pushfield("4"))
    root.bind("5", lambda e: pushfield("5"))
    root.bind("6", lambda e: pushfield("6"))
    root.bind("7", lambda e: pushfield("7"))
    root.bind("8", lambda e: pushfield("8"))
    root.bind("9", lambda e: pushfield("9"))
    root.bind("0", lambda e: pushfield("0"))
    root.bind(".", lambda e: pushfield("."))

    root.bind("+", lambda e: setop("+"))
    root.bind("-", lambda e: setop("-"))
    root.bind("*", lambda e: setop("*"))
    root.bind("/", lambda e: setop("/"))
    root.bind("^", lambda e: setop("^"))
    root.bind("=", eqop)
    root.bind("<Return>", eqop)
    root.bind("<BackSpace>", delop)

    root.mainloop()


if __name__ == "__main__":
    main()
