from tkinter import *
from tkinter import ttk

from tkinter_nav.page import Page
from utils.request_utils import getRequests


class AllRequestsPage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'AllRequestsPage')
        self.configure(background='white')

    def page_did_mount(self):
        left_frame = Frame(self, background="white")
        right_frame = Frame(self, background="white")

        # left frame code
        logo_image = PhotoImage(file=self.app_state['college_logo'])
        image_element = Label(left_frame, image=logo_image, bd=0)
        image_element.photo = logo_image
        image_element.pack()
        Label(left_frame, text=self.app_state['college_name'], font="Helvetica 18",
              bd=0, bg='white').pack(pady=20)

        left_frame.grid(row=0, column=0)
        right_frame.grid(row=0, column=1)

        self.treeView = ttk.Treeview(right_frame)
        self.treeView["columns"] = ["s_id", "s_name"]
        self.treeView.heading("s_id", text="Student ID")
        self.treeView.heading("s_name", text="Student Name")
        self.treeView["show"] = "headings"
        self.treeView.bind('<ButtonRelease-1>', self.selectItem)

        requests = getRequests()
        print(requests,len(requests))
        for i, request in enumerate(requests):
            s_id = request['id']
            s_name = request['first_name'] + ' ' + request['last_name']
            self.treeView.insert("", i+1, s_id, values=(str(s_id), s_name))

        self.treeView.grid()
        if len(requests) == 0:
            self.treeView.grid_forget()
            Label(right_frame, text="No requests for now", bg="#fff").grid()

        self.btn = Button(right_frame, text="Go Back to Admin Page",
               relief="flat",
               bg='#1565c0', fg="white",
               font='Helvetica 10',
               command=lambda: self.navigate('AdminHomePage')
        )
        self.btn.grid(ipadx=4, ipady=2, pady=16)

        # placing
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        return super().page_did_mount()

    def selectItem(self, event):
        curItem = self.treeView.item(self.treeView.focus())
        id = curItem['values'][0]
        print('id = ', id)
        self.app_state['review_id'] = int(id)
        self.update_state()
        self.navigate('ReviewChangesPage')
    
    def page_did_unmount(self):
        self.treeView.grid_forget()
        self.btn.grid_forget()
        return super().page_did_unmount()
