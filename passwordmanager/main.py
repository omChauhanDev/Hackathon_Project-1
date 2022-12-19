from tkinter import CENTER, Tk, Label, Button, Entry, Frame, END, Toplevel
from tkinter import  ttk
from db_operations import DbOperations



# Creating a class for the main window
class root_window:

    def __init__(self, root, db):
        self.db = db
        self.root=root
        self.root.title("Password Manager")
        self.root.geometry("1520x780+0+0")

         # Labels mean the text that is displayed on the screen.

        '''padx adds spaces on the x-axis from both the sides. pady similarly adds spaces on the y-axis grid 
        organizes the widgets in a table-like structure. Basically, it is used to place the widgets at the specified 
        row and column '''

        head_title = Label(self.root, text='PASSWORD  MANAGER',width=80,
        bg="cyan", font=("Arial Rounded MT Bold",20),padx=10,pady=10, justify=CENTER,
        anchor="center").grid(columnspan=4, padx=0,pady=50)

        '''
        We are creating a frame for crud operations. CRUD stands for Create, Read, Update, Delete.
        These are the basic functions of a database. We will create a frame for these operations.
        Then we will create buttons and entry boxes for these operations.
        The reason we will create a frame for these operations is because we want to keep them in a separate frame
        '''

        '''self.main is the name of our window. We are creating a frame inside the window and then we're making 
        borders for the frame. 
        Calling all the main components of the application in the init function.'''

        self.crud_frame = Frame(self.root, highlightbackground="brown",
        highlightthickness=5, padx=10, pady=40)
        self.crud_frame.grid(columnspan=1,padx=1,pady=15)

        # calling the functions to create the labels, buttons, and entry boxes
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()
        
        # creating the view(called tree view) for the records
        self.create_records_tree()
    
    # creating labels for the entry boxes. Labels are basically the text that is displayed on the screen
    def create_entry_labels(self):
        self.col_no, self.row_no = 0, 0
        labels_info = ('ID', 'Website', 'Username', 'Password')

        # iterating over the labels
        for label_info in labels_info:
            # creating a label in the frame
            Label(self.crud_frame, text=label_info, bg='black',
            fg='white', font=("Ariel",14), padx=5, pady=2).grid(row=self.row_no,
            column=self.col_no,padx=5, pady=3)
            # incrementing the column number to place the button in the same row
            self.col_no+=1
    
    # creating buttons for the crud operations
    def create_crud_buttons(self):
        self.row_no+=1
        self.col_no = 0
        # Buttons are created by giving them the function that they will perform when clicked
        buttons_info = (('Save', 'dark green', self.save_record), ('Update', 'navy', self.update_record),
        ('Delete', 'violet red', self.delete_record), ('Copy Password', 'salmon', self.copy_record), ("Show All Records", "medium orchid",
        self.show_records))
        # iterating over the buttons
        for btn_info in buttons_info:
            if btn_info[0] == "Show All Records":
                # incrementing the row number to place the upcoming button(s) in the next row
                self.row_no += 1
                self.col_no = 0
            '''creating the button by assigning the location i.e the crud frame and 
            giving it the text, background color, font, width, and the function that it will perform'''
            Button(self.crud_frame, text=btn_info[0], bg=btn_info[1],
            fg='white', font=("Ariel",14), padx=2, pady=1, width=20, command = btn_info[2]).grid(row=self.row_no,
            column=self.col_no,padx=30, pady=15)
            self.col_no+=1


    # creating entry boxes for the crud operations 
    def create_entry_boxes(self):
        self.row_no+=1
        # list to store the entry boxes
        self.entry_boxes = []
        self.col_no = 0
         # creating 4 entry boxes
        for i in range(4):
            show=""
            # Hiding the password with asterisks
            if i == 3 :
                show = "*"  
            entry_box = Entry(self.crud_frame, width=20, background='lightgrey',
            font = ("Ariel", 14), show = show)
            # placing the entry box in the grid
            entry_box.grid(row=self.row_no, column=self.col_no,padx=10,pady=10)
            self.col_no+=1
             # appending the entry box to the list
            self.entry_boxes.append(entry_box)


    # CRUD/Database FUNCTIONS
    def save_record(self):
        # Fetching the data from the entry boxes
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()

        # Inserting the data into the database
        data = {'website': website, "username": username, "password": password}
        self.db.create_record(data)
        # Showing the records in the tree view
        self.show_records()


    def update_record(self):
        # Fetching the data from the entry boxes
        ID = self.entry_boxes[0].get()
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()

        # Updating the data in the database
        data = {'ID': ID, 'website': website, "username": username, "password": password}
        self.db.update_record(data)
        # Showing the updated records
        self.show_records()
    
    def delete_record(self):
        # Fetching the data from the entry boxes
        ID = self.entry_boxes[0].get()
        # Deleting the data from the database
        self.db.delete_record(ID)
        # Showing the updated records
        self.show_records()
    
    def show_records(self):
        # Returns a tuple of all the children(entries) of the parent
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        # Fetching the records from the database
        record_list = self.db.show_record()
        for record in record_list:
            # Inserting the records into the tree view
            self.records_tree.insert("", END, values = (record[0], record[3], record[4], record[5]))

    
    def create_records_tree(self):
        columns = ("ID", "Website", "Username", "Password")
        # creating the tree view from the ttk module
        self.records_tree = ttk.Treeview(self.root, columns = columns, show = 'headings')
        self.records_tree.heading("ID", text = "ID")
        self.records_tree.heading("Website", text = "Website Name")
        self.records_tree.heading("Username", text = "Username")
        self.records_tree.heading("Password", text = "Password")
        # website and username are the fields that will be displayed
        self.records_tree['displaycolumns'] = ("Website", "Username")

        # placing the tree view in the grid
        def item_selected(event):
            for selected_item in self.records_tree.selection():
                item = self.records_tree.item(selected_item)
                record = item['values']
                for entry_box, item in zip(self.entry_boxes, record):
                    entry_box.delete(0, END)
                    entry_box.insert(0, item)   

        # binding the tree view with the function
        self.records_tree.bind("<<TreeviewSelect>>", item_selected)

        self.records_tree.grid(padx=560)


    #copies directly to the clipboard
    def copy_record(self):
        # clearing the clipboard
        self.root.clipboard_clear()
        # appending the password to the clipboard
        self.root.clipboard_append(self.entry_boxes[3].get())
        message = "Password Copied To Clipboard"
        title = "Copy"
        if self.entry_boxes[3].get() == "":
            message = 'Entry Box is Empty'
            title = "Error"
        # showing the message after copying the password
        self.showmessage(title, message)

    # title and message are passed when function is called
    def showmessage(self, title_box:str=None, message:str=None):
        TIME_TO_WAIT = 900 #in ms
        # creating a new window
        root = Toplevel(self.root)
        background = "green"
        if title_box == "Error":
           background = "red"
        
        # setting the size of the window
        root.geometry('300x30+760+415')
        root.title(title_box)
        Label(root, text = message, background = background, font = ("Ariel", 15), fg = "white").pack(padx = 4, pady = 2)
                
        # after the time specified, the window will be destroyed/closed
        try:
            root.after(TIME_TO_WAIT, root.destroy)
        except Exception as e:
            print("Error occured", e)

if __name__=="__main__":
    #create table if doesn't exists
    db_class = DbOperations()
    db_class.create_table()

    #create tkinter window
    # Initializing the tkinter window with the title bar
    root=Tk()
    # creating the object of the root window class
    root_class=root_window(root, db_class)

    root.mainloop()
    '''mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event 
    as long as the window is not closed. '''
