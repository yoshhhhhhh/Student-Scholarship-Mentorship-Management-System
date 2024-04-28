import streamlit as st
import streamlit_authenticator as stauth
from create import create
from read import read
from update import update
from delete import delete
from database import create_table, close
import yaml
from yaml.loader import SafeLoader

st.title("PES University")
st.subheader("Scholarship and mentorship Management")

is_login = False # Variable to check if the user has logged in

# Login (Check user credentials)
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    with open('users.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    user_type = config['credentials']['usernames'].get(username, {}).get('type', None)
    is_login = True
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# User priviledges on frontend after login for student
if is_login and user_type=='Student':
    menu = ["Dashboard", "Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice=="Dashboard":
        st.subheader(f'Welcome {name} ({user_type})')
        authenticator.logout('Logout', 'main')
    elif choice == "Add":
        st.subheader("Enter Student Details:")
        create()
    elif choice == "View":
        st.subheader("View created tasks")
        read()
    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()
    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()
    else:
        st.subheader("About tasks")

# User priviledges on frontend after login for Admin
if is_login and user_type=='Admin':
    menu = ["Dashboard", "Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice=="Dashboard":
        st.subheader(f'Welcome {name} ({user_type})')
        authenticator.logout('Logout', 'main')
    elif choice == "Add":
        st.subheader("Enter Admin Details:")
        create()
    elif choice == "View":
        st.subheader("View created tasks")
        read()
    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()
    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()
    else:
        st.subheader("About tasks")

# User priviledges on frontend after login for Faculty
if is_login and user_type=='Faculty':
    menu = ["Dashboard", "Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice=="Dashboard":
        st.subheader(f'Welcome {name} ({user_type})')
        authenticator.logout('Logout', 'main')
    elif choice == "Add":
        st.subheader("Enter Faculty Details:")
        create()
    elif choice == "View":
        st.subheader("View created tasks")
        read()
    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()
    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()
    else:
        st.subheader("About tasks")
        
        
        #################################
        
        
        
        

def update_student():
    result = view_all_data_student()
    if not result:
        st.warning("No student data available.")
        return

    # Extract column names from the first row of the result
    columns = [desc[0] for desc in c.description]
    df = pd.DataFrame(result, columns=columns)

    with st.expander("Current Students"):
        st.dataframe(df)

    list_of_students = [i[0] for i in view_only_student_ids()]
    selected_student = st.selectbox("Student to Edit", list_of_students)
    selected_result = get_student(selected_student)

    if selected_result:
        # Use the same approach to get column names dynamically
        selected_columns = [desc[0] for desc in c.description]
        selected_dict = dict(zip(selected_columns, selected_result[0]))

        if 'SRN' in selected_dict:  # Assuming 'SRN' is always present
            # Layout for updating student details
            col1, col2 = st.columns(2)
            with col1:
                for col_name in selected_columns[:len(selected_columns) // 2]:
                    # Display the existing values
                    st.text_input(f"{col_name}:", selected_dict[col_name], key=f"{col_name}_input")
            with col2:
                for col_name in selected_columns[len(selected_columns) // 2:]:
                    # Display the existing values
                    st.text_input(f"{col_name}:", selected_dict[col_name], key=f"{col_name}_input")

            if st.button("Update Student"):
                # Get updated values
                updated_values = {col_name: st.session_state[f"{col_name}_input"] for col_name in selected_columns}
                # Remove SRN from updated_values, as it's already included
                updated_values.pop('SRN', None)

                # Get the intersection of keys in updated_values and expected parameters of edit_student_data
                valid_keys = set(updated_values.keys()) & {'new_SRN', 'new_Name', 'new_Address', 'new_DOB', 'new_Dept_name', 'new_CGPA', 'new_Phone_no', 'new_Gender', 'new_Email_id'}

                # Pass only the valid keys to the edit_student_data function
                edit_student_data(**{key: updated_values[key] for key in valid_keys}, SRN=selected_student)

                st.success(f"Successfully updated Student ID: {selected_student}")
