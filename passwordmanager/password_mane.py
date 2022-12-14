from tkinter import CENTER, Tk, Label, Button, Entry, Frame
from tkinter import  ttk
from db_operations import DbOperations


class root_window:

    def __init__(self, root, db):
        self.db = db
        self.root=root
        self.root.title("Password Manager")
        self.root.geometry("900x600+40+40")

        head_title = Label(self.root, text='Password Manager',width=40,
        bg="purple", font=("Ariel",20),padx=10,pady=10, justify=CENTER,
        anchor="center").grid(columnspan=4, padx=140,pady=20)

        self.crud_frame = Frame(self.root, highlightbackground="black",
        highlightthickness=1, padx=10, pady=30)
        self.crud_frame.grid()
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()

    def create_entry_labels(self):
        self.col_no, self.row_no = 0, 0
        labels_info = ('ID', 'Website', 'Username', 'Password')
        for label_info in labels_info:
            Label(self.crud_frame, text=label_info, bg='grey',
            fg='white', font=("Ariel",12), padx=5, pady=2).grid(row=self.row_no,
            column=self.col_no,padx=5, pady=2)
            self.col_no+=1

    def create_crud_buttons(self):
        self.row_no+=1
        self.col_no = 0
        buttons_info = (('Save', 'green', self.save_record), ('Update', 'blue', self.update_record),
        ('Delete', 'red', self.delete_record), ('Copy Password', 'violet', self.copy_record))
        for btn_info in buttons_info:
            Button(self.crud_frame, text=btn_info[0], bg=btn_info[1],
            fg='white', font=("Ariel",12), padx=2, pady=1, width=20, command = btn_info[2]).grid(row=self.row_no,
            column=self.col_no,padx=5, pady=10)
            self.col_no+=1


        
    def create_entry_boxes(self):
        self.row_no+=1
        self.entry_boxes = []
        self.col_no = 0
        for i in range(4):
            show=""
            if i == 3 :
                show = "*"
            entry_box = Entry(self.crud_frame, width=20, background='lightgrey',
            font = ("Ariel", 12), show = show)
            entry_box.grid(row=self.row_no, column=self.col_no,padx=5,pady=2)
            self.col_no+=1
            self.entry_boxes.append(entry_box)


    #CRUD FUNCTIONS
    def save_record(self):
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()

        data = {'website': website, "username": username, "password": password}
        self.db.create_record(data)


    def update_record(self):
        pass
    
    def delete_record(self):
        pass
    
    def show_records(self):
        record_list = self.db.show_record()
        for record in record_list:
            print(record)


    #copies directly to the clipboard
    def copy_record(self):
        pass


if __name__=="__main__":
    #create table if doesn't exists
    db_class = DbOperations()
    db_class.create_table()

    #create tkinter window
    root=Tk()
    root_class=root_window(root, db_class)
    root.mainloop()