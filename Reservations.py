import io
from email.mime import image
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

from tkinter.font import BOLD
import csv
customers_path = "files/customers.csv"


def open_reservations(root):
    reservations_page = Toplevel(root)
    reservations_page.geometry("1280x720")
    reservations_page.title("reservations")

    bg = ImageTk.PhotoImage(Image.open("images/2.jpg"))
    bg_lab = Label(reservations_page, image=bg)
    bg_lab.place(x=0, y=0, relheight=1, relwidth=1)

    reservation_lab1 = Label(reservations_page, font=(
        'Arial', 40, BOLD), text="reserve movie", bg="#adb901")
    reservation_lab1.pack(padx=10, pady=10)

    fr1 = Frame(reservations_page, bg="#adb901")
    fr1.columnconfigure(0, weight=1)
    fr1.columnconfigure(1, weight=1)
    fr1_lb1 = Label(fr1, font=('Arial', 22),
                    text="Enter your name :", bg="#adb901")
    fr1_lb1.grid(row=0, column=0, sticky="W")
    your_name = Entry(fr1, font=('Arial', 22))
    your_name.grid(row=0, column=1, pady=20)
    fr1_lb2 = Label(fr1, font=('Arial', 22),
                    text="Enter the name of the movie :", bg="#adb901")
    fr1_lb2.grid(row=1, column=0, sticky="W")
    movie_name = Entry(fr1, font=('Arial', 22))
    movie_name.grid(row=1, column=1, pady=20)
    fr1.pack(padx=10, pady=70)
    fr2 = Frame(fr1, bg="#adb901")
    fr2.columnconfigure(0, weight=1)
    fr2.columnconfigure(1, weight=1)
    fr2.columnconfigure(2, weight=1)

    choice = IntVar()
    opt1 = Radiobutton(fr2, text="9:30 to 11:00", font=(
        'Arial', 18), bg="#adb901", value=1, variable=choice)
    opt1.grid(row=0, column=0)
    opt2 = Radiobutton(fr2, text="11:30 to 1:00", font=(
        'Arial', 18), bg="#adb901", value=2, variable=choice)
    opt2.grid(row=0, column=1)
    opt3 = Radiobutton(fr2, text="1:30 to 3:00", font=(
        'Arial', 18), bg="#adb901", value=3, variable=choice)
    opt3.grid(row=0, column=2)
    fr2.grid(row=3, column=0, columnspan=2)

    sub_btn = Button(fr1, text="Submit", font=('Arial', 30, BOLD), bg="#fd5301",
                     command=lambda: reserve(your_name, movie_name, choice, reservations_page))
    sub_btn.grid(row=4, column=0, columnspan=2, sticky=W+E, pady=40)
   # res_btn=Button(fr1,text="reset",font=('Arial', 30, BOLD), bg="#fd5301")
   # res_btn.grid(row=4,column=1,sticky="E", pady=40)

    reservations_page.mainloop()


def reserve(nam, mov, cho, window):
    with open(customers_path, "a", newline="") as file:
        file.seek(0, io.SEEK_END)
        if nam.get() != "" and mov.get() != "" and cho.get() != 0:
            writer = csv.DictWriter(
                file, fieldnames=['Name', 'movie', 'time', ])
            writer.writerow(
                {'Name': nam.get(), 'movie': mov.get(), 'time': cho.get()})
            messagebox.showinfo(title="Success", message="DONE", parent=window)
        else:
            messagebox.showerror(
                title="Error", message="You have to fill the blanks", parent=window)
    nam.delete(0, tk.END)
    mov.delete(0, tk.END)
    cho = 0
