from tkinter import *
from tkinter_nav.wrapper import Wrapper

# import all pages
from pages.student_request import ReviewChangesPage
from pages.all_requests import AllRequestsPage
from pages.reset_password import PasswordResetPage
from pages.admin_page import AdminHomePage
from pages.student_home import StudentHomePage
from pages.register import RegisterPage
from pages.welcome import WelcomePage

print("Python Mini Project Using Tkinter")

class RootPage(Wrapper):
    def __init__(self):

        Wrapper.__init__(self, pages=[
            # Before Login pages
            WelcomePage,
            RegisterPage,
            PasswordResetPage,

            # Student pages
            StudentHomePage,

            # Admin pages
            AdminHomePage,
            AllRequestsPage,
            ReviewChangesPage,
        ], start_state={
            'college_logo': './images/logo.png',
            'college_name': 'Raghu Institute Of Technology\n(Autonomous)',
            'sample_user_dp': './images/user.png',
            'user_id': -1,
            'review_id': -1
        })


        self.title("My Python Mini Project")
        self.geometry("%dx%d" % (1280, 768))
        self.configure(background='white')
        self.show_page('WelcomePage')

if __name__ == '__main__':
    root = RootPage()
    root.mainloop()
