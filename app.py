import streamlit as st
from create import *
from read import *
from update import *
import yaml
from delete import *
from database import *
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
from student import *
from faculty import *
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
#print("Username:", username)

# Initialize user_type with a default value
user_type = 'default_user_type'

def main():
    global user_type  # Declare user_type as global to modify the global variable

    st.title("University Scholarship and Mentor Management")
    print("Before conditional check - Username:", username)
    if 'credentials' in config and 'usernames' in config['credentials'] and username in config['credentials']['usernames']:
        # Retrieve the specific username with case sensitivity
        user_type = config['credentials']['usernames'].get(username, {}).get('user_type', 'default_user_type')
        #print("Username:", username)
        upper_user = username.upper()
        #print("Uusername:", upper_user)
    else:
        print(".")
    if authentication_status:
        #authenticator.logout('Logout', 'main')
        
        if  user_type=='Student':
            menu = ["Dashboard",  "View"]
            #upper_user=username
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
                #read()
                #read_student()
                read_student_particular(upper_user)
                
            elif choice == "Edit":
                st.subheader("Update created tasks")
                result= view_all_data_timer()
                df = pd.DataFrame(result, columns=['ID','EVentname','Eventime'])
                df['Eventime'] = df['Eventime'].astype(str)

                st.dataframe(df)
                #update()
            elif choice == "Remove":
                st.subheader("Delete created tasks")
                delete()
            else:
                st.subheader("About tasks")

        # User priviledges on frontend after login for Admin
        if  user_type=='Admin':
            menu = ["Dashboard", "Add", "View", "Edit", "Remove"]
            choice = st.sidebar.selectbox("Menu", menu)
            create_table()
            if choice=="Dashboard":
                st.subheader(f'Welcome {name} ({user_type})')
                authenticator.logout('Logout', 'main')
            elif choice == "Add":
                st.subheader("Enter Admin Details:")
                add_options = ["Admin", "Administer", "Bank Account Details", "Courses", "Enrols", "Faculty", "Mentor", "Payment", "Scholarship", "Semester", "Student"]
                add_choice = st.selectbox("Select Data Type to Add", add_options)

                if add_choice == "Admin":
                    #create()
                    create_admin()
                elif add_choice =="Adminster":
                    create_administer()
                elif add_choice == "Bank Account Details":
                    create_bankaccountdetails()
                elif add_choice ==  "Courses":
                    create_courses()
                elif add_choice =="Enrols":
                    create_enrols()
                elif add_choice=="Faculty":
                    create_faculty()
                elif add_choice=="Mentor":
                    create_mentor()
                elif add_choice ==  "Payment":
                    create_payment()
                elif add_choice ==  "Scholarship":
                    create_scholarship()
                elif add_choice == "Semester":
                    create_semester()
                elif add_choice ==  "Student":
                    create_student()
            elif choice == "View":
                st.subheader("View create rtnrt tasks")
                #read()
                front_all_view()
                
            elif choice == "Edit":
                st.subheader("Update created tasks")
                #update()
                front_all_update()
            elif choice == "Remove":
                st.subheader("Delete created tasks")
                #delete()
                front_remove()
            else:
                st.subheader("About tasks")

        # User priviledges on frontend after login for Faculty
        if user_type=='Faculty':
            menu = ["Dashboard", "View",  "Add", "Edit"]
            choice = st.sidebar.selectbox("Menu", menu)
            create_table()
            if choice=="Dashboard":
                st.subheader(f'Welcome {name} ({user_type})')
                authenticator.logout('Logout', 'main')
            elif choice == "Add":
                st.subheader("Enter Faculty Details:")
                #create()
                faculty_create_mentor( upper_user )
            elif choice == "View":
                st.subheader("View created tasks")
                read_faculty_particular(upper_user)
            elif choice == "Edit":
                st.subheader("Update created tasks")
                #update()
                faculty_mentor_edit(username)
            elif choice == "Remove":
                st.subheader("Delete created tasks")
                delete()
            else:
                st.subheader("About tasks")
                
        # menu = ["Addggg", "View", "Edit", "Remove"]
        # choice = st.sidebar.selectbox("Menu", menu)

        # create_table()
        # if choice == "Add":
        #     st.subheader("Enter Dealer Details:")
        #     create()

        # elif choice == "View":
        #     st.subheader("View created tasks")
        #     read()

        # elif choice == "Edit":
        #     st.subheader("Update created tasks")
        #     update()

        # elif choice == "Remove":
        #     st.subheader("Delete created tasks")
        #     delete()

        # else:
        #     st.subheader("About tasks")
        
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
        
    
        

        
    


if __name__ == '__main__':
    main()
    



