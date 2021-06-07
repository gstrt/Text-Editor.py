import tkinter as tk
from tkinter.filedialog import askopenfilename

globalFile = None


def choose_file():
    filename = askopenfilename()
    with open(filename, 'w') as file:
        chosen_file = file.write('file')
        file_path_lbl = tk.Label(
            text=filename
        )

        file_path_lbl.pack()
        globalFile = chosen_file


def save():
    text_to_write = file_text.get(1.0, tk.END)
    globalFile.write(text_to_write)


main_window = tk.Tk()

open_button = tk.Button(
    text='Open',
    command=choose_file
)

file_text = tk.Text()

quit_button = tk.Button(
    text='Quit',
    command=quit
)

save_button = tk.Button(
    text='Save',
    command=save
)
quit_button.pack()
file_text.pack()
open_button.pack()
save_button.pack()
main_window.mainloop()
