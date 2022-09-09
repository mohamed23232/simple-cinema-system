import io
import tkinter as tk
from tkinter import Button, Checkbutton, Entry, Label, Toplevel, messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk
import csv
movies_path = "files/Movies.csv"


def open_add_movie(root):
    add_page = Toplevel(root)
    add_page.title("add movies")
    add_page.geometry("1280x720")
    # putting an image as a BackGround
    bg_add = ImageTk.PhotoImage(Image.open("images/2.jpg"))
    bg_lab_add = Label(add_page, image=bg_add)
    bg_lab_add.place(x=0, y=0, relheight=1, relwidth=1)
    add_lab1 = Label(add_page, font=(
        'Arial', 40, BOLD), text="Add Movie", bg="#adb901")
    add_lab1.pack(padx=10, pady=10)

    add_frame = tk.Frame(add_page, bg="#adb901")
    add_frame.columnconfigure(0, weight=1)
    add_frame.columnconfigure(1, weight=1)
    add_lab_movie = Label(add_frame, font=('Arial', 22),
                          text="Enter the name of the movie : ", bg="#adb901")
    add_lab_movie.grid(column=0, row=0, sticky="W")
    movie_name = Entry(add_frame, font=('Arial', 22))
    movie_name.grid(column=1, row=0, pady=20)
    add_lab_release_date = Label(add_frame, font=('Arial', 22),
                                 text="Enter Release Date : ", bg="#adb901")
    add_lab_release_date.grid(column=0, row=1, pady=20, sticky="W")
    release_date = Entry(add_frame, font=('Arial', 22))
    release_date.grid(column=1, row=1, pady=20)
    add_Director = Label(add_frame, font=('Arial', 22),
                         text="Enter the Director name : ", bg="#adb901")
    add_Director.grid(column=0, row=2, pady=20, sticky="W")
    Director = Entry(add_frame, font=('Arial', 22))
    Director.grid(column=1, row=2, pady=20)
    add_genres_movies = Label(add_frame, font=('Arial', 25),
                              text="Choose the Genres of the movie", bg="#adb901")
    add_genres_movies.grid(column=0, row=3, pady=20, columnspan=2)
    options_frame = tk.Frame(add_frame)
    options_frame.columnconfigure(0, weight=1)
    options_frame.columnconfigure(1, weight=1)
    options_frame.columnconfigure(2, weight=1)
    options_frame.columnconfigure(3, weight=1)
    options_frame.columnconfigure(4, weight=1)
    options_frame.columnconfigure(5, weight=1)
    options_frame.columnconfigure(6, weight=1)

    ch = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),
          tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]

    add_genres_Options_Action = Checkbutton(
        options_frame, text="Action", font=('Arial', 18), bg="#adb901", variable=ch[0])
    add_genres_Options_Action.grid(column=0, row=0)
    add_genres_Options_Drama = Checkbutton(
        options_frame, text="Drama", font=('Arial', 18), bg="#adb901", variable=ch[1])
    add_genres_Options_Drama.grid(column=1, row=0)
    add_genres_Options_Comedy = Checkbutton(
        options_frame, text="Comedy", font=('Arial', 18), bg="#adb901", variable=ch[2])
    add_genres_Options_Comedy.grid(column=2, row=0)
    add_genres_Options_Fantasy = Checkbutton(
        options_frame, text="Fantasy", font=('Arial', 18), bg="#adb901", variable=ch[3])
    add_genres_Options_Fantasy.grid(column=3, row=0)
    add_genres_Options_Horror = Checkbutton(
        options_frame, text="Horror", font=('Arial', 18), bg="#adb901", variable=ch[4])
    add_genres_Options_Horror.grid(column=4, row=0)
    add_genres_Options_Romance = Checkbutton(
        options_frame, text="Romance", font=('Arial', 18), bg="#adb901", variable=ch[5])
    add_genres_Options_Romance.grid(column=5, row=0)
    add_genres_Options_Thriller = Checkbutton(
        options_frame, text="Thriller", font=('Arial', 18), bg="#adb901", variable=ch[6])
    add_genres_Options_Thriller.grid(column=6, row=0)
    add_genres_Options_Western = Checkbutton(
        options_frame, text="Western", font=('Arial', 18), bg="#adb901", variable=ch[7])
    add_genres_Options_Western.grid(column=7, row=0)
    options_frame.grid(column=0, row=4, pady=5, columnspan=2)

    genres_objects = [add_genres_Options_Action, add_genres_Options_Drama, add_genres_Options_Comedy, add_genres_Options_Fantasy,
                      add_genres_Options_Horror, add_genres_Options_Romance, add_genres_Options_Thriller, add_genres_Options_Western]
    submit_btn = Button(add_frame, text="Submit",
                        font=('Arial', 30, BOLD), bg="#fd5301", command=lambda: adding(movie_name, release_date, Director, ch, genres_objects, add_page))
    submit_btn.grid(column=0, row=5, sticky="W", pady=40)

    reset_btn = Button(add_frame, text="Reset",
                       font=('Arial', 30, BOLD), bg="#fd5301", command=lambda: clear_fields(movie_name, release_date, Director, ch))
    reset_btn.grid(column=1, row=5, sticky="E", pady=40)

    add_frame.pack(padx=10, pady=70)

    add_page.mainloop()


def is_number(date):
    try:
        int(date.get())
        return True
    except ValueError:
        return False


def clear_fields(movie, date, director, li):
    movie.delete(0, tk.END)
    date.delete(0, tk.END)
    director.delete(0, tk.END)
    for i in li:
        i.set(0)


def adding(movie, date, director, li, li_text, window):
    t = ""
    for i in range(8):
        if li[i].get() == 1:
            t = t + li_text[i].cget("text") + "|"
    genres = t.removesuffix('|')
    with open(movies_path, "a", newline="") as file:
        file.seek(0, io.SEEK_END)
        if movie.get() != "" and date.get() != "" and director.get() != "" and is_number(date):
            writer = csv.DictWriter(
                file, fieldnames=['Name', 'Date', 'Director', 'genres'])
            writer.writerow({'Name': movie.get(), 'Date': date.get(),
                            'Director': director.get(), 'genres': genres})
            messagebox.showinfo(title="Success", message="DONE", parent=window)
        elif is_number(date) == False and date.get() != "":
            messagebox.showerror(
                title="Error", message="data must be a number", parent=window)
        else:
            messagebox.showerror(
                title="Error", message="You have to fill the blanks", parent=window)
    clear_fields(movie, date, director, li)
