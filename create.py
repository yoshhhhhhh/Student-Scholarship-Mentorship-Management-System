import streamlit as st
from database import( add_data,
                       add_data_admin,
    add_data_administer,
    add_data_bankaccountdetails,
    add_data_courses,
    add_data_enrols,
    add_data_faculty,
    add_data_mentor,
    add_data_payment,
    add_data_scholarship,
    add_data_semester,
    add_data_student
                     )


def create():
    col1, col2 = st.columns(2)
    with col1:
        dealer_id = st.text_input("ID:")
        dealer_name = st.text_input("Name:")
    with col2:
        dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        dealer_pin = st.text_input("Pin Code:")
    dealer_street = st.text_input("Street Name:")
    if st.button("Add Dealer"):
        add_data(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
        st.success("Successfully added Dealer: {}".format(dealer_name))
        
def create_admin():
    col1, col2 = st.columns(2)
    with col1:
        admin_id = st.text_input("Admin ID:")
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
    with col2:
        phone_no = st.text_input("Phone Number:")
    if st.button("Add Admin"):
        add_data_admin(admin_id, username, password, phone_no)
        st.success("Successfully added Admin: {}".format(username))


def create_administer():
    col1, col2 = st.columns(2)
    with col1:
        admin_id = st.text_input("Admin ID:")
        student_id = st.text_input("Student ID:")
        faculty_id = st.text_input("Faculty ID:")
    with col2:
        scholarship_id = st.text_input("Scholarship ID:")
        account_number = st.text_input("Account Number:")
        transaction_id = st.text_input("Transaction ID:")
    if st.button("Add Administer"):
        add_data_administer(admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id)
        st.success("Successfully added Administer entry")


def create_bankaccountdetails():
    col1, col2 = st.columns(2)
    with col1:
        account_number = st.text_input("Account Number:")
        ifsc_code = st.text_input("IFSC Code:")
    with col2:
        acc_holder_name = st.text_input("Account Holder Name:")
        student_id = st.text_input("Student ID:")
    if st.button("Add Bank Account Details"):
        add_data_bankaccountdetails(account_number, ifsc_code, acc_holder_name, student_id)
        st.success("Successfully added Bank Account Details")


def create_courses():
    col1, col2 = st.columns(2)
    with col1:
        sem_id = st.text_input("Semester ID:")
        course_name = st.text_input("Course Name:")
    if st.button("Add Course"):
        add_data_courses(sem_id, course_name)
        st.success("Successfully added Course")


def create_enrols():
    col1, col2 = st.columns(2)
    with col1:
        sem_id = st.text_input("Semester ID:")
        SRN = st.text_input("Student Registration Number:")
        SGPA = st.number_input("SGPA:")
    with col2:
        section = st.text_input("Section:")
        attendance = st.number_input("Attendance:")
    if st.button("Add Enrolment"):
        add_data_enrols(sem_id, SRN, SGPA, section, attendance)
        st.success("Successfully added Enrolment entry")


def create_faculty():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name:")
        faculty_id = st.text_input("Faculty ID:")
        address = st.text_input("Address:")
    with col2:
        dob = st.date_input("Date of Birth:")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        dept_name = st.text_input("Department Name:")
    if st.button("Add Faculty"):
        add_data_faculty(name, faculty_id, address, dob, gender, dept_name)
        st.success("Successfully added Faculty")


def create_mentor():
    col1, col2 = st.columns(2)
    with col1:
        faculty_id = st.text_input("Faculty ID:")
        student_id = st.text_input("Student ID:")
        fam_date = st.date_input("Family Date:")
    with col2:
        issues = st.text_area("Issues:")
    if st.button("Add Mentor"):
        add_data_mentor(faculty_id, student_id, fam_date, issues)
        st.success("Successfully added Mentor entry")


def create_payment():
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Date:")
        time = st.time_input("Time:")
    with col2:
        status = st.text_input("Status:")
        transaction_id = st.text_input("Transaction ID:")
        scholarship_id = st.text_input("Scholarship ID:")
    if st.button("Add Payment"):
        add_data_payment(date, time, status, transaction_id,scholarship_id)
        st.success("Successfully added Payment entry")


def create_scholarship():
    col1, col2 = st.columns(2)
    with col1:
        scholarship_id = st.text_input("Scholarship ID:")
        amount = st.number_input("Amount:")
        criteria = st.text_input("Criteria:")
    with col2:
        name = st.text_input("Name:")
        student_id = st.text_input("Student ID:")
    if st.button("Add Scholarship"):
        add_data_scholarship(scholarship_id, amount, criteria, name, student_id)
        st.success("Successfully added Scholarship")


def create_semester():
    col1, col2 = st.columns(2)
    with col1:
        sem_number = st.number_input("Semester Number:")
        sem_id = st.text_input("Semester ID:")
    with col2:
        academic_year = st.text_input("Academic Year:")
    if st.button("Add Semester"):
        add_data_semester(sem_number, sem_id, academic_year)
        st.success("Successfully added Semester")


def create_student():
    col1, col2 = st.columns(2)
    with col1:
        SRN = st.text_input("Student Registration Number:")
        name = st.text_input("Name:")
        address = st.text_input("Address:")
        DOB = st.date_input("Date of Birth:")
    with col2:
        dept_name = st.text_input("Department Name:")
        CGPA = st.number_input("CGPA:")
        phone_no = st.text_input("Phone Number:")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        email_id = st.text_input("Email ID:")
    if st.button("Add Student"):
        add_data_student(SRN, name, address, DOB, dept_name, CGPA, phone_no, gender, email_id)
        st.success("Successfully added Student")