from tkinter import *
from tkinter import messagebox

from tkinter_nav.page import Page
from utils.validators import is_valid_password
from utils.otp_utils import send_otp_to_phone
from utils.students_utils import check_student_exists, getStudentByEmail, password_reset


class PasswordResetPage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'PasswordResetPage')
        self.configure(background='white')

        self.real_phone = ''  # StringVar(self)
        self.email = StringVar(self)
        self.otp = StringVar(self)
        self.password = StringVar(self)
        self.confirm_password = StringVar(self)

        left_frame = Frame(self, background="white")
        right_frame = Frame(self, background="white")

        # left frame code
        logo_image = PhotoImage(file=self.app_state['college_logo'])
        image_element = Label(left_frame, image=logo_image, bd=0)
        image_element.photo = logo_image
        image_element.pack()
        Label(left_frame, text=self.app_state['college_name'], font="Helvetica 18",
              bd=0, bg='white').pack(pady=20)
        # right frame code
        self.email_frame = Frame(right_frame, background="white")
        self.otp_frame = Frame(right_frame, background="white")
        self.password_reset_frame = Frame(right_frame, background="white")

        Label(
            right_frame,
            text="RESET PASSWORD",
            font='Helvetica 18 underline',
            bg='#fff',
        ).pack(pady=20)

        email_label = Label(
            self.email_frame,
            text="Enter your email",
            bg='#fff', font=('4')
        )

        email_entry = Entry(
            self.email_frame,
            textvariable=self.email,
            relief="solid",
            bg="#eeeeee", font='3',
        )

        send_otp_button = Button(
            self.email_frame,
            text="Send OTP",
            relief="flat",
            bg='#1565c0', fg="white",
            font='Helvetica 10',
            command=self.send_otp_click
        )

        Label(
            self.otp_frame,
            text=f"An OTP is sent to your phone number",
            bg="#fff"
        ).pack()

        otp_label = Label(
            self.otp_frame,
            text="Enter the OTP",
            bg='#fff', font=('4')
        )

        otp_entry = Entry(
            self.otp_frame,
            textvariable=self.otp,
            relief="solid",
            bg="#eeeeee", font='3',
            justify='center'
        )

        verify_otp_button = Button(
            self.otp_frame,
            text="Verify OTP",
            relief="flat",
            bg='#1565c0', fg="white",
            font='Helvetica 10',
            command=self.verify_otp_click
        )

        password_label = Label(
            self.password_reset_frame,
            text="Enter your new password",
            bg='#fff', font=('4')
        )

        password_entry = Entry(
            self.password_reset_frame,
            textvariable=self.password,
            relief="solid",
            bg="#eeeeee", font='3',
            show='*'
        )

        confim_password_label = Label(
            self.password_reset_frame,
            text="Confirm your new password",
            bg='#fff', font=('4')
        )

        confim_password_entry = Entry(
            self.password_reset_frame,
            textvariable=self.confirm_password,
            relief="solid",
            bg="#eeeeee", font='3',
            show='*'
        )

        reset_button = Button(
            self.password_reset_frame,
            text="Update password",
            relief="flat",
            bg='#1565c0', fg="white",
            font='Helvetica 10',
            command=self.update_password_click
        )

        email_label.pack(pady=2)
        email_entry.pack(pady=8, padx=4, ipadx=4, ipady=4, fill=X)
        send_otp_button.pack(ipadx=4, ipady=2, pady=16)
        otp_label.pack(pady=2)
        otp_entry.pack(pady=8, padx=4, ipadx=4, ipady=4, fill=X)
        verify_otp_button.pack(ipadx=4, ipady=2, pady=16)
        password_label.pack(pady=2)
        password_entry.pack(pady=8, padx=4, ipadx=4, ipady=4, fill=X)
        confim_password_label.pack(pady=2)
        confim_password_entry.pack(pady=8, padx=4, ipadx=4, ipady=4, fill=X)
        reset_button.pack(ipadx=4, ipady=2, pady=16)
        self.email_frame.pack()

        Button(
            self,
            text="Back to Login",
            relief="flat",
            bg='#1565c0', fg="white",
            font='Helvetica 10',
            command=lambda: self.navigate('WelcomePage')
        )

        # griding
        left_frame.grid(row=0, column=0)
        right_frame.grid(row=0, column=1)

        # placing
        self.grid_rowconfigure(0, weight=7)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=7)         

    def send_otp_click(self):
        self.real_email = self.email.get()
        if check_student_exists(self.real_email):
            try:
                user = getStudentByEmail(self.email.get())
                self.real_phone = user['phone']
                (cotp, res) = send_otp_to_phone(user['phone'])
                print(cotp, res, self.real_phone)
                self.real_otp = cotp
                self.email_frame.pack_forget()  # disappears email_frame
                self.otp_frame.pack()
            except Exception as e:
                print('otp send error', e)
                messagebox.showerror(
                    "Server Fault", "Server error! Please try again")
        else:
            messagebox.showerror(
                "User Not Found", "Student with this email id doesnt exist")

    def verify_otp_click(self):
        if self.otp.get().strip() == str(self.real_otp):
            self.otp_frame.pack_forget()
            self.password_reset_frame.pack()
        else:
            messagebox.showerror(
                "Wrong OTP", "You have entered an invalid OTP")
            self.otp_frame.pack_forget()
            self.email_frame.pack()
            self.email.set('')
            self.otp.set('')

    def update_password_click(self):
        if not is_valid_password(self.password.get()):
            messagebox.showerror(
                "Invalid Password", "Enter Valid Password")
        elif self.password.get() != self.confirm_password.get():
            messagebox.showerror(
                "Invalid Password", "Password and Confirm Password should be same!!")
        else:
            password_reset(self.real_email, self.password.get())
            messagebox.showinfo("Reset successful",
                                "Please login again with your new password.")
            self.navigate('WelcomePage')
