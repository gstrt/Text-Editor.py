import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


def save_chosen_file():
    chosen_file = asksaveasfilename()
    file_input = file_text.get("1.0", 'end-1c')
    with open(chosen_file, 'w') as file:
        file.write(file_input)


def open_file():
    choose_file = askopenfilename()
    file_name_lbl = tk.Label(
        text=choose_file
    )

    with open(choose_file, 'r') as f:
        file_text.insert(1.0, f.read())

    file_name_lbl.pack()


main_window = tk.Tk()

save_button = tk.Button(
    text='Save',
    command=save_chosen_file
)

file_text = tk.Text()

quit_button = tk.Button(
    text='Quit',
    command=quit
)

open_button = tk.Button(
    text='Open',
    command=open_file
)
quit_button.pack()
file_text.pack()
open_button.pack()
save_button.pack()
main_window.mainloop()
