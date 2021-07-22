import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class Editor:

    def __init__(self):
        self.main_window = tk.Tk()
        self.save_button = tk.Button(
            text='Save',
            command=self.save_chosen_file
        )
        self.file_text = tk.Text()
        self.file_name_lbl = tk.Label()
        self.quit_button = tk.Button(
            text='Quit',
            command=quit
        )
        self.open_button = tk.Button(
            text='Open',
            command=self.open_file
        )

    def save_chosen_file(self):
        chosen_file = asksaveasfilename()
        file_input = self.file_text.get("1.0", 'end-1c')
        with open(chosen_file, 'w') as file:
            file.write(file_input)

    def open_file(self):
        choose_file = askopenfilename()
        self.file_name_lbl.config(text=choose_file)

        self.file_text.delete("1.0", "end-1c")

        with open(choose_file, 'r') as f:
            self.file_text.insert(1.0, f.read())

    def draw(self):
        self.quit_button.pack()
        self.file_text.pack()
        self.open_button.pack()
        self.save_button.pack()
        self.file_name_lbl.pack()
        self.main_window.mainloop()


if __name__ == "__main__":
    editor = Editor()
    editor.draw()

