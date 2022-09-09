import tkinter as tk
from tkinter import Button, Label, Toplevel
from tkinter.font import BOLD
from PIL import Image, ImageTk
movies_path = "files/Movies.csv"


def open_show_movie(root):
    show_page = Toplevel(root)
    show_page.title("Show our list")
    show_page.geometry("1280x720")
    bg_show = ImageTk.PhotoImage(Image.open("images/3.jpg"))
    bg_lab_show = Label(show_page, image=bg_show)
    bg_lab_show.place(x=0, y=0, relheight=1, relwidth=1)
    show_lab1 = Label(show_page, font=(
        'Arial', 40, BOLD), text="show Movies List", bg="#adb901")
    show_lab1.pack(padx=10, pady=10)
    show_frame = tk.Frame(show_page, bg="#adb901")
    show_frame.columnconfigure(0, weight=1)
    show_frame.columnconfigure(1, weight=1)
    show_frame.columnconfigure(2, weight=1)
    show_frame.columnconfigure(3, weight=1)
    Action_btn = Button(show_frame, text="Action",
                        font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Action_btn.cget("text")), show_lab_names))
    Action_btn.grid(column=0, row=0, sticky=tk.W+tk.E)
    Drama_btn = Button(show_frame, text="Drama",
                       font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Drama_btn.cget("text")), show_lab_names))
    Drama_btn.grid(column=1, row=0, sticky=tk.W+tk.E)
    Comedy_btn = Button(show_frame, text="Comedy",
                        font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Comedy_btn.cget("text")), show_lab_names))
    Comedy_btn.grid(column=2, row=0, sticky=tk.W+tk.E)
    Fantasy_btn = Button(show_frame, text="Fantasy",
                         font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Fantasy_btn.cget("text")), show_lab_names))
    Fantasy_btn.grid(column=3, row=0, sticky=tk.W+tk.E)
    Horror_btn = Button(show_frame, text="Horror",
                        font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Horror_btn.cget("text")), show_lab_names))
    Horror_btn.grid(column=0, row=1, sticky=tk.W+tk.E)
    Romance_btn = Button(show_frame, text="Romance",
                         font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Romance_btn.cget("text")), show_lab_names))
    Romance_btn.grid(column=1, row=1, sticky=tk.W+tk.E)
    Thriller_btn = Button(show_frame, text="Thriller",
                          font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Thriller_btn.cget("text")), show_lab_names))
    Thriller_btn.grid(column=2, row=1, sticky=tk.W+tk.E)
    Western_btn = Button(show_frame, text="Western",
                         font=('Arial', 25, BOLD), bg="#fd5301", command=lambda: making_label(getting_names(Western_btn.cget("text")), show_lab_names))
    Western_btn.grid(column=3, row=1, sticky=tk.W+tk.E)

    show_lab_names = Label(show_frame, text="",
                           font=('Arial', 25), bg="#adb901")
    show_lab_names.grid(column=0, row=2, columnspan=4,
                        pady=40, sticky=tk.W+tk.E)
    show_frame.pack(fill='x', pady=30)

    tk.mainloop()


is_on = True


def getting_names(text):
    movies_to_show = []
    dates = []
    directors = []
    with open(movies_path, "r") as file:
        for line in file:
            row = line.rstrip().split(",")
            genre_type = row[-1].split("|")
            for kind in genre_type:
                if text.lower() == kind.lower():
                    movies_to_show.append(row[0])
                    dates.append(row[1])
                    directors.append(row[2])
    return [movies_to_show, dates, directors]


def making_label(names, lab):
    s = ""
    movies_names = ""
    for i in range(len(names[0])):
        s = s + \
            f"Movie: {names[0][i]} ------- Release date: {names[1][i]} ------- Directed by: {names[2][i]}\n"
    movies_names = s.removesuffix('\n')
    lab['text'] = movies_names.rstrip()
