import datetime

import pandas as pd
import streamlit as st
# from database import (view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data,
#                         view_all_data_admin,view_all_data_administer,view_only_admin_names,
#                          get_admin,edit_admin_data, view_only_administer_ids,get_administer,
#                         edit_administer_data,    view_all_data_bankaccountdetails,
#                         view_only_bankaccountdetails_ids,get_bankaccountdetails, edit_bankaccountdetails_data,
#                         view_all_data_courses, view_only_course_ids,get_course,edit_course_data,
#                         view_all_data_enrols,view_only_enrols_ids,get_enrol,edit_enrols_data
#                         )
from database import *


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Current Dealers"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_dealer_names()]
    selected_dealer = st.selectbox("Dealer to Edit", list_of_dealers)
    selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        dealer_id = selected_result[0][0]
        dealer_name = selected_result[0][1]
        dealer_city = selected_result[0][2]
        dealer_pin = selected_result[0][3]
        dealer_street = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_dealer_id = st.text_input("ID:", dealer_id)
            new_dealer_name = st.text_input("Name:", dealer_name)
        with col2:
            new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])
            new_dealer_pin = st.text_input("Pin Code:", dealer_pin)
        new_dealer_street = st.text_input("Street Name:", dealer_street)
        if st.button("Update Dealer"):
            edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
            st.success("Successfully updated:: {} to ::{}".format(dealer_name, new_dealer_name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        



# Update the function definition in update.py
def update_admin():
    result = view_all_data_admin()
    df = pd.DataFrame(result, columns=['Admin ID', 'Admin Name', 'Admin Password', 'Admin Phone Number'])
    with st.expander("Current Admins"):
        st.dataframe(df)
    list_of_admins = [i[0] for i in view_only_admin_ids()]
    selected_admin = st.selectbox("Admin to Edit", list_of_admins)
    selected_result = get_admin(selected_admin)

    if selected_result:
        admin_id = selected_result[0][0]
        admin_name = selected_result[0][1]
        admin_password = selected_result[0][2]
        admin_phone_no = selected_result[0][3]  # Assuming phone_no is at index 3, modify if needed

        # Layout for updating admin data

        col1, col2, col3 = st.columns(3)
        with col1:
            new_admin_id = st.text_input("ID:", admin_id)
            new_admin_name = st.text_input("Name:", admin_name)
        with col2:
            new_admin_password = st.text_input("Password:", admin_password)
        with col3:
            new_admin_phone_no = st.text_input("Phone Number:", admin_phone_no)

        if st.button("Update Admin"):
            # Pass all updated fields to the edit_admin_data function
            edit_admin_data(new_admin_id, new_admin_name, new_admin_password, new_admin_phone_no, admin_id)
            st.success("Successfully updated Admin: {} to {}".format(admin_name, new_admin_name))

    result2 = view_all_data_admin()
    df2 = pd.DataFrame(result2, columns=['Admin ID', 'Admin Name', 'Admin Password', 'Admin Phone Number'])
    with st.expander("Updated Admin Data"):
        st.dataframe(df2)


def update_administer():
    result = view_all_data_administer()
    df = pd.DataFrame(result, columns=['Administer ID', 'Admin ID', 'Semester ID'])
    with st.expander("Current Administers"):
        st.dataframe(df)
    list_of_administers = [i[0] for i in view_only_administer_ids()]
    selected_administer = st.selectbox("Administer to Edit", list_of_administers)
    selected_result = get_administer(selected_administer)

    if selected_result:
        administer_id = selected_result[0][0]
        admin_id = selected_result[0][1]
        semester_id = selected_result[0][2]

        # Layout for updating administer data

        col1, col2 = st.columns(2)
        with col1:
            new_administer_id = st.text_input("Administer ID:", administer_id)
            new_admin_id = st.text_input("Admin ID:", admin_id)
        with col2:
            new_semester_id = st.text_input("Semester ID:", semester_id)

        if st.button("Update Administer"):
            edit_administer_data(new_administer_id, new_admin_id, new_semester_id, administer_id, admin_id, semester_id)
            st.success("Successfully updated Administer ID: {} to {}".format(administer_id, new_administer_id))

    result2 = view_all_data_administer()
    df2 = pd.DataFrame(result2, columns=['Administer ID', 'Admin ID', 'Semester ID'])
    with st.expander("Updated Administer Data"):
        st.dataframe(df2)
        
        

def update_bankaccountdetails():
    result = view_all_data_bankaccountdetails()
    df = pd.DataFrame(result, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
    with st.expander("Current Bank Account Details"):
        st.dataframe(df)
    list_of_accounts = [i[0] for i in view_only_bankaccountdetails_ids()]
    selected_account = st.selectbox("Bank Account to Edit", list_of_accounts)
    selected_result = get_bankaccountdetails(selected_account)

    if selected_result:
        account_number = selected_result[0][0]
        ifsc_code = selected_result[0][1]
        account_holder_name = selected_result[0][2]
        student_id = selected_result[0][3]

        # Layout for updating bank account details

        col1, col2 = st.columns(2)
        with col1:
            new_account_number = st.text_input("Account Number:", account_number)
            new_ifsc_code = st.text_input("IFSC Code:", ifsc_code)
        with col2:
            new_account_holder_name = st.text_input("Account Holder Name:", account_holder_name)
            new_student_id = st.text_input("Student ID:", student_id)

        if st.button("Update Bank Account"):
            edit_bankaccountdetails_data(new_account_number, new_ifsc_code, new_account_holder_name, new_student_id, account_number)
            st.success("Successfully updated Bank Account: {} to {}".format(account_number, new_account_number))

    result2 = view_all_data_bankaccountdetails()
    df2 = pd.DataFrame(result2, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
    with st.expander("Updated Bank Account Details"):
        st.dataframe(df2)


# Updated get_courses function
def get_courses(sem_id, course_name):
    c.execute('SELECT * FROM courses WHERE sem_id=%s AND course_name=%s', (sem_id, course_name))
    data = c.fetchall()
    return data

def update_courses():
    result = view_all_data_courses()
    df = pd.DataFrame(result, columns=['Semester ID', 'Course Name'])
    with st.expander("Current Courses"):
        st.dataframe(df)
    list_of_courses = [(i[0], i[1]) for i in view_only_courses_ids()]
    selected_course = st.selectbox("Course to Edit", list_of_courses)
    
    if selected_course:
        selected_sem_id, selected_course_name = selected_course
        selected_result = get_courses(selected_sem_id, selected_course_name)

        if selected_result:
            sem_id = selected_result[0][0]
            course_name = selected_result[0][1]

            # Layout for updating course details
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Semester ID:", sem_id, key="sem_id", disabled=True)
            with col2:
                new_course_name = st.text_input("Course Name:", course_name)

            if st.button("Update Course"):
                edit_courses_data(sem_id, new_course_name, sem_id, course_name)
                st.success("Successfully updated Course: {} to {}".format(course_name, new_course_name))

    result2 = view_all_data_courses()
    df2 = pd.DataFrame(result2, columns=['Semester ID', 'Course Name'])
    with st.expander("Updated Course Details"):
        st.dataframe(df2)




def update_enrols():
    result = view_all_data_enrols()
    df = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
    with st.expander("Current Enrolments"):
        st.dataframe(df)
    list_of_enrols = [(i[0], i[1]) for i in view_only_enrols_ids()]
    selected_enrol = st.selectbox("Enrolment to Edit", list_of_enrols)
    selected_sem_id, selected_srn = selected_enrol
    selected_result = get_enrols(selected_sem_id, selected_srn)

    if selected_result:
        sem_id = selected_result[0][0]
        srn = selected_result[0][1]
        sgpa = selected_result[0][2]
        section = selected_result[0][3]
        attendance = selected_result[0][4]

        # Layout for updating enrolment details

        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Semester ID:", sem_id, key="sem_id", disabled=True)
            st.text_input("Student ID:", srn, key="srn", disabled=True)
        with col2:
            new_sgpa = st.text_input("SGPA:", sgpa)
            new_section = st.text_input("Section:", section)
            new_attendance = st.text_input("Attendance:", attendance)

        if st.button("Update Enrolment"):
            edit_enrols_data(sem_id, srn, new_sgpa, new_section, new_attendance,sem_id,srn)
            st.success("Successfully updated Enrolment for Student ID: {}".format(srn))

    result2 = view_all_data_enrols()
    df2 = pd.DataFrame(result2, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
    with st.expander("Updated Enrolment Details"):
        st.dataframe(df2)

        
        
        

def update_faculty():
    result = view_all_data_faculty()
    df = pd.DataFrame(result, columns=[ 'Faculty Name', 'Faculty ID','Faculty Address', 'Date of Birth', 'Gender', 'Department'])
    with st.expander("Current Faculty"):
        st.dataframe(df)
    list_of_faculty = [i[0] for i in view_only_faculty_ids()]
    selected_faculty = st.selectbox("Faculty to Edit", list_of_faculty)
    selected_result = get_faculty(selected_faculty)

    if selected_result:
        faculty_name = selected_result[0][0]
        faculty_id = selected_result[0][1]
        
        faculty_address = selected_result[0][2]
        faculty_dob = selected_result[0][3]
        faculty_gender = selected_result[0][4]
        faculty_department = selected_result[0][5]

        # Layout for updating faculty details

        col1, col2 = st.columns(2)
        with col1:
            new_faculty_id = st.text_input("Faculty ID:", faculty_id)
            new_faculty_name = st.text_input("Faculty Name:", faculty_name)
            new_faculty_dob = st.text_input("Date of Birth:", faculty_dob)
        with col2:
            new_faculty_address = st.text_input("Faculty Address:", faculty_address)
            new_faculty_gender = st.text_input("Gender:", faculty_gender)
            new_faculty_department = st.text_input("Department:", faculty_department)

        if st.button("Update Faculty"):
            edit_faculty_data( new_faculty_name, new_faculty_id, new_faculty_address, new_faculty_dob, new_faculty_gender, new_faculty_department, faculty_id)
            st.success("Successfully updated Faculty: {} to {}".format(faculty_id, new_faculty_id))

    result2 = view_all_data_faculty()
    df2 = pd.DataFrame(result2, columns=[ 'Faculty Name', 'Faculty ID','Faculty Address', 'Date of Birth', 'Gender', 'Department'])
    with st.expander("Updated Faculty Details"):
        st.dataframe(df2)


def update_mentor():
    result = view_all_data_mentor()
    df = pd.DataFrame(result, columns=['MentorID', 'StudentID', 'FAM date','Issues'])
    with st.expander("Current Mentors"):
        st.dataframe(df)
    list_of_mentors = [(i[0], i[1],i[2].strftime("%Y-%m-%d")) for i in view_only_mentor_admin_ids()]
    for mentor_tuple in list_of_mentors:
        print(mentor_tuple[2])
    selected_mentor = st.selectbox("Mentor to Edit", list_of_mentors)
    mentor_id,student_id,fam_date =selected_mentor[:3] 
    selected_result = get_mentor_admin(mentor_id,student_id,fam_date)

    if selected_result:
        mentor_id = selected_result[0][0]
        student_id=selected_result[0][1]
        fam_date=selected_result[0][2]
        issues=selected_result[0][3]
        # mentor_name = selected_result[0][1]
        # faculty_id = selected_result[0][2]

        # Layout for updating mentor details

        col1, col2 = st.columns(2)
        with col1:
            new_mentor_id = st.text_input("Mentor ID:", mentor_id)
            new_student_id = st.text_input("Student ID:", student_id)
        with col2:
            new_fam_date = st.text_input("FAM Date:", fam_date)
            new_issues = st.text_input("Issues:",issues)

        if st.button("Update Mentor"):
            edit_mentor_data(new_mentor_id, new_student_id, new_fam_date, new_issues, mentor_id, student_id,fam_date)
            st.success("Successfully updated Mentor: {} to {}".format(mentor_id, new_mentor_id))

    result2 = view_all_data_mentor()
    df2 = pd.DataFrame(result2, columns=['Mentor ID', 'Student ID', 'Fam Date','Issues'])
    with st.expander("Updated Mentor Details"):
        st.dataframe(df2)


def update_payment():
    result = view_all_data_payment()
    df = pd.DataFrame(result, columns=['Date','Time','Status','Payment ID',  'Scholarship ID'])
    with st.expander("Current Payments"):
        df['Time'] = df['Time'].astype(str)
        st.dataframe(df)
    list_of_payments = [i[0] for i in view_only_payment_ids()]
    selected_payment = st.selectbox("Payment to Edit", list_of_payments)
    selected_result = get_payment(selected_payment)

    if selected_result:
        # payment_id = selected_result[0][0]
        # amount = selected_result[0][1]
        # date = selected_result[0][2]
        # student_id = selected_result[0][3]
        
        date = selected_result[0][0]
        time = selected_result[0][1]
        status = selected_result[0][2]
        payment_id = selected_result[0][3]
        scholarship_id=selected_result[0][4]

        # Layout for updating payment details

        col1, col2 = st.columns(2)
        with col1:
            new_payment_id = st.text_input("Payment ID:", payment_id)
            new_time = st.text_input("time:", time)
            new_status = st.text_input("time:", status)
        with col2:
            new_date = st.text_input("Date:", date)
            new_scholarship_id = st.text_input("Scholarship ID:", scholarship_id)

        if st.button("Update Payment"):
            edit_payment_data(new_date, new_time, new_status, new_payment_id,new_scholarship_id, payment_id)
            st.success("Successfully updated Payment ID: {} to {}".format(payment_id, new_payment_id))

    result2 = view_all_data_payment()
    df2 = pd.DataFrame(result2, columns=['Date','Time','Status','Payment ID',  'Scholarship ID'])
    with st.expander("Updated Payment Details"):
        df2['Time'] = df2['Time'].astype(str)

        st.dataframe(df2)

def update_scholarship():
    result = view_all_data_scholarship()
    df = pd.DataFrame(result, columns=['Scholarship ID', 'Amount', 'Criteria', 'Name', 'Student ID'])
    with st.expander("Current Scholarships"):
        st.dataframe(df)
    list_of_scholarships = [i[0] for i in view_only_scholarship_ids()]
    selected_scholarship = st.selectbox("Scholarship to Edit", list_of_scholarships)
    selected_result = get_scholarship(selected_scholarship)

    if selected_result:
        scholarship_id = selected_result[0][0]
        amount = selected_result[0][1]
        criteria = selected_result[0][2]
        name = selected_result[0][3]
        student_id = selected_result[0][4]

        # Layout for updating scholarship details

        col1, col2 = st.columns(2)
        with col1:
            new_scholarship_id = st.text_input("Scholarship ID:", scholarship_id)
            new_amount = st.text_input("Amount:", amount)
            new_criteria = st.text_input("Criteria:", criteria)
        with col2:
            new_name = st.text_input("Name:", name)
            new_student_id = st.text_input("Student ID:", student_id)

        if st.button("Update Scholarship"):
            edit_scholarship_data(new_scholarship_id, new_amount, new_criteria, new_name, new_student_id, scholarship_id)
            st.success("Successfully updated Scholarship ID: {} to {}".format(scholarship_id, new_scholarship_id))

    result2 = view_all_data_scholarship()
    df2 = pd.DataFrame(result2, columns=['Scholarship ID', 'Amount', 'Criteria', 'Name', 'Student ID'])
    with st.expander("Updated Scholarship Details"):
        st.dataframe(df2)


def update_semester():
    result = view_all_data_semester()
    df = pd.DataFrame(result, columns=['Semester Number','Semester ID', 'Academic year'])
    with st.expander("Current Semesters"):
        st.dataframe(df)
    list_of_semesters = [i[0] for i in view_only_semester_ids()]
    selected_semester = st.selectbox("Semester to Edit", list_of_semesters)
    
    selected_result = get_semester(selected_semester)

    if selected_result:
        
        semester_number = selected_result[0][0]
        semester_id = selected_result[0][1]
        academic_year=selected_result[0][2]

        # Layout for updating semester details

        col1, col2 = st.columns(2)
        with col1:
            new_semester_id = st.text_input("Semester ID:", semester_id)
            new_semester_number = st.text_input("Semester Number:", semester_number)
        with col2:
            # new_start_date = st.text_input("Start Date:", start_date)
            # new_end_date = st.text_input("End Date:", end_date)
            new_academic_year = st.text_input("ACADEMIC Yeaf:",academic_year)

        if st.button("Update Semester"):
            edit_semester_data(new_semester_id, new_semester_number, new_academic_year, semester_id)
            st.success("Successfully updated Semester ID: {} to {}".format(semester_id, new_semester_id))

    result2 = view_all_data_semester()
    df2 = pd.DataFrame(result2, columns=[ 'Semester Number', 'Semester ID', 'Academic year'])
    with st.expander("Updated Semester Details"):
        st.dataframe(df2)

# Update function
def update_student():
    result = view_all_data_student()
    df = pd.DataFrame(result, columns=['Student ID', 'Name', 'Date of Birth', 'Address', 'Dept Name', 'CGPA', 'Phone Number', 'Gender', 'Email'])
    with st.expander("Current Students"):
        st.dataframe(df)
    list_of_students = [i[0] for i in view_only_student_ids()]
    selected_student = st.selectbox("Student to Edit", list_of_students)
    selected_result = get_student(selected_student)

    if selected_result:
        student_id = selected_result[0][0]
        name = selected_result[0][1]
        dob = selected_result[0][2]
        address = selected_result[0][3]
        dept_name = selected_result[0][4]
        cgpa = selected_result[0][5]
        phone_number = selected_result[0][6]
        gender = selected_result[0][7]
        email = selected_result[0][8]

        # Layout for updating student details
        col1, col2 = st.columns(2)
        with col1:
            new_student_id = st.text_input("Student ID:", student_id)
            new_name = st.text_input("Name:", name)
            new_dob = st.text_input("Date of Birth:", dob)
            new_address = st.text_input("Address:", address)
            new_dept_name = st.text_input("Dept Name:", dept_name)
        with col2:
            new_cgpa = st.text_input("CGPA:", cgpa)
            new_phone_number = st.text_input("Phone Number:", phone_number)
            new_gender = st.text_input("Gender:", gender)
            new_email = st.text_input("Email:", email)

        if st.button("Update Student"):
            edit_student_data(
                new_student_id, new_name, new_dob, new_address, new_dept_name,
                new_cgpa, new_phone_number, new_gender, new_email, student_id
            )
            st.success("Successfully updated Student ID: {} to {}".format(student_id, new_student_id))

    result2 = view_all_data_student()
    df2 = pd.DataFrame(result2, columns=['Student ID', 'Name', 'Date of Birth', 'Address', 'Dept Name', 'CGPA', 'Phone Number', 'Gender', 'Email'])
    with st.expander("Updated Student Details"):
        st.dataframe(df2)


def front_all_update():
    edit_options = ["Admin", "Administer", "Bank Account Details", "Courses", "Enrols", "Faculty", "Mentor", "Payment", "Scholarship", "Semester", "Student"]
    edit_choice = st.selectbox("Select Data Type to Edit", edit_options)

    if edit_choice == "Admin":
        # Update data for Admin
        update_admin()
    
    #elif edit_choice == "Administer":
        # Update data for Administer
       # update_administer()

    elif edit_choice == "Bank Account Details":
        # Update data for Bank Account Details
        update_bankaccountdetails()

    elif edit_choice == "Courses":
        # Update data for Courses
        update_courses()

    elif edit_choice == "Enrols":
        # Update data for Enrols
        update_enrols()

    elif edit_choice == "Faculty":
        # Update data for Faculty
        update_faculty()

    elif edit_choice == "Mentor":
        # Update data for Mentor
        update_mentor()

    elif edit_choice == "Payment":
        # Update data for Payment
        update_payment()

    elif edit_choice == "Scholarship":
        # Update data for Scholarship
        update_scholarship()

    elif edit_choice == "Semester":
        # Update data for Semester
        update_semester()

    elif edit_choice == "Student":
        # Update data for Student
        update_student()


        
