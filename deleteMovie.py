import os
import tkinter as tk
from tkinter import Button, Entry, Label, Toplevel
from tkinter.font import BOLD
from PIL import Image, ImageTk
import csv

movies_path = "files/Movies.csv"
movies_path_edited = "files/Movies_edit.csv"


def open_delete_movie(root):
    delete_page = Toplevel(root)
    delete_page.title("Delete a movie")
    delete_page.geometry("1280x720")

    bg_delete = ImageTk.PhotoImage(Image.open("images/2.jpg"))
    bg_lab_delete = Label(delete_page, image=bg_delete)
    bg_lab_delete.place(x=0, y=0, relheight=1, relwidth=1)
    delete_lab1 = Label(delete_page, font=(
        'Arial', 40, BOLD), text="Delete Movie", bg="#adb901")
    delete_lab1.pack(padx=10, pady=10)
    delete_frame = tk.Frame(delete_page, bg="#adb901")
    delete_frame.columnconfigure(0, weight=1)
    delete_frame.columnconfigure(1, weight=1)
    delete_lab_movie = Label(delete_frame, font=('Arial', 35),
                             text="Enter the name of the movie", bg="#adb901")
    delete_lab_movie.grid(column=0, row=0, columnspan=2)
    movie_name = Entry(delete_frame, font=('Arial', 25), width=30)
    movie_name.grid(column=0, row=1, pady=30, columnspan=2)
    submit_btn = Button(delete_frame, text="Submit",
                        font=('Arial', 40, BOLD), bg="#fd5301", command=lambda: delete_row(movie_name))
    submit_btn.grid(column=0, row=5, columnspan=2, pady=80)
    delete_frame.pack(padx=10, pady=120)
    tk.mainloop()


def delete_row(movie):
    with open(movies_path, "r") as infile, open(movies_path_edited, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        for row in csv.reader(infile):
            if row[0] != movie.get():
                writer.writerow(row)
    os.remove(movies_path)
    os.rename(movies_path_edited, movies_path)
    movie.delete(0, tk.END)
