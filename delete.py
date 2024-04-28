import pandas as pd
import streamlit as st
from database import (
    view_all_data, view_only_dealer_names, delete_data,
    view_all_data_administer,view_all_data_bankaccountdetails,view_all_data_courses,view_all_data_admin,
    view_all_data_enrols,view_all_data_faculty,view_all_data_mentor,view_all_data_payment,
    view_all_data_scholarship,view_all_data_semester,view_all_data_student,
    view_only_admin_ids,
    view_only_administer_ids,view_only_mentor_admin_ids,
    view_only_bankaccountdetails_ids, view_only_courses_ids, 
    view_only_enrols_ids, view_only_faculty_ids, view_only_mentor_ids, 
    view_only_payment_ids, view_only_scholarship_ids, view_only_semester_ids,
    view_only_student_ids,delete_admin_data, delete_administer_data ,delete_bankaccountdetails_data,
    delete_courses_data,delete_enrols_data, delete_faculty_data ,delete_mentor_data,
    delete_payment_data, delete_scholarship_data,delete_semester_data,delete_student_data)

def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_dealer_names()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete ::{}".format(selected_dealer))
    if st.button("Delete Dealer"):
        delete_data(selected_dealer)
        st.success("Dealer has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Updated data"):
        st.dataframe(df2)



def delete_admin():
    result = view_all_data_admin()  # You need to modify this function to retrieve admin data
    df = pd.DataFrame(result, columns=['Admin ID', 'Username', 'Password', 'Phone Number'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_admins = [i[0] for i in view_only_admin_ids()]
    selected_admin = st.selectbox("Task to Delete", list_of_admins)
    st.warning("Do you want to delete ::{}".format(selected_admin))
    if st.button("Delete Admin"):
        delete_admin_data(selected_admin)
        st.success("Admin has been deleted successfully")
    new_result = view_all_data_admin()  # You need to modify this function to retrieve updated admin data
    df2 = pd.DataFrame(new_result, columns=['Admin ID', 'Username', 'Password', 'Phone Number'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_administer():
    result = view_all_data_administer()
    df = pd.DataFrame(result, columns=['Admin ID', 'Student ID', 'Faculty ID', 'Scholarship ID', 'Account Number', 'Transaction ID'])
    with st.expander("Current Administer data"):
        st.dataframe(df)
    list_of_administers = [i for i in view_only_administer_ids()]
    selected_administer = st.selectbox("Task to Delete", list_of_administers)
    st.warning("Do you want to delete Administer ::{}".format(selected_administer))
    if st.button("Delete Administer"):
        delete_administer_data(*selected_administer)
        st.success("Administer data has been deleted successfully")
    new_result = view_all_data_administer()
    df2 = pd.DataFrame(new_result, columns=['Admin ID', 'Student ID', 'Faculty ID', 'Scholarship ID', 'Account Number', 'Transaction ID'])
    with st.expander("Updated Administer data"):
        st.dataframe(df2)
        
#for bank account
def delete_bankaccountdetails():
    result = view_all_data_bankaccountdetails()
    df = pd.DataFrame(result, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
    with st.expander("Current Bank Account Details"):
        st.dataframe(df)
    list_of_accounts = [i[0] for i in view_only_bankaccountdetails_ids()]
    selected_account = st.selectbox("Task to Delete", list_of_accounts)
    st.warning("Do you want to delete Bank Account ::{}".format(selected_account))
    if st.button("Delete Bank Account"):
        delete_bankaccountdetails_data(selected_account)
        st.success("Bank Account details have been deleted successfully")
    new_result = view_all_data_bankaccountdetails()
    df2 = pd.DataFrame(new_result, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
    with st.expander("Updated Bank Account Details"):
        st.dataframe(df2)


def delete_courses():
    result = view_all_data_courses()
    df = pd.DataFrame(result, columns=['Semester ID', 'Course Name'])
    with st.expander("Current Courses"):
        st.dataframe(df)
    list_of_courses = [(i[0], i[1]) for i in view_only_courses_ids()]
    selected_course = st.selectbox("Task to Delete", list_of_courses)
    st.warning("Do you want to delete Course ::{}".format(selected_course))
    if st.button("Delete Course"):
        delete_courses_data(selected_course[0], selected_course[1])
        st.success("Course has been deleted successfully")
    new_result = view_all_data_courses()
    df2 = pd.DataFrame(new_result, columns=['Semester ID', 'Course Name'])
    with st.expander("Updated Courses"):
        st.dataframe(df2)


def delete_enrols():
    result = view_all_data_enrols()
    df = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
    with st.expander("Current Enrols Data"):
        st.dataframe(df)
    list_of_enrols = [(i[0], i[1]) for i in view_only_enrols_ids()]
    selected_enrol = st.selectbox("Task to Delete", list_of_enrols)
    st.warning("Do you want to delete Enrolment ::{}".format(selected_enrol))
    if st.button("Delete Enrolment"):
        delete_enrols_data(selected_enrol[0], selected_enrol[1])
        st.success("Enrolment has been deleted successfully")
    new_result = view_all_data_enrols()
    df2 = pd.DataFrame(new_result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
    with st.expander("Updated Enrols Data"):
        st.dataframe(df2)
        

def delete_faculty():
    result = view_all_data_faculty()
    df = pd.DataFrame(result, columns=['Name', 'Faculty ID', 'Address', 'DOB', 'Gender', 'Department Name'])
    with st.expander("Current Faculty Data"):
        st.dataframe(df)
    list_of_faculty = [i[0] for i in view_only_faculty_ids()]
    selected_faculty = st.selectbox("Task to Delete", list_of_faculty)
    st.warning("Do you want to delete Faculty ::{}".format(selected_faculty))
    if st.button("Delete Faculty"):
        delete_faculty_data(selected_faculty)
        st.success("Faculty has been deleted successfully")
    new_result = view_all_data_faculty()
    df2 = pd.DataFrame(new_result, columns=['Name', 'Faculty ID', 'Address', 'DOB', 'Gender', 'Department Name'])
    with st.expander("Updated Faculty Data"):
        st.dataframe(df2)


def delete_mentor():
    result = view_all_data_mentor()
    df = pd.DataFrame(result, columns=['Faculty ID', 'Student ID', 'Family Date', 'Issues'])
    with st.expander("Current Mentor Data"):
        st.dataframe(df)
    list_of_mentors = [(i[0], i[1],i[2].strftime("%Y-%m-%d")) for i in view_only_mentor_admin_ids()]
    selected_mentor = st.selectbox("Task to Delete", list_of_mentors)
    st.warning("Do you want to delete Mentor ::{}".format(selected_mentor))
    if st.button("Delete Mentor"):
        delete_mentor_data(selected_mentor[0], selected_mentor[1])
        st.success("Mentor has been deleted successfully")
    new_result = view_all_data_mentor()
    df2 = pd.DataFrame(new_result, columns=['Faculty ID', 'Student ID', 'Fam Date', 'Issues'])
    with st.expander("Updated Mentor Data"):
        st.dataframe(df2)


def delete_payment():
    result = view_all_data_payment()
    df = pd.DataFrame(result, columns=['Date', 'Time', 'Status', 'Transaction ID','Scholarship ID'])
    with st.expander("Current Payment Data"):
        df['Time'] = df['Time'].astype(str)

        st.dataframe(df)
    list_of_payments = [i[0] for i in view_only_payment_ids()]
    selected_payment = st.selectbox("Task to Delete", list_of_payments)
    st.warning("Do you want to delete Payment ::{}".format(selected_payment))
    if st.button("Delete Payment"):
        delete_payment_data(selected_payment)
        st.success("Payment has been deleted successfully")
    new_result = view_all_data_payment()
    df2 = pd.DataFrame(new_result, columns=['Date', 'Time', 'Status', 'Transaction ID','Scholarship ID'])
    with st.expander("Updated Payment Data"):
        df2['Time'] = df2['Time'].astype(str)

        st.dataframe(df2)

def delete_scholarship():
    result = view_all_data_scholarship()
    df = pd.DataFrame(result, columns=['Scholarship ID', 'Amount', 'Criteria', 'Name', 'Student ID'])
    with st.expander("Current Scholarship Data"):
        st.dataframe(df)
    list_of_scholarships = [i[0] for i in view_only_scholarship_ids()]
    selected_scholarship = st.selectbox("Task to Delete", list_of_scholarships)
    st.warning("Do you want to delete Scholarship ::{}".format(selected_scholarship))
    if st.button("Delete Scholarship"):
        delete_scholarship_data(selected_scholarship)
        st.success("Scholarship has been deleted successfully")
    new_result = view_all_data_scholarship()
    df2 = pd.DataFrame(new_result, columns=['Scholarship ID', 'Amount', 'Criteria', 'Name', 'Student ID'])
    with st.expander("Updated Scholarship Data"):
        st.dataframe(df2)



def delete_semester():
    result = view_all_data_semester()
    df = pd.DataFrame(result, columns=['Semester Number', 'Semester ID', 'Academic Year'])
    with st.expander("Current Semester Data"):
        st.dataframe(df)
    list_of_semesters = [i[0] for i in view_only_semester_ids()]
    selected_semester = st.selectbox("Task to Delete", list_of_semesters)
    st.warning("Do you want to delete Semester ::{}".format(selected_semester))
    if st.button("Delete Semester"):
        delete_semester_data(selected_semester)
        st.success("Semester has been deleted successfully")
    new_result = view_all_data_semester()
    df2 = pd.DataFrame(new_result, columns=['Semester Number', 'Semester ID', 'Academic Year'])
    with st.expander("Updated Semester Data"):
        st.dataframe(df2)


def delete_student():
    result = view_all_data_student()
    df = pd.DataFrame(result, columns=['SRN', 'Name', 'Address', 'DOB', 'Dept Name', 'CGPA', 'Phone No', 'Gender', 'Email ID'])
    with st.expander("Current Student Data"):
        st.dataframe(df)
    list_of_students = [i[0] for i in view_only_student_ids()]
    selected_student = st.selectbox("Task to Delete", list_of_students)
    st.warning("Do you want to delete Student ::{}".format(selected_student))
    if st.button("Delete Student"):
        delete_student_data(selected_student)
        st.success("Student has been deleted successfully")
    new_result = view_all_data_student()
    df2 = pd.DataFrame(new_result, columns=['SRN', 'Name', 'Address', 'DOB', 'Dept Name', 'CGPA', 'Phone No', 'Gender', 'Email ID'])
    with st.expander("Updated Student Data"):
        st.dataframe(df2)



def front_remove():
    remove_options = ["Admin", "Administer", "Bank Account Details", "Courses", "Enrols", "Faculty", "Mentor", "Payment", "Scholarship", "Semester", "Student"]
    remove_choice = st.selectbox("Select Data Type to Remove", remove_options)

    if remove_choice == "Admin":
        # Implement the logic to remove admin data
        delete_admin()
    elif remove_choice == "Administer":
        # Implement the logic to remove administer data
        delete_administer()
    elif remove_choice == "Bank Account Details":
        # Implement the logic to remove bank account details data
        delete_bankaccountdetails()
    elif remove_choice == "Courses":
        # Implement the logic to remove courses data
        delete_courses()
    elif remove_choice == "Enrols":
        # Implement the logic to remove enrols data
        delete_enrols()
    elif remove_choice == "Faculty":
        # Implement the logic to remove faculty data
        delete_faculty()
    elif remove_choice == "Mentor":
        # Implement the logic to remove mentor data
        delete_mentor()
    elif remove_choice == "Payment":
        # Implement the logic to remove payment data
        delete_payment()
    elif remove_choice == "Scholarship":
        # Implement the logic to remove scholarship data
        delete_scholarship()
    elif remove_choice == "Semester":
        # Implement the logic to remove semester data
        delete_semester()
    elif remove_choice == "Student":
        # Implement the logic to remove student data
        delete_student()
