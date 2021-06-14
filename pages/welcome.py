from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from utils.students_utils import login_student

from tkinter_nav import Page


class WelcomePage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'WelcomePage')
        self.configure(background='white')
        self.admin_click_count = 0

        left_frame = Frame(self, background="white")
        right_frame = Frame(self, background="white")

        self.user_email = StringVar(self)
        self.user_password = StringVar(self)

        # left frame code
        logo_image = PhotoImage(file=self.app_state['college_logo'])
        image_element = Label(left_frame, image=logo_image, bd=0)
        image_element.photo = logo_image
        image_element.pack()
        Label(left_frame, text=self.app_state['college_name'], font="Helvetica 18",
              bd=0, bg='white').pack(pady=20)

        image_element.bind("<Button-1>", self.show_admin)

        # right frame code

        Label(
            right_frame,
            text="LOGIN TO YOUR ACCOUNT",
            font='Helvetica 18 underline',
            bg='#fff',
        ).pack(pady=20)
        email_label = Label(
            right_frame,
            text="Enter your email",
            bg='#fff', font=('4')
        )

        email_entry = Entry(
            right_frame,
            textvariable=self.user_email,
            relief="solid",
            bg="#eeeeee", font='3',
        )
        password_label = Label(
            right_frame,
            text="Enter your password",
            bg='#fff', font=('4')
        )

        password_entry = Entry(
            right_frame,
            textvariable=self.user_password,
            relief="solid",
            bg="#eeeeee", font='3',
            show='*'
        )

        login_button = Button(
            right_frame,
            text="LOGIN",
            relief="flat",
            bg='#1565c0', fg="white",
            font='Helvetica 10',
            command=self.login_btn_click
        )

        reset_button = Button(
            right_frame,
            text="Forget Password? Reset",
            fg="#1565c0", bg="white",
            bd=0,
            relief=FLAT,
            font='Helvetica 11 underline',
            command=lambda: self.navigate('PasswordResetPage')
        )

        register_button = Button(
            right_frame,
            text="New User? Register here",
            fg="#1565c0", bg="white",
            bd=0,
            relief=FLAT,
            font='Helvetica 11 underline',
            command=lambda: self.navigate('RegisterPage')
        )

        email_label.pack(pady=2)
        email_entry.pack(pady=8, padx=4, ipadx=4, ipady=4, fill=X)
        password_label.pack(pady=2)
        password_entry.pack(pady=8, padx=4, ipadx=4, ipady=4, fill=X)

        login_button.pack(ipadx=4, ipady=2, pady=16)
        reset_button.pack(ipadx=8, ipady=4, pady=4)
        register_button.pack(ipadx=8, ipady=4, pady=4)

        # griding
        left_frame.grid(row=0, column=0)
        right_frame.grid(row=0, column=1)

        # placing
        self.grid_rowconfigure(0, weight=7)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=7)

    def login_btn_click(self):
        email = self.user_email.get().strip()
        password = self.user_password.get().strip()
        user_id, err = login_student(email, password)
        if type(user_id) != int:
            messagebox.showerror(
                'Login Failed', err)
        else:
            messagebox.showinfo(
                'Login Success', "You are successfully logged in!!!")
            self.app_state['user_id'] = int(user_id)
            self.update_state()
            self.navigate('StudentHomePage')

    def show_admin(self, event):
        self.admin_click_count += 1
        if self.admin_click_count == 2:
            self.admin_click_count = 0
            admin_password = simpledialog.askstring(
                title="Admin Verification",
                prompt="Enter the admin password:"
            )
            if admin_password == 'nopassword':
                self.navigate('AdminHomePage')
            else:
                messagebox.showerror(
                    "Wrong password", "You have entered wrong password.. ")

    def page_did_unmount(self):
        self.user_email.set('')
        self.user_password.set('')
