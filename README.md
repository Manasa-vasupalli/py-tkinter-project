### Python mini project using tkinter

1) First prepare welcome screen consisting of login and signup page

2) If this is the first time you are logging into website, click on signup

3) In signup page provide entries such as 
   
      firstname, lastname, contactnumber, address (Next)
      
      emailid, password, confirm password(min 8 and max 15characters)   (Next)
      
      department and cgpa for credits

      (Register)

      Create option like upload photo, validate email, contactnumber; verify OTP concept also validate all these details entered are correct or not. If successful store all the detais in text file in the form of dictionary, if any error is found, show the error in the form of popup.

4) Once registration successful, it should be redirected to home page and student enters username and password. Once correct details are provided, create a button called View details in his page. Once clicked on View details, all his details should be displayed in the form of table. display photo in his page. report error if username and password are incorrect

5) Suppose if a student request any details to be updated he should sent request to admin to update his details

6) In admin page after logging with his username and password, in the admin page provide several options like

      - View student details by rollno
      - View student details by department
      - View student details who has cgpa>7 (decide range you want to choose)
      - Update student details upon request from studentv