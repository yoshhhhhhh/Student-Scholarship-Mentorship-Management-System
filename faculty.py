import pandas as pd
import streamlit as st
import plotly.express as px
from database import *
from student import *
#from create import create_mentor


def read_faculty_particular(username):
    view_options = [   "Mentor",   "Student's Performance","Student Details"]
    view_choice = st.selectbox("Select Data Type to View", view_options)
    
    if view_choice == "Mentor":
            # View data for Student
            result_mentor = get_mentor_faculty(username)
            df = pd.DataFrame(result_mentor, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues'])
            st.dataframe(df)
            
    elif view_choice == "Student's Performance":  
        result_mentor = get_mentor_faculty(username)
        df = pd.DataFrame(result_mentor, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues']) 
            
        # Extract unique student IDs from the DataFrame
        unique_student_ids = df['Student ID'].unique()

        # Display the list of unique student IDs to the user
        selected_student_id = st.selectbox("Select a Student ID", unique_student_ids)

        # Further processing with the selected student ID can be added here
        st.write(f"You selected Student ID: {selected_student_id}")
        student_sem_performance(selected_student_id)
        
        

         # Add more conditions for other view options if needed
    
    elif view_choice ==  "Student Details":
        result_mentor = get_mentor_faculty(username)
        df = pd.DataFrame(result_mentor, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues']) 
            
        # Extract unique student IDs from the DataFrame
        unique_student_ids = df['Student ID'].unique()

        # Display the list of unique student IDs to the user
        selected_student_id = st.selectbox("Select a Student ID", unique_student_ids)
        result_student = get_student(selected_student_id)
        df = pd.DataFrame(result_student, columns=['SRN', 'Name', 'Address', 'DOB', 'Dept Name', 'CGPA', 'Phone No', 'Gender', 'Email ID'])
        st.dataframe(df)
                   

def faculty_create_mentor( username ):
    result_mentor = get_mentor_faculty(username)
    df = pd.DataFrame(result_mentor, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues']) 
            
        # Extract unique student IDs from the DataFrame
    unique_student_ids = df['Student ID'].unique()

        # Display the list of unique student IDs to the user
    selected_student_id = st.selectbox("Select a Student ID", unique_student_ids)
    col1, col2 = st.columns(2)
    with col1:
        #faculty_id = username
        st.text_input("Faculty ID:", username, key="faculty_id", disabled=True)
        
        student_id = selected_student_id
        fam_date = st.date_input("Family Date:")
    with col2:
        issues = st.text_area("Issues:")
    if st.button("Add Mentor"):
        add_data_mentor(username, student_id, fam_date, issues)
        st.success("Successfully added Mentor entry")
        
        
        
def faculty_mentor_edit(username):
    result_mentor = get_mentor_faculty(username)
    df = pd.DataFrame(result_mentor, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues']) 
            
        # Extract unique student IDs from the DataFrame
    unique_student_ids = df['Student ID'].unique()

        # Display the list of unique student IDs to the user
    selected_student_id = st.selectbox("Select a Student ID and date", unique_student_ids)
    # Filter the DataFrame based on the selected student ID
    filtered_df = df[df['Student ID'] == selected_student_id]

    # Extract unique FAM Date values for the selected student ID
    unique_fam_dates = filtered_df['FAM Date'].unique()

    # Display the list of unique FAM Date values to the user
    selected_fam_date = st.selectbox("Select a FAM Date", unique_fam_dates)
    selected_result = get_mentor_admin(username,selected_student_id,selected_fam_date)
    
    if selected_result:
        # mentor_id = selected_result[0][0]
        # student_id=selected_result[0][1]
        # fam_date=selected_result[0][2]
        issues=selected_result[0][3]
    col1, col2 = st.columns(2)
    with col1:
        #faculty_id = username
        st.text_input("Faculty ID:", username, key="faculty_id", disabled=True)
        st.text_input("Student ID:", selected_student_id, key="student_id", disabled=True)
        #student_id = selected_student_id
        #fam_date = st.date_input("Fam Date:")
    with col2:
        new_fam_date = st.text_input("FAM Date:", selected_fam_date)
        new_issues = st.text_input("Issues:",issues)
    

    if st.button("Update Mentor"):
            edit_mentor_data(username, selected_student_id, new_fam_date, new_issues, username, selected_student_id,selected_fam_date)
            st.success("Successfully updated Mentor: {} to {}".format(username, username))

    result_f = get_mentor_student(selected_student_id)
    df4 = pd.DataFrame(result_f, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues'])
    with st.expander("Updated Mentor Details"):
        st.dataframe(df4)