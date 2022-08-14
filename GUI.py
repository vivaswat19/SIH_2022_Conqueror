
from ast import main
import tkinter as tk
from turtle import onclick
main_window = tk.Tk()
main_window.geometry("2560x1600")

# main_window.attributes('-fullscreen',True)

def clear_page():
    for widget in main_window.winfo_children():
        widget.destroy()

def page_1(main_window):
    aquifer_hydrolic_conductivity_label = tk.Label(main_window,text = "Aquifer Hydrolic Conductivity").place(x = 40,y = 60)
    aquifer_hydrolic_conductivity_input = tk.Text(main_window,height = 1, width = 6).place(x=100, y=60)
    button = tk.Button(main_window, text="click", command=clear_page).place(x=100,y=200)



page_1(main_window=main_window)
main_window.mainloop()