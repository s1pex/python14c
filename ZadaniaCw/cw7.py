import tkinter as tk
from screeninfo import get_monitors
root = tk.Tk()


root.title("Book Store")
#root.geometry("800x600")
root.iconbitmap("./bookshelf.ico")
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height

left_frame = tk.Frame(root, borderwidth = 4, relief = "ridge", width = screen_width/12, height = screen_height/5)
left_frame.pack(side = "left", padx = 3, pady = 3)
left_frame.pack_propagate(0)

right_frame = tk.Frame(root, borderwidth = 4, relief = "ridge", width = screen_width/5, height = screen_height/5)
right_frame.pack(side = "right", padx = 3, pady = 3)
right_frame.pack_propagate(0)
label = tk.Label(right_frame, text = "Podaj imię i nazwisko")
label.pack()

entry = tk.Entry(left_frame)
entry.pack(anchor = "w", padx = 5, pady = 5)

def change_text():
    e = entry.get()
    praca = radio_var.get()
    lang = ""


    for i in range(0, len(lista1)):
        if lista1[i].get() == 1:
            lang += listaCheck[i].cget("text")

    label.config(text = e + " " + praca + " " + lang)

radio_var = tk.StringVar(value=" ")
radioButton = tk.Radiobutton(left_frame, text = "Tester", value = "Tester", variable=radio_var)
radioButton.pack(anchor="w", padx= 5, pady= 5)
radioButton1 = tk.Radiobutton(left_frame, text = "Programista", value = "Programista", variable= radio_var)
radioButton1.pack(anchor="w", padx= 5, pady= 5)

lista1 = []
listaCheck = []
lista1.append(tk.IntVar())
checkButton = tk.Checkbutton(left_frame, text = "java", variable=lista1)
checkButton.pack(anchor="w", padx = 5, pady=5)
lista1.append(tk.IntVar())
checkButton1 = tk.Checkbutton(left_frame, text = "python", variable=lista1)
checkButton1.pack(anchor="w", padx = 5, pady=5)
listaCheck.append(checkButton1)
listaCheck.append(checkButton)

button = tk.Button(left_frame, text = "Ok", command = change_text)
button.pack(anchor="w", padx=5, pady=5)

root.mainloop()