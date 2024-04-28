import pandas as pd
import streamlit as st
import plotly.express as px
from database import *





def read_student_particular(username):
    view_options = [  "Bank Account Details", "Courses",   "Mentor",  "Scholarship", "Semester", "Student"]
    view_choice = st.selectbox("Select Data Type to View", view_options)
    
    if view_choice == "Student":
            # View data for Student
            result = get_student(username)
            df = pd.DataFrame(result, columns=['SRN', 'Name', 'Address', 'DOB', 'Dept Name', 'CGPA', 'Phone No', 'Gender', 'Email ID'])
            st.dataframe(df)
    elif view_choice == "Semester":
            result_semester = view_all_data_semester()
            df_semester = pd.DataFrame(result_semester, columns=['Semester Number', 'Semester ID', 'Academic year'])
            

            # Create an empty DataFrame to store the results
            df_enrols = pd.DataFrame(columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])

            # Iterate through each "Semester ID"
            for semester_id in df_semester['Semester ID']:
                print("seme",semester_id)
                # Use get_enrols function to retrieve data for each "Semester ID" and append to df_enrols
                result_enrols = get_enrols(semester_id, username)
                # df1 = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
                # st.dataframe(df1)
                df_enrols = pd.concat([df_enrols, pd.DataFrame(result_enrols, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])], ignore_index=True)



            # Merge Semester and Enrols DataFrames on 'Semester ID'
            merged_df = pd.merge(df_semester, df_enrols, on='Semester ID', how='inner')

            # Display the combined DataFrame
            st.dataframe(merged_df)
    elif view_choice == "Bank Account Details":
            result = get_bankaccountdetails_student(username)
            df = pd.DataFrame(result, columns=['Account Number', 'IFSC Code', 'Account Holder Name', 'Student ID'])
            st.dataframe(df)
    
    elif view_choice == "Courses":
            result_semester = view_all_data_semester()
            df_semester = pd.DataFrame(result_semester, columns=['Semester Number', 'Semester ID', 'Academic year'])
            

            # Create an empty DataFrame to store the results
            df_enrols = pd.DataFrame(columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
            #result_courses = view_all_data_courses()
            #df_courses = pd.DataFrame( columns=['Semester ID', 'Course Name'])
            #st.dataframe(df)

            # Iterate through each "Semester ID"
            for semester_id in df_semester['Semester ID']:
                print("seme",semester_id)
                # Use get_enrols function to retrieve data for each "Semester ID" and append to df_enrols
                result_enrols = get_enrols(semester_id, username)
                # df1 = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
                # st.dataframe(df1)
                df_enrols = pd.concat([df_enrols, pd.DataFrame(result_enrols, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])], ignore_index=True)



            # Merge Semester and Enrols DataFrames on 'Semester ID'
            merged_df = pd.merge(df_semester, df_enrols, on='Semester ID', how='inner')

            # Display the combined DataFrame
            #st.dataframe(merged_df)
                        # Extract unique semester IDs from merged_df
            courses_semester_ids = merged_df['Semester ID']

            # Create an empty DataFrame to store course data
            df_courses = pd.DataFrame(columns=['Semester ID', 'Course Name'])
            # Iterate through each unique "Semester ID"
            for semester_id in courses_semester_ids:
                # Use view_all_data_courses function to retrieve course data for each "Semester ID"
                result_courses = get_courses_student(semester_id)
                
                # Append the result to df_courses
                df_courses = pd.concat([df_courses, pd.DataFrame(result_courses, columns=['Semester ID', 'Course Name'])], ignore_index=True)

            # Display the combined DataFrame
            st.dataframe(df_courses)
    
    elif view_choice == "Mentor":
             # View data for Mentor
            result = get_mentor_student(username)
            df = pd.DataFrame(result, columns=['Faculty ID', 'Student ID', 'FAM Date', 'Issues'])
            st.dataframe(df)
            
    
    
    elif view_choice== "Scholarship":
             # View data for Scholarship
            result_scholarship = get_scholarship_student(username)
            #df_schoarship = pd.DataFrame(result, columns=['Scholarship ID',  'Amount', 'Criteria','Name', 'Student ID'])
            #st.dataframe(df)
            #result_semester = view_all_data_semester()
            df_scholarship = pd.DataFrame(result_scholarship, columns=['Scholarship ID',  'Amount', 'Criteria','Name', 'Student ID'])
            

            # Create an empty DataFrame to store the results
            df_payment = pd.DataFrame(columns=['Date', 'Time', 'Status', 'Transaction ID','Scholarship ID'])
            #result_courses = view_all_data_courses()
            #df_courses = pd.DataFrame( columns=['Semester ID', 'Course Name'])
            #st.dataframe(df)

            # Iterate through each "Semester ID"
            for scholarship_id in df_scholarship['Scholarship ID']:
                print("seme",scholarship_id)
                # Use get_enrols function to retrieve data for each "Semester ID" and append to df_enrols
                result_payment = get_payment_student(scholarship_id)
                # df1 = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
                # st.dataframe(df1)
                df_payment = pd.concat([df_payment, pd.DataFrame(result_payment, columns=['Date', 'Time', 'Status', 'Transaction ID','Scholarship ID'])], ignore_index=True)



            # Merge Semester and Enrols DataFrames on 'Semester ID'
            merged_df = pd.merge(df_scholarship, df_payment, on='Scholarship ID', how='inner')
            merged_df['Time'] = merged_df['Time'].astype(str)

            st.dataframe(merged_df)




def student_sem_performance(username):
            result_semester = view_all_data_semester()
            df_semester = pd.DataFrame(result_semester, columns=['Semester Number', 'Semester ID', 'Academic year'])
            

            # Create an empty DataFrame to store the results
            df_enrols = pd.DataFrame(columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])

            # Iterate through each "Semester ID"
            for semester_id in df_semester['Semester ID']:
                print("seme",semester_id)
                # Use get_enrols function to retrieve data for each "Semester ID" and append to df_enrols
                result_enrols = get_enrols(semester_id, username)
                # df1 = pd.DataFrame(result, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])
                # st.dataframe(df1)
                df_enrols = pd.concat([df_enrols, pd.DataFrame(result_enrols, columns=['Semester ID', 'Student ID', 'SGPA', 'Section', 'Attendance'])], ignore_index=True)



            # Merge Semester and Enrols DataFrames on 'Semester ID'
            merged_df = pd.merge(df_semester, df_enrols, on='Semester ID', how='inner')

            # Display the combined DataFrame
            st.dataframe(merged_df)