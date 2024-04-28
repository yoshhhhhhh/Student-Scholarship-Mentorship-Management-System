import pandas as pd
import streamlit as st
import plotly.express as px
from database import (view_all_data,view_all_data_admin,view_all_data_student,view_all_data_administer,
                      view_all_data_bankaccountdetails,view_all_data_courses,view_all_data_enrols,
                      view_all_data_faculty,view_all_data_scholarship,view_all_data_semester,
                      view_all_data_mentor ,view_all_data_payment)


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    
    with st.expander("View all Dealers"):
        st.dataframe(df)
    
    with st.expander("Dealer Location"):
        task_df = df['Dealer City'].value_counts().reset_index()
        task_df.columns = ['Dealer City', 'count']  # Rename columns for clarity
        st.dataframe(task_df)
        
        p1 = px.pie(task_df, names='Dealer City', values='count', title='Dealer Location Distribution')
        st.plotly_chart(p1)


def read_admin():
    result = view_all_data_admin()
    df = pd.DataFrame(result, columns=['Admin ID', 'Name', 'Email', 'Phone'])
    
    with st.expander("View all Admins"):
        st.dataframe(df)


def read_administer():
    result = view_all_data_administer()
    df = pd.DataFrame(result, columns=['Administer ID', 'Admin ID', 'Student ID', 'Date'])
    
    with st.expander("View all Administer Records"):
        st.dataframe(df)

def read_bankaccountdetails():
    result = view_all_data_bankaccountdetails()
    df = pd.DataFrame(result, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
    
    with st.expander("View all Bank Account Details"):
        st.dataframe(df)
    
    with st.expander("Bank Account Holder Distribution"):
        task_df = df['Account Holder Name'].value_counts().reset_index()
        task_df.columns = ['Account Holder Name', 'count']  # Rename columns for clarity
        st.dataframe(task_df)
        
        p1 = px.pie(task_df, names='Account Holder Name', values='count', title='Bank Account Holder Distribution')
        st.plotly_chart(p1)
        

def read_course():
    result = view_all_data_courses()
    df = pd.DataFrame(result, columns=['Course Code', 'Course Title', 'Credits'])
    
    with st.expander("View all Courses"):
        st.dataframe(df)
def read_enrols():
    result = view_all_data_enrols()
    df = pd.DataFrame(result, columns=['Student ID', 'Course Code', 'Semester Number', 'Year'])
    
    with st.expander("View all Enrolments"):
        st.dataframe(df)
        
def read_faculty():
    result = view_all_data_faculty()
    df = pd.DataFrame(result, columns=['Faculty ID', 'Name', 'Dept Name'])
    
    with st.expander("View all Faculty"):
        st.dataframe(df)
        
        
def read_mentor():
    result = view_all_data_mentor()
    df = pd.DataFrame(result, columns=['Mentor ID', 'Faculty ID', 'Student ID'])
    
    with st.expander("View all Mentors"):
        st.dataframe(df)
        
def read_payment():
    result = view_all_data_payment()
    df = pd.DataFrame(result, columns=['Payment ID', 'Amount', 'Date', 'Student ID'])
    
    with st.expander("View all Payments"):
        st.dataframe(df)
        
def read_scholarship():
    result = view_all_data_scholarship()
    df = pd.DataFrame(result, columns=['Scholarship ID', 'Amount', 'Criteria', 'Name', 'Student ID'])
    
    with st.expander("View all Scholarships"):
        st.dataframe(df)
        
def read_semester():
    result = view_all_data_semester()
    df = pd.DataFrame(result, columns=['Semester Number', 'Semester ID', 'Academic Year'])
    
    with st.expander("View all Semesters"):
        st.dataframe(df)


def read_student():
    result = view_all_data_student()
    df = pd.DataFrame(result, columns=['SRN', 'Name', 'Address', 'DOB', 'Dept Name', 'CGPA', 'Phone No', 'Gender', 'Email ID'])
    
    with st.expander("View all Students"):
        st.dataframe(df)
        




def front_all_view():
        view_options = ["Admin", "Administer", "Bank Account Details", "Courses", "Enrols", "Faculty", "Mentor", "Payment", "Scholarship", "Semester", "Student"]
        view_choice = st.selectbox("Select Data Type to View", view_options)

        if view_choice == "Admin":
            # View data for Admin
            result = view_all_data_admin()
            df = pd.DataFrame(result, columns=['Admin ID', 'Admin Name', 'Admin Email', 'Admin Password'])
            st.dataframe(df)
        elif view_choice == "Administer":
            # View data for Administer
            result = view_all_data_administer()
            df = pd.DataFrame(result, columns=['Admin ID', 'Student ID', 'Faculty ID', 'Scholarship ID', 'Account Number', 'Transaction ID'])
            st.dataframe(df)

        elif view_choice == "Bank Account Details":
            # View data for Bank Account Details
            result = view_all_data_bankaccountdetails()
            df = pd.DataFrame(result, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
            st.dataframe(df)

        elif view_choice == "Courses":
            # View data for Courses
            result = view_all_data_courses()
            df = pd.DataFrame(result, columns=['Semester ID', 'Course Name'])
            st.dataframe(df)

        elif view_choice == "Enrols":
            # View data for Enrols
            result = view_all_data_enrols()
            df = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
            st.dataframe(df)

        elif view_choice == "Faculty":
            # View data for Faculty
            result = view_all_data_faculty()
            df = pd.DataFrame(result, columns=['Name', 'Faculty ID', 'Address', 'DOB', 'Gender', 'Dept Name'])
            st.dataframe(df)

        elif view_choice == "Mentor":
            # View data for Mentor
            result = view_all_data_mentor()
            df = pd.DataFrame(result, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues'])
            st.dataframe(df)

        elif view_choice == "Payment":
            # View data for Payment
            result = view_all_data_payment()
            df = pd.DataFrame(result, columns=['Date', 'Time', 'Status', 'Transaction ID','Scholarship ID'])
            df['Time'] = df['Time'].astype(str)

            st.dataframe(df)

        elif view_choice == "Scholarship":
            # View data for Scholarship
            result = view_all_data_scholarship()
            df = pd.DataFrame(result, columns=['Scholarship ID',  'Amount', 'Criteria','Name', 'Student ID'])
            st.dataframe(df)

        elif view_choice == "Semester":
            # View data for Semester
            result = view_all_data_semester()
            df = pd.DataFrame(result, columns=['Semester ID', 'Start Date', 'End Date'])
            st.dataframe(df)

        elif view_choice == "Student":
            # View data for Student
            result = view_all_data_student()
            df = pd.DataFrame(result, columns=['SRN', 'Name', 'Address', 'DOB', 'Dept Name', 'CGPA', 'Phone No', 'Gender', 'Email ID'])
            st.dataframe(df)

