import sys
from tkinter import *
from tkinter import messagebox

from tkinter_nav.page import Page
from utils.request_utils import deleteRequest, getRequest, getRequests, mergeRequest
from utils.students_utils import getStudentById, login_student
from views.profile_image import ProfileImage


class ReviewChangesPage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent, 'ReviewChangesPage')
        self.configure(background='white')

    def page_did_mount(self):
        self.review_id = self.app_state['review_id']
        if self.review_id == -1:
            return

        new_data = getRequest(self.review_id)
        old_data = getStudentById(new_data['id'])
        items = [
            ("Your first name", 'first_name'),
            ("Your last name",  'last_name'),
            ("Your address",    'address'),
            ("Your phone",      'phone'),
            ("Your email",      'email'),
            ("Your department", 'department'),
            ("Your CGPA",       'cgpa')
        ]

        # dividing into frames
        left_frame = Frame(self, background="white")

        Label(left_frame,
              text="Before",
              background='#fff', font='4'
              ).grid(row=0, column=1)

        old_profile_image = ProfileImage(left_frame, old_data['profile_pic'])
        profileImageOld = Label(left_frame, image=old_profile_image, bd=0)
        profileImageOld.image = old_profile_image
        profileImageOld.grid(row=1, column=1, pady=6, padx=2, sticky='we')
        for i, item in enumerate(items):
            label, key = item
            Label(
                left_frame,
                relief="flat",
                text=label,
                bg='#fff',

            ).grid(row=i+2, column=0, pady=4, padx=2, sticky='w')
            Label(
                left_frame,
                relief="flat",
                text=' : ',
                bg='#fff',

            ).grid(row=i+2, column=1, pady=4, padx=2)
            Label(
                left_frame,
                relief="flat",
                text=str(old_data[key]),
                bg='#fff',

            ).grid(row=i+2, column=2, pady=4, padx=2, sticky='w')

        right_frame = Frame(self, background="white")

        Label(right_frame,
              text="After",
              background='#fff', font='4'
              ).grid(row=0, column=1)

        new_profile_image = ProfileImage(right_frame, new_data['profile_pic'])
        profileImageNew = Label(right_frame, image=new_profile_image, bd=0)
        profileImageNew.image = new_profile_image
        profileImageNew.grid(row=1, column=1, pady=6, padx=2, sticky='we')
        for i, item in enumerate(items):
            label, key = item
            Label(
                right_frame,
                relief="flat",
                text=label,
                bg='#fff',
            ).grid(row=i+2, column=0, pady=4, padx=2, sticky='w')
            Label(
                right_frame,
                relief="flat",
                text=' : ',
                bg='#fff',

            ).grid(row=i+2, column=1, pady=4, padx=2)
            Label(
                right_frame,
                relief="flat",
                text=str(new_data[key]),
                bg='#fff',

            ).grid(row=i+2, column=2, pady=4, padx=2, sticky='w')

        buttons_frame = Frame(self)

        cancel_button = Button(
            buttons_frame,
            text="Cancel",
            relief="flat",
            bg='#616161', fg="white",
            font='Helvetica 12',
            command=self.cancel_request,
        )
        decline_button = Button(
            buttons_frame,
            text="Decline",
            relief="flat",
            bg='#d32f2f', fg="white",
            font='Helvetica 12',
            command=self.decline_request,
        )

        accept_button = Button(
            buttons_frame,
            text="Accept",
            relief="flat",
            bg='#2e7d32', fg="white",
            font='Helvetica 12',
            command=self.accept_request,
        )

        # griding
        cancel_button.grid(row=1, column=0, padx=12,
                           ipadx=16, pady=16, sticky='e')
        decline_button.grid(row=1, column=1, padx=12,
                            ipadx=16, pady=16, sticky='e')
        accept_button.grid(row=1, column=2, padx=12,
                           ipadx=16, pady=16, sticky='w')

        left_frame.grid(row=0, column=0)
        right_frame.grid(row=0, column=1)
        buttons_frame.grid(row=1, column=0, columnspan=2)

        # placing
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        return super().page_did_mount()

    def cancel_request(self):
        answer = messagebox.askquestion(
            "Cancel Message", "Are you sure you want to cancel and go back to ALl requests?")
        if answer == "yes":
            self.openAllRequests()

    def decline_request(self):
        answer = messagebox.askquestion(
            "Decline Message", "Are you sure you want to decline")
        if answer == "yes":
            deleteRequest(self.review_id)
            self.openAllRequests()

    def accept_request(self):
        answer = messagebox.askquestion(
            "Accept Message", "Are you sure you want to accept the change")
        if answer == "yes":
            mergeRequest(self.review_id)
            self.openAllRequests()

    def openAllRequests(self):
        self.app_state['review_id'] = -1
        self.update_state()
        self.navigate('AllRequestsPage')
