from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter_nav.page import Page

from utils.students_utils import getStudentById
from utils.request_utils import createRequest
from views.profile_image import ProfileImage

deps = ['CSE', 'ECE', 'EEE', 'CIVIL', 'MECH']

class StudentHomePage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'StudentHomePage')
        self.configure(background='white')

    def page_did_mount(self):
        self.user_id = self.app_state['user_id']
        if self.user_id == -1:
            return
        self.details = getStudentById(self.user_id)
        self.new_details = self.details
        print('student_details', self.details)
        
        self.profile_pic = StringVar(self, self.details['profile_pic'])
        self.first_name = StringVar(self, self.details['first_name'])
        self.last_name = StringVar(self, self.details['last_name'])
        self.address = StringVar(self, self.details['address'])
        self.phone = StringVar(self, self.details['phone'])
        self.email = StringVar(self, self.details['email'])
        self.department = StringVar(self, self.details['department'])
        self.cgpa = StringVar(self, self.details['cgpa'])
        self.heading_var = StringVar(self, "Students Details")

        self.items = [
            ("Your first name", self.first_name),
            ("Your last name",  self.last_name),
            ("Your address",    self.address),
            ("Your phone",      self.phone),
            ("Your email",      self.email),
            ("Your department", self.department),
            ("Your CGPA",       self.cgpa)
        ]

        self.view_rows = [[None, None] for i in range(len(self.items))]

        # design

        left_frame = Frame(self, background="white")
        right_frame = Frame(self, background="white")

        # left frame code
        photoImage = ProfileImage(self, self.details['profile_pic'], 200)
        self.profileImage = Label(
            left_frame, image=photoImage, bd=0, background='#fff')
        self.profileImage.image = photoImage
        self.profileImage.pack()

        self.select_dp_btn = Button(
            left_frame,
            text="Select Profile Picture",
            relief="solid",
            font='Helvetica 12', command=self.update_profile_pic
        )

        # right frame code
        Label(
            right_frame,
            textvariable=self.heading_var,
            font='Helvetica 18 underline',
            background="white"
        ).grid(row=0, column=0, pady=4, padx=2)

        for i, x in enumerate(self.items):
            label, strvar = x
            Label(
                right_frame,
                relief="flat",
                text=label,
                bg='#fff',
                font='16'
            ).grid(row=i+1, column=0, pady=4, padx=2, sticky='w')
            Label(
                right_frame,
                relief="flat",
                text=' : ',
                bg='#fff',
                font='16'
            ).grid(row=i+1, column=1, pady=4, padx=2)
            self.view_rows[i][0] = Label(
                right_frame,
                relief="flat",
                text=strvar.get(),
                bg='#fff',
                font='16'
            )
            self.view_rows[i][0].grid(
                row=i+1, column=2, pady=4, padx=2, sticky='w')
            if "department" in label:
                self.view_rows[i][1] = OptionMenu(
                    right_frame,
                    strvar,
                    *deps,
                )
                self.view_rows[i][1]['font'] = "1",
                self.view_rows[i][1]['bd'] = 1,
                self.view_rows[i][1]['relief'] = "solid"
            else:
                self.view_rows[i][1] = Entry(
                    right_frame,
                    textvariable=strvar,
                    relief="solid",
                    bg="#eeeeee", font='3',
                )
        
        self.button = Button(
            right_frame,
            text="EDIT",
            relief=FLAT,
            bg='#1565c0', fg="white",
            font='Helvetica 11',
            command=self.edit_click
        )
        self.button.grid(row=9, column=1, ipadx=4, ipady=2, pady=16)

        Button(
            right_frame,
            text="LOG OUT",
            relief=FLAT,
            bg='#1565c0', fg="white",
            font='Helvetica 11',
            command=self.log_out
        ).grid(row=9, column=2, ipadx=4, ipady=2, pady=16)

        # placing
        left_frame.grid(row=0, column=0,  padx=4, pady=4, ipadx=8, ipady=8)
        right_frame.grid(row=0, column=1,  padx=4, pady=4, ipadx=8, ipady=8)
        right_frame.grid_columnconfigure(0, weight=3)
        right_frame.grid_columnconfigure(1, weight=7)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=0)

    # methods

    def update_profile_pic(self):
        file_path = askopenfilename()
        self.profile_pic.set(file_path)
        photoImg = ProfileImage(self, file_path, 200)
        self.profileImage.configure(image=photoImg)
        self.profileImage.image = photoImg
    
    def update_details(self):
        self.new_details['profile_pic'] = self.profile_pic.get().strip()
        self.new_details['first_name'] = self.first_name.get().strip()
        self.new_details['last_name'] = self.last_name.get().strip()
        self.new_details['address'] = self.address.get().strip()
        self.new_details['phone'] = self.phone.get().strip()
        self.new_details['email'] = self.email.get().strip()
        self.new_details['department'] = self.department.get().strip()
        self.new_details['cgpa'] = self.cgpa.get().strip()

        success, err = createRequest(self.new_details)
        if not success:
            messagebox.showerror("Invalid details", err)
        else:
            messagebox.showinfo("Successfully requested",
                                "Your changes has been submitted to admin")
            self.button.config(command=self.edit_click, text="Edit")
            self.heading_var.set("Students Details (old data)")


    def update_click(self):
        print('update_click')
        self.update_details()
        self.select_dp_btn.pack_forget()
        self.profileImage.pack_forget()
        for i in range(len(self.items)):
            self.view_rows[i][0].grid(
                row=i+1, column=2, pady=4, padx=2, sticky='w')
            self.view_rows[i][1].grid_forget()

    def edit_click(self):
        print('edit_click')
        self.select_dp_btn.pack(pady=20)
        for i in range(len(self.items)):
            self.view_rows[i][0].grid_forget()
            if "department" in self.items[i][0]:
                self.view_rows[i][1].grid(row=i+1, column=2,
                                          padx=4, pady=4, sticky="we")
            else:
                self.view_rows[i][1].grid(row=i+1, column=2, padx=4, pady=4)
        self.button.config(command=self.update_click, text="Update")

    def log_out(self):
        self.app_state['user_id'] = -1
        self.update_state()
        self.navigate('WelcomePage')
