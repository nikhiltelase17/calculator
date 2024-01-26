import tkinter as tk
import pygame

window = tk.Tk()
window.minsize(width=300, height=400)
window.title("Calculator")
window.config(pady=50, padx=50)
result = " "

pygame.mixer.init()
click_sound = pygame.mixer.Sound("click_effect-86995.mp3")


def show7():
    global result
    result += "7"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show8():
    global result
    result += "8"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show9():
    global result
    result += "9"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show_divide():
    global result
    result += "/"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show_multi():
    global result
    result += "*"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def back():
    global result
    result = result[:-1]
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def all_clear():
    global result
    result = "0"
    back()
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def total():
    global result
    t = eval(result)
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{t}")


def show4():
    global result
    result += "4"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show5():
    global result
    result += "5"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show6():
    global result
    result += "6"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show_sub():
    global result
    result += "-"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show1():
    global result
    result += "1"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show2():
    global result
    result += "2"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show3():
    global result
    result += "3"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show_add():
    global result
    result += "+"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show00():
    global result
    result += "00"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show0():
    global result
    result += "0"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show_point():
    global result
    result += "."
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


def show_modulo():
    global result
    result += "%"
    pygame.mixer.Sound.play(click_sound)
    result_label.config(text=f"{result}")


result_label = tk.Label(text="0", font=0, height=2, foreground="green")
result_label.grid(column=0, columnspan=50, row=0, sticky="e")

c_button = tk.Button(text="C", width=7, height=2, command=all_clear, foreground="blue")
c_button.grid(column=0, row=1)

m_button = tk.Button(text="%", width=7, height=2, command=show_modulo, foreground="blue")
m_button.grid(column=1, row=1)

b_button = tk.Button(text="🔙", width=7, height=2, command=back, foreground="blue")
b_button.grid(column=2, row=1)

button_division = tk.Button(text="/", width=7, height=2, command=show_divide, foreground="blue")
button_division.grid(column=3, row=1)

button7 = tk.Button(text="7", width=7, height=2, command=show7)
button7.grid(column=0, row=2)

button8 = tk.Button(text="8", width=7, height=2, command=show8)
button8.grid(column=1, row=2)

button9 = tk.Button(text="9", width=7, height=2, command=show9)
button9.grid(column=2, row=2)

button_multi = tk.Button(text="*", width=7, height=2, command=show_multi, foreground="blue")
button_multi.grid(column=3, row=2)

button4 = tk.Button(text="4", width=7, height=2, command=show4)
button4.grid(column=0, row=3)

button5 = tk.Button(text="5", width=7, height=2, command=show5)
button5.grid(column=1, row=3)

button6 = tk.Button(text="6", width=7, height=2, command=show6)
button6.grid(column=2, row=3)

button_sub = tk.Button(text="-", width=7, height=2, command=show_sub, foreground="blue")
button_sub.grid(column=3, row=3)

button1 = tk.Button(text="1", width=7, height=2, command=show1)
button1.grid(column=0, row=4)

button2 = tk.Button(text="2", width=7, height=2, command=show2)
button2.grid(column=1, row=4)

button3 = tk.Button(text="3", width=7, height=2, command=show3)
button3.grid(column=2, row=4)

button_add = tk.Button(text="+", width=7, height=2, command=show_add, foreground="blue")
button_add.grid(column=3, row=4)

button00 = tk.Button(text="00", width=7, height=2, command=show00)
button00.grid(column=0, row=5)

button0 = tk.Button(text="0", width=7, height=2, command=show0)
button0.grid(column=1, row=5)

button_point = tk.Button(text=".", width=7, height=2, command=show_point)
button_point.grid(column=2, row=5)


total_button = tk.Button(text="=", width=7, height=2, command=total, foreground="green")
total_button.grid(column=3, row=5)


window.mainloop()