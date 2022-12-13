from tkinter import Tk, Label, Button, Entry
from tkinter import  ttk


class root_window:

    def __init__(self, root):
        self.root=root
        self.root.title("Password Manager")
        self.root.geometry("900x600+40+40")

        head_title = Label(self.root, text='Password Manager',width=40,
        bg="purple", font=("Ariel",20),padx=10,pady=10, justify="center",anchor="center").grid(columnspan=4, padx=140,pady=10)

        crud_frame=ttk.Frame(self.root)
        crud_frame.grid()

        entry_boxes = []
        row_no = col_no = 0
        for i in range(4):
            entry_box = Entry(crud_frame, width=30, background='lightgrey')
            entry_box.grid(row=row_no, column=col_no,padx=5,pady=2)
            col_no+=1



if __name__=="__main__":
    root=Tk()
    root_class=root_window(root)
    root.mainloop()
