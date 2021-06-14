from views.profile_image import ProfileImage
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.font import Font

from tkinter_nav.page import Page
from utils.students_utils import register_student

deps = ['CSE', 'ECE', 'EEE', 'CIVIL', 'MECH']


class RegisterPage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'RegisterPage')
        self.configure(background='white')
        left_frame = Frame(self, background="white")
        right_frame = Frame(self, background="white")
        logo_image = PhotoImage(file=self.app_state['college_logo'])
        image_element = Label(left_frame, image=logo_image, bd=0)
        image_element.photo = logo_image
        image_element.pack()
        Label(left_frame, text=self.app_state['college_name'], font="Helvetica 18",
              bd=0, bg='white').pack(pady=20)

        # right frame code

        Label(
            right_frame,
            text="REGISTER YOUR DETAILS",
            font='Helvetica 18 underline',
            bg='#fff',
        ).grid(row=0, column=0, columnspan=2, padx=4, pady=16)

        photoImg = ProfileImage(
            self, self.app_state['sample_user_dp'], 50, False)
        self.profileImage = Label(
            right_frame, image=photoImg, bd=0, background='white')
        self.profileImage.image = photoImg
        self.profileImage.grid(row=1, column=0, padx=4, pady=4)

        Button(
            right_frame,
            text="Select Profile Picture",
            relief="solid",
            font='Helvetica 12',
            command=self.update_profile_pic
        ).grid(row=1, column=1, padx=4, pady=4)

        right_frame.grid_rowconfigure(1, weight=0)

        # string variables declaration
        self.profile_pic = StringVar(right_frame)
        self.first_name = StringVar(right_frame)
        self.last_name = StringVar(right_frame)
        self.address = None
        self.phone = StringVar(right_frame)
        self.email = StringVar(right_frame)
        self.password = StringVar(right_frame)
        self.confirm_password = StringVar(right_frame)
        self.department = StringVar(right_frame, deps[0])
        self.cgpa = StringVar(right_frame)

        items = [
            #        LABEL:            Dep.   SHOW*  1line  StringVar
            ("Enter your first name",  False, False, True,  self.first_name),
            ("Enter your last name",   False, False, True,  self.last_name),
            ("Enter your address",     False, False, False, self.address),
            ("Enter your phone",       False, False, True,  self.phone),
            ("Enter your email",       False, False, True,  self.email),
            ("Enter your password",    False, True,  True,  self.password),
            ("Confirm your password",  False, True,  True,  self.confirm_password),
            ("Enter your departement", True,  False, True,  self.department),
            ("Enter your CGPA",        False, False, True,  self.cgpa)
        ]

        # accessing data
        for i, item in enumerate(items):
            label, is_dep, is_pass, is_entry, strvar = item
            Label(right_frame, text=label, bg='#fff', font='4').grid(
                row=i+2, column=0,
                pady=4, padx=2,
                sticky='w' if is_entry else 'nw'
            )
            if is_dep:
                menu = OptionMenu(right_frame, strvar, *deps)
                menu["bd"] = 1
                menu["relief"] = "solid"
                menu.grid(row=i+2, column=1, padx=10, pady=4, sticky="we")
            elif is_entry:
                Entry(
                    right_frame,
                    textvariable=strvar,
                    relief="solid",
                    bg="#eeeeee", font='3',
                    show='*' if is_pass else ''
                ).grid(row=i+2, column=1, padx=4, pady=4)
            else:
                self.address = Text(
                    right_frame,
                    relief="solid",
                    bg="#eeeeee", font='3',
                    height=2,
                    width=20
                )
                self.address.grid(row=i+2, column=1, padx=4, pady=4)

            right_frame.grid_rowconfigure(i+2, weight=0)

        register_button = Button(
            right_frame,
            text="Register",
            relief="flat",
            bg='#1565c0', fg="white",
            font='Helvetica 12',
            command=self.register_btn_click
        )

        login_button = Button(
            right_frame,
            text="Already User? Login here",
            fg="#1565c0", bg="white",
            bd=0,
            relief=FLAT,
            command=lambda: self.navigate('WelcomePage'),
            font=Font(name='Helvetica', size=12, underline=True),
        )
        next_row = len(items)+2
        register_button.grid(row=next_row+1, column=1, padx=4,
                             ipadx=4, ipady=2, pady=16)
        login_button.grid(row=next_row+2, column=1, pady=4, padx=4)

        left_frame.grid(row=0, column=0,  padx=4, pady=4, ipadx=8, ipady=8)
        right_frame.grid(row=0, column=1,  padx=4, pady=4, ipadx=8, ipady=8)

        # placing

        right_frame.grid_columnconfigure(0, weight=3)
        right_frame.grid_columnconfigure(1, weight=7)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # methods
    def update_profile_pic(self):
        file_path = askopenfilename()
        self.profile_pic.set(file_path)
        photoImg = ProfileImage(self, file_path, 50)
        self.profileImage.configure(image=photoImg)
        self.profileImage.image = photoImg

    def register_btn_click(self):
        user_data = {
            'profile_pic': self.profile_pic.get(),
            'first_name': self.first_name.get().strip(),
            'last_name': self.last_name.get().strip(),
            'address': self.address.get("1.0", END).strip(),
            'phone': self.phone.get().strip(),
            'email': self.email.get().strip(),
            'password': self.password.get().strip(),
            'confirm_password': self.confirm_password.get().strip(),
            'department': self.department.get().strip(),
            'cgpa': self.cgpa.get().strip(),
        }
        success, err = register_student(user_data)
        if not success:  # error box
            messagebox.showerror("Changes needed whatevber", err)
        else:  # store user details!
            messagebox.showinfo("Registration Successful!",
                                "Your details are registered ")
            self.navigate('WelcomePage')

    def page_did_unmount(self):
        self.profile_pic.set('')
        self.first_name.set('')
        self.last_name.set('')
        self.address.delete('1.0', END)
        self.phone.set('')
        self.email.set('')
        self.password.set('')
        self.confirm_password.set('')
        self.department.set('')
        self.cgpa.set('')
        return super().page_did_unmount()
