import tkinter as tk
from tkinter import Label, Toplevel, mainloop, messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk
from addMovie import open_add_movie
from deleteMovie import open_delete_movie
from showList import open_show_movie
from Reservations import open_reservations


class MyGUI:
    def __init__(self):
        # Making the GUI
        self.root = tk.Tk()
        self.root.title("Our Cinema")
        self.root.geometry("1280x720")
        # putting an image as a BackGround
        self.bg = ImageTk.PhotoImage(Image.open("images/1.jpg"))
        self.bg_lab = Label(self.root, image=self.bg)
        self.bg_lab.place(x=0, y=0, relheight=1, relwidth=1)

        # making the menuBar
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close without Q", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(
            label="Add Movie", command=lambda: open_add_movie(self.root))
        self.actionmenu.add_separator()
        self.actionmenu.add_command(
            label="Delete Movie", command=lambda: open_delete_movie(self.root))
        self.actionmenu.add_separator()
        self.actionmenu.add_command(
            label="Show Movie List", command=lambda: open_show_movie(self.root))
        self.actionmenu.add_separator()
        self.actionmenu.add_command(
            label="Reservations", command=lambda: open_reservations(self.root))

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(
            self.root, text="Welcome to our Cinema", font=('Helvetica', 40, BOLD), bg="#adb901")
        self.label.pack(padx=10, pady=30)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.columnconfigure(0, weight=1)

        self.Button = tk.Button(
            self.btn_frame, text="Add a Movie", font=('Arial', 25), bg="#fd5301", command=lambda: open_add_movie(self.root))
        self.Button.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.Button1 = tk.Button(
            self.btn_frame, text="Delete a Movie", font=('Arial', 25), bg="#fd5301", command=lambda: open_delete_movie(self.root))
        self.Button1.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.Button2 = tk.Button(
            self.btn_frame, text="Show our Movies list", font=('Arial', 25), bg="#fd5301", command=lambda: open_show_movie(self.root))
        self.Button2.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.Button3 = tk.Button(
            self.btn_frame, text="Reservations", font=('Arial', 25), bg="#fd5301", command=lambda: open_reservations(self.root))
        self.Button3.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.btn_frame.pack(pady=150)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


MyGUI()
