from tkinter import *
from customtkinter import *

current_version = 0.1

WIDTH, HEIGHT = 800, 350

padding = 10
button_height = 50

root = Tk()
root.title(f"SMath {current_version}")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.focus_set()
root.configure(background = "#D3D4D5")

root.resizable(False, False)


def test():
    print("test :)")


program_items = []  # Will contain every item of the current program, so they can be destroyed when the user wants to use another one


def dist_a_b_load():
    global program_items, program_frame, padding
    global title, a1, a2, a3, b1, b2, b3

    title = CTkLabel(
        text = "Distancia de A a B",
        text_font = ("Arial", 16, "bold"),
        master = program_frame,
        fg_color = "#9EA6A9",
        corner_radius = 4,
        width = 250,
        height = 40)
    title.place(relx = 0.5, y = 30, anchor = CENTER)


def unload_program():
    pass


button_frame = CTkFrame(
    master = root,
    fg_color = "#BEBFC1",
    corner_radius = 20,
    width = 260,
    height = HEIGHT - padding * 2)
button_frame.place(x = 10, y = 10)

program_frame = CTkFrame(
    master = root,
    fg_color = "#BEBFC1",
    corner_radius = 20,
    width = 510,
    height = HEIGHT - padding * 2)
program_frame.place(x = 280, y = 10)


dist_a_b_button = CTkButton(
    text = "Distancia de A a B",
    text_font = ("Arial", 13),
    master = button_frame,
    fg_color = "#41A7EE",
    hover = True,
    hover_color = "#2290DD",
    command = dist_a_b_load,
    width = 240,
    height = button_height,
    corner_radius = 12)
dist_a_b_button.place(x = padding, y = padding)

dist_p_r_button = CTkButton(
    text = "Distancia de P a r",
    text_font = ("Arial", 13),
    master = button_frame,
    fg_color = "#41A7EE",
    hover = True,
    hover_color = "#2290DD",
    command = test,
    width = 240,
    height = button_height,
    corner_radius = 12)
dist_p_r_button.place(x = padding, y = padding * 2 + button_height)

dist_2_pl_button = CTkButton(
    text = "Distancia entre 2 planos",
    text_font = ("Arial", 13),
    master = button_frame,
    fg_color = "#41A7EE",
    hover = True,
    hover_color = "#2290DD",
    command = test,
    width = 240,
    height = button_height,
    corner_radius = 12)
dist_2_pl_button.place(x = padding, y = padding * 3 + button_height * 2)


root.mainloop()