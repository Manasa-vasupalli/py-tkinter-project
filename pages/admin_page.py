from tkinter import *
from tkinter import ttk

from tkinter_nav.page import Page
from utils.students_utils import getStudents


class AdminHomePage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'AdminHomePage')
        self.configure(background='white')

    def page_did_mount(self):
        left_frame = Frame(self, background="white")
        right_frame = Frame(self, background="white")

        # left frame code
        logo_image = PhotoImage(file=self.app_state['college_logo'])
        image_element = Label(left_frame, image=logo_image, bd=0)
        image_element.photo = logo_image
        image_element.pack()
        Label(left_frame, text="Raghu Institute Of Technology\n(Autonomous)", font="Helvetica 18",
              bd=0, bg='white').pack(pady=20)
        Label(left_frame, text="Admin Page", font="Helvetica 20",
              bd=0, bg='white').pack(pady=20)

        left_frame.grid(row=0, column=0)
        right_frame.grid(row=0, column=1)
        Label(right_frame, text="Students list", font="Helvetica 16 underline",
              bd=0, bg='white').grid(row=0, column=0, pady=8)

        treeView = ttk.Treeview(right_frame)
        treeView["columns"] = [
            'id',
            'name',
            'address',
            'phone',
            'email',
            'department',
            'cgpa',
        ]
        treeView.heading("id", text="Student ID")
        treeView.heading("name", text="Student Name")
        treeView["show"] = "headings"

        vsb = ttk.Scrollbar(right_frame, orient="vertical",
                            command=treeView.yview)
        treeView.configure(yscrollcommand=vsb.set)

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda:
                       treeview_sort_column(tv, col, not reverse))

        for col in treeView['columns']:
            treeView.heading(col, text=f"{col.upper()}", anchor=CENTER, command=lambda _col=col:
                             treeview_sort_column(treeView, _col, False))
            # initially smaller size
            treeView.column(col, anchor=CENTER, width=40)
        treeView.update()
        for col in treeView['columns']:
            treeView.column(col, width=100)

        students = getStudents()
        for i, student in enumerate(students):
            s_id = i
            s_name = student['first_name'] + ' ' + student['last_name']
            s_address = student['address']
            s_phone = student['phone']
            s_email = student['email']
            s_department = student['department']
            s_cgpa = student['cgpa']
            data = (str(s_id), s_name, s_address,
                    s_phone,
                    s_email,
                    s_department,
                    s_cgpa)
            treeView.insert("", i+1, s_id, values=data)

        if len(students) != 0:
            treeView.grid(row=1, column=0, sticky='nesw')
            vsb.grid(row=1, column=1, sticky='ns')
        else:
            Label(right_frame, text="No students for now", bg="#fff").grid()

        Button(right_frame, text="Update Requests",
               relief="flat",
               bg='#1565c0', fg="white",
               command=lambda: self.navigate('AllRequestsPage'),
               font='Helvetica 10',).grid(ipadx=4, ipady=2, pady=16)

        Button(right_frame, text="Log Out",
               relief="flat",
               bg='#1565c0', fg="white",
               command=lambda: self.navigate('WelcomePage'),
               font='Helvetica 10',).grid(ipadx=4, ipady=2, pady=16)

        # placing
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        return super().page_did_mount()
