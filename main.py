from tkinter import *
from customtkinter import *
from numpy import sqrt

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


class dist_a_b():
    def load():
        global program_items, program_frame, padding
        global title, a1, a2, a3, b1, b2, b3, result_label

        spacing = "          "

        title = CTkLabel(
            text = "Distancia de A a B",
            text_font = ("Arial", 16, "bold", UNDERLINE),
            master = program_frame,
            fg_color = "#9EA6A9",
            corner_radius = 6,
            width = 250,
            height = 40)
        title.place(relx = 0.5, y = 30, anchor = CENTER)


        a_label = CTkLabel(
            text = f"A({spacing},{spacing},{spacing})",
            text_font = ("Arial", 16, "bold"),
            master = program_frame,
            fg_color = "#afb6c1",
            corner_radius = 6,
            width = 300,
            height = 40)
        a_label.place(relx = 0.5, y = 100, anchor = CENTER)

        b_label = CTkLabel(
            text = f"B({spacing},{spacing},{spacing})",
            text_font = ("Arial", 16, "bold"),
            master = program_frame,
            fg_color = "#afb6c1",
            corner_radius = 6,
            width = 300,
            height = 40)
        b_label.place(relx = 0.5, y = 150, anchor = CENTER)

        a1 = CTkEntry(
            placeholder_text = " a1",
            text_font = ("Arial", 16),
            master = a_label,
            width = 62,
            height = 36,
            fg_color = "#afb6c1",
            corner_radius = 6,
            border_width = 1)
        a1.place(x = 50, y = 2)

        a2 = CTkEntry(
            placeholder_text = " a2",
            text_font = ("Arial", 16),
            master = a_label,
            width = 62,
            height = 36,
            fg_color = "#afb6c1",
            corner_radius = 6,
            border_width = 1)
        a2.place(x = 127, y = 2)

        a3 = CTkEntry(
            placeholder_text = " a3",
            text_font = ("Arial", 16),
            master = a_label,
            width = 62,
            height = 36,
            fg_color = "#afb6c1",
            corner_radius = 6,
            border_width = 1)
        a3.place(x = 204, y = 2)

        b1 = CTkEntry(
            placeholder_text = " b1",
            text_font = ("Arial", 16),
            master = b_label,
            width = 62,
            height = 36,
            fg_color = "#afb6c1",
            corner_radius = 6,
            border_width = 1)
        b1.place(x = 50, y = 2)

        b2 = CTkEntry(
            placeholder_text = " b2",
            text_font = ("Arial", 16),
            master = b_label,
            width = 62,
            height = 36,
            fg_color = "#afb6c1",
            corner_radius = 6,
            border_width = 1)
        b2.place(x = 127, y = 2)

        b3 = CTkEntry(
            placeholder_text = " b3",
            text_font = ("Arial", 16),
            master = b_label,
            width = 62,
            height = 36,
            fg_color = "#afb6c1",
            corner_radius = 6,
            border_width = 1)
        b3.place(x = 204, y = 2)

        calculate_button = CTkButton(
            text = "Calcular",
            text_font = ("Arial", 13),
            master = program_frame,
            fg_color = "#53ce69",
            hover = True,
            hover_color = "#34B74B",
            command = dist_a_b.calculate,
            width = 120,
            height = button_height,
            corner_radius = 12)
        calculate_button.place(relx = 0.5, y = 230, anchor = CENTER)

        result_label = CTkLabel(
            text = "RESULTADO: ",
            anchor = "w",
            text_font = ("Arial", 13, "bold"),
            master = program_frame,
            fg_color = "#9EA6A9",
            corner_radius = 20,
            width = 490,
            height = 40)
        result_label.place(relx = 0.5, y = 300, anchor = CENTER)


    def calculate():
        global a1, a2, a3, b1, b2, b3, result_label

        try:
            a1_ = eval(a1.get())
            a2_ = eval(a2.get())
            a3_ = eval(a3.get())
            b1_ = eval(b1.get())
            b2_ = eval(b2.get())
            b3_ = eval(b3.get())

            result = sqrt(pow(b1_ - a1_, 2) + pow(b2_ - a2_, 2) + pow(b3_ - a3_, 2))

            result_label.config(text = f"RESULTADO: {round(result, 2)}u")

        except:
            result_label.config(text = f"RESULTADO: ¡Rellena todos los campos!")


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


calculate_button = CTkButton(
    text = "Distancia de A a B",
    text_font = ("Arial", 13),
    master = button_frame,
    fg_color = "#41A7EE",
    hover = True,
    hover_color = "#2290DD",
    command = dist_a_b.load,
    width = 240,
    height = button_height,
    corner_radius = 12)
calculate_button.place(x = padding, y = padding)

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