import mysql.connector
from datetime import timedelta

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="<your password>",
    database="scholarship_mentor"
)

c = mydb.cursor()


# c.execute("CREATE DATABASE IF NOT EXISTS e_bike")

def create_table():
    #c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
              #'dealer_street TEXT)')
    c.execute('''CREATE TABLE IF NOT EXISTS admin (
                  admin_id varchar(30) NOT NULL,
                  username varchar(30) DEFAULT NULL,
                  password varchar(45) NOT NULL,
                  phone_no int DEFAULT NULL,
                  PRIMARY KEY (admin_id),
                  UNIQUE KEY phone_no_UNIQUE (phone_no)
                  )''')
      # Create 'administer' table
    c.execute('''CREATE TABLE IF NOT EXISTS administer (
                  admin_id varchar(30) NOT NULL,
                  student_id varchar(20) NOT NULL,
                  faculty_id varchar(30) NOT NULL,
                  scholarship_id varchar(20) NOT NULL,
                  account_number varchar(30) NOT NULL,
                  transaction_id varchar(30) NOT NULL,
                  PRIMARY KEY (admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id),
                  KEY student_minister_idx (student_id),
                  KEY faculty_minister_idx (faculty_id),
                  KEY scholarship_minister_idx (scholarship_id),
                  KEY account_minister_idx (account_number),
                  KEY transaction_minister_idx (transaction_id),
                  CONSTRAINT account_minister FOREIGN KEY (account_number) REFERENCES bankaccountdetails (account_number) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT admin_minister FOREIGN KEY (admin_id) REFERENCES admin (admin_id) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT faculty_minister FOREIGN KEY (faculty_id) REFERENCES faculty (faculty_id) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT scholarship_minister FOREIGN KEY (scholarship_id) REFERENCES scholarship (scholarship_id) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT student_minister FOREIGN KEY (student_id) REFERENCES student (SRN) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT transaction_minister FOREIGN KEY (transaction_id) REFERENCES payment (transaction_id) ON DELETE CASCADE ON UPDATE CASCADE
                   ) ''')
    c.execute('''CREATE TABLE IF NOT EXISTS bankaccountdetails (
                  account_number varchar(30) NOT NULL,
                  ifsc_code varchar(30) NOT NULL,
                  acc_holder_name varchar(40) NOT NULL,
                  student_id varchar(20) NOT NULL,
                  PRIMARY KEY (account_number),
                  KEY student_id_idx (student_id),
                  CONSTRAINT studentid FOREIGN KEY (student_id) REFERENCES student (SRN) ON DELETE CASCADE ON UPDATE CASCADE
                   ) ''')
    # Create 'courses' table
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
                  sem_id varchar(10) NOT NULL,
                  course_name varchar(30) NOT NULL,
                  PRIMARY KEY (sem_id, course_name),
                  CONSTRAINT semid_course FOREIGN KEY (sem_id) REFERENCES semester (sem_id) ON DELETE CASCADE ON UPDATE CASCADE
                   ) ''')

     # Create 'enrols' table
    c.execute('''CREATE TABLE IF NOT EXISTS enrols (
                  sem_id varchar(10) NOT NULL,
                  SRN varchar(20) NOT NULL,
                  SGPA float NOT NULL,
                  section varchar(1) NOT NULL,
                  attendance decimal(6,0) DEFAULT NULL,
                  PRIMARY KEY (sem_id, SRN),
                  KEY SRN_idx (SRN),
                  CONSTRAINT sem_id FOREIGN KEY (sem_id) REFERENCES semester (sem_id) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT SRN FOREIGN KEY (SRN) REFERENCES student (SRN) ON DELETE CASCADE ON UPDATE CASCADE
                  ) ''')
    # Create 'faculty' table
    c.execute('''CREATE TABLE IF NOT EXISTS faculty (
                  name varchar(30) NOT NULL,
                  faculty_id varchar(20) NOT NULL,
                  address varchar(45) NOT NULL,
                  dob date DEFAULT NULL,
                  gender varchar(10) NOT NULL,
                  dept_name varchar(30) NOT NULL,
                  PRIMARY KEY (faculty_id)
                  ) ''')
     # Create 'mentor' table
    c.execute('''CREATE TABLE IF NOT EXISTS mentor (
                  faculty_id varchar(30) NOT NULL,
                  student_id varchar(20) NOT NULL,
                  fam_date date DEFAULT NULL,
                  issues varchar(55) DEFAULT NULL,
                  PRIMARY KEY (faculty_id, student_id),
                  KEY studentidmentor_idx (student_id),
                  CONSTRAINT facultyidmetor FOREIGN KEY (faculty_id) REFERENCES faculty (faculty_id) ON DELETE CASCADE ON UPDATE CASCADE,
                  CONSTRAINT studentidmentor FOREIGN KEY (student_id) REFERENCES student (SRN) ON DELETE CASCADE ON UPDATE CASCADE
                   ) ''')
    # Create 'payment' table
    c.execute('''CREATE TABLE IF NOT EXISTS payment(
                    `date` date NOT NULL,
                    `time` time DEFAULT NULL,
                    `status` varchar(30) NOT NULL,
                    `transaction_id` varchar(30) NOT NULL,
                    `scholarship_id` varchar(20) DEFAULT NULL,
                    PRIMARY KEY (`transaction_id`),
                    KEY `fk_payment_scholarship` (`scholarship_id`),
                    CONSTRAINT `fk_payment_scholarship` FOREIGN KEY (`scholarship_id`) REFERENCES `scholarship` (`scholarship_id`)
                    ) ''')
    # Create 'scholarship' table
    c.execute('''CREATE TABLE IF NOT EXISTS scholarship (
                  scholarship_id varchar(20) NOT NULL,
                  amount int NOT NULL,
                  criteria varchar(20) DEFAULT NULL,
                  name varchar(20) NOT NULL,
                  student_id varchar(20) NOT NULL,
                  PRIMARY KEY (scholarship_id),
                  KEY student_id_idx (student_id),
                  CONSTRAINT student_id FOREIGN KEY (student_id) REFERENCES student (SRN) ON DELETE CASCADE ON UPDATE CASCADE
                     ) ''')
    # Create 'semester' table
    c.execute('''CREATE TABLE IF NOT EXISTS semester (
                  sem_number int NOT NULL,
                  sem_id varchar(10) NOT NULL,
                  academic_year varchar(10) NOT NULL,
                  PRIMARY KEY (sem_id)
                  ) ''')
     # Create 'student' table
    c.execute('''CREATE TABLE IF NOT EXISTS student (
                  SRN varchar(20) NOT NULL,
                  Name varchar(25) NOT NULL,
                  Address varchar(45) DEFAULT NULL,
                  DOB date NOT NULL,
                  Dept_name varchar(30) NOT NULL,
                  CGPA float NOT NULL,
                  Phone_no int DEFAULT NULL,
                  Gender varchar(6) DEFAULT NULL,
                  Email_id varchar(45)
                  )''')









def add_data():
    
    mydb.commit()
def add_data_admin(admin_id, username, password, phone_no):
    c.execute('INSERT INTO admin(admin_id, username, password, phone_no) VALUES (%s, %s, %s, %s)',
              (admin_id, username, password, phone_no))
    mydb.commit()

def add_data_administer(admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id):
    c.execute('INSERT INTO administer(admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id) VALUES (%s, %s, %s, %s, %s, %s)',
              (admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id))
    mydb.commit()

def add_data_bankaccountdetails(account_number, ifsc_code, acc_holder_name, student_id):
    c.execute('INSERT INTO bankaccountdetails(account_number, ifsc_code, acc_holder_name, student_id) VALUES (%s, %s, %s, %s)',
              (account_number, ifsc_code, acc_holder_name, student_id))
    mydb.commit()

def add_data_courses(sem_id, course_name):
    c.execute('INSERT INTO courses(sem_id, course_name) VALUES (%s, %s)',
              (sem_id, course_name))
    mydb.commit()

def add_data_enrols(sem_id, SRN, SGPA, section, attendance):
    c.execute('INSERT INTO enrols(sem_id, SRN, SGPA, section, attendance) VALUES (%s, %s, %s, %s, %s)',
              (sem_id, SRN, SGPA, section, attendance))
    mydb.commit()

def add_data_faculty(name, faculty_id, address, dob, gender, dept_name):
    c.execute('INSERT INTO faculty(name, faculty_id, address, dob, gender, dept_name) VALUES (%s, %s, %s, %s, %s, %s)',
              (name, faculty_id, address, dob, gender, dept_name))
    mydb.commit()

def add_data_mentor(faculty_id, student_id, fam_date, issues):
    c.execute('INSERT INTO mentor(faculty_id, student_id, fam_date, issues) VALUES (%s, %s, %s, %s)',
              (faculty_id, student_id, fam_date, issues))
    mydb.commit()

def add_data_payment(date, time, status, transaction_id,scholarship_id):
    c.execute('INSERT INTO payment(date, time, status, transaction_id,scholarship_id) VALUES (%s, %s, %s, %s,%s)',
              (date, time, status, transaction_id,scholarship_id))
    mydb.commit()

def add_data_scholarship(scholarship_id, amount, criteria, name, student_id):
    c.execute('INSERT INTO scholarship(scholarship_id, amount, criteria, name, student_id) VALUES (%s, %s, %s, %s, %s)',
              (scholarship_id, amount, criteria, name, student_id))
    mydb.commit()

def add_data_semester(sem_number, sem_id, academic_year):
    c.execute('INSERT INTO semester(sem_number, sem_id, academic_year) VALUES (%s, %s, %s)',
              (sem_number, sem_id, academic_year))
    mydb.commit()

def add_data_student(SRN, Name, Address, DOB, Dept_name, CGPA, Phone_no, Gender, Email_id):
    c.execute('INSERT INTO student(SRN, Name, Address, DOB, Dept_name, CGPA, Phone_no, Gender, Email_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
              (SRN, Name, Address, DOB, Dept_name, CGPA, Phone_no, Gender, Email_id))
    mydb.commit()



def view_all_data():
    c.execute('SELECT * FROM DEALER')
    data = c.fetchall()
    return data
def view_all_data_admin():
    c.execute('SELECT * FROM admin')
    data = c.fetchall()
    return data

def view_all_data_administer():
    c.execute('SELECT * FROM administer')
    data = c.fetchall()
    return data

def view_all_data_bankaccountdetails():
    c.execute('SELECT * FROM bankaccountdetails')
    data = c.fetchall()
    return data

def view_all_data_courses():
    c.execute('SELECT * FROM courses')
    data = c.fetchall()
    return data

def view_all_data_enrols():
    c.execute('SELECT * FROM enrols')
    data = c.fetchall()
    return data

def view_all_data_faculty():
    c.execute('SELECT * FROM faculty')
    data = c.fetchall()
    return data

def view_all_data_mentor():
    c.execute('SELECT * FROM mentor')
    data = c.fetchall()
    return data

def view_all_data_payment():
    c.execute('SELECT * FROM payment')
    data = c.fetchall()
    return data

def view_all_data_scholarship():
    c.execute('SELECT * FROM scholarship')
    data = c.fetchall()
    return data

def view_all_data_semester():
    c.execute('SELECT * FROM semester')
    data = c.fetchall()
    return data

def view_all_data_student():
    c.execute('SELECT * FROM student')
    data = c.fetchall()
    return data


def view_only_dealer_names():
    c.execute('SELECT dealer_name FROM DEALER')
    data = c.fetchall()
    return data

# Placeholder function, adapt based on your actual database structure
def view_only_admin_ids():
    c.execute('SELECT admin_id FROM admin')
    data = c.fetchall()
    return data

def view_only_administer_ids():
    c.execute('SELECT admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id FROM administer')
    data = c.fetchall()
    return data

def view_only_bankaccountdetails_ids():
    c.execute('SELECT account_number FROM bankaccountdetails')
    data = c.fetchall()
    return data

def view_only_courses_ids():
    c.execute('SELECT sem_id, course_name FROM courses')
    data = c.fetchall()
    return data

def view_only_enrols_ids():
    c.execute('SELECT sem_id, SRN FROM enrols')
    data = c.fetchall()
    return data

def view_only_faculty_ids():
    c.execute('SELECT faculty_id FROM faculty')
    data = c.fetchall()
    return data

def view_only_mentor_ids():
    c.execute('SELECT faculty_id, student_id FROM mentor')
    data = c.fetchall()
    return data
def view_only_mentor_admin_ids():
    c.execute('SELECT faculty_id, student_id ,fam_date FROM mentor')
    data = c.fetchall()
    return data

def view_only_payment_ids():
    c.execute('SELECT transaction_id FROM payment')
    data = c.fetchall()
    return data

def view_only_scholarship_ids():
    c.execute('SELECT scholarship_id FROM scholarship')
    data = c.fetchall()
    return data

def view_only_semester_ids():
    c.execute('SELECT sem_id FROM semester')
    data = c.fetchall()
    return data

def view_only_student_ids():
    c.execute('SELECT SRN FROM student')
    data = c.fetchall()
    return data


def get_dealer(dealer_name):
    c.execute('SELECT * FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
    data = c.fetchall()
    return data
#ge functions for mydatabse
def get_admin(admin_id):
    c.execute('SELECT * FROM admin WHERE admin_id=%s', (admin_id,))
    data = c.fetchall()
    return data

def get_administer(admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id):
    c.execute('SELECT * FROM administer WHERE admin_id=%s AND student_id=%s AND faculty_id=%s AND scholarship_id=%s AND account_number=%s AND transaction_id=%s',
              (admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id))
    data = c.fetchall()
    return data

def get_bankaccountdetails(account_number):
    c.execute('SELECT * FROM bankaccountdetails WHERE account_number=%s', (account_number,))
    data = c.fetchall()
    return data

def get_courses(sem_id, course_name):
    c.execute('SELECT * FROM courses WHERE sem_id=%s AND course_name=%s', (sem_id, course_name))
    data = c.fetchall()
    return data

def get_enrols(sem_id, SRN):
    c.execute('SELECT * FROM enrols WHERE sem_id=%s AND SRN=%s', (sem_id, SRN))
    data = c.fetchall()
    return data

def get_faculty(faculty_id):
    c.execute('SELECT * FROM faculty WHERE faculty_id=%s', (faculty_id,))
    data = c.fetchall()
    return data

def get_mentor(faculty_id, student_id):
    c.execute('SELECT * FROM mentor WHERE faculty_id=%s AND student_id=%s', (faculty_id, student_id))
    data = c.fetchall()
    return data

def get_payment(transaction_id):
    c.execute('SELECT * FROM payment WHERE transaction_id=%s', (transaction_id,))
    data = c.fetchall()
    return data

def get_scholarship(scholarship_id):
    c.execute('SELECT * FROM scholarship WHERE scholarship_id=%s', (scholarship_id,))
    data = c.fetchall()
    return data

def get_semester(sem_id):
    c.execute('SELECT * FROM semester WHERE sem_id=%s', (sem_id,))
    data = c.fetchall()
    return data

def get_student(SRN):
    c.execute('SELECT * FROM student WHERE SRN=%s', (SRN,))
    data = c.fetchall()
    return data



def edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street):
    c.execute("UPDATE DEALER SET dealer_id=%s, dealer_name=%s, dealer_city=%s, dealer_pin=%s, dealer_street=%s WHERE "
              "dealer_id=%s and dealer_name=%s and dealer_city=%s and dealer_pin=%s and dealer_street=%s", (new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
    mydb.commit()
    data = c.fetchall()
    return data
#edit function according to my database
def edit_admin_data(new_admin_id, new_username, new_password, new_phone_no, admin_id):
    c.execute("UPDATE admin SET admin_id=%s, username=%s, password=%s, phone_no=%s WHERE admin_id=%s",
              (new_admin_id, new_username, new_password, new_phone_no, admin_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_administer_data(new_admin_id, new_student_id, new_faculty_id, new_scholarship_id, new_account_number, new_transaction_id,
                         admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id):
    c.execute("UPDATE administer SET admin_id=%s, student_id=%s, faculty_id=%s, scholarship_id=%s, account_number=%s, transaction_id=%s "
              "WHERE admin_id=%s AND student_id=%s AND faculty_id=%s AND scholarship_id=%s AND account_number=%s AND transaction_id=%s",
              (new_admin_id, new_student_id, new_faculty_id, new_scholarship_id, new_account_number, new_transaction_id,
               admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_bankaccountdetails_data(new_account_number, new_ifsc_code, new_acc_holder_name, new_student_id, account_number):
    c.execute("UPDATE bankaccountdetails SET account_number=%s, ifsc_code=%s, acc_holder_name=%s, student_id=%s "
              "WHERE account_number=%s",
              (new_account_number, new_ifsc_code, new_acc_holder_name, new_student_id, account_number))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_courses_data(new_sem_id, new_course_name, sem_id, course_name):
    c.execute("UPDATE courses SET sem_id=%s, course_name=%s WHERE sem_id=%s AND course_name=%s",
              (new_sem_id, new_course_name, sem_id, course_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_enrols_data(new_sem_id, new_SRN, new_SGPA, new_section, new_attendance, sem_id, SRN):
    c.execute("UPDATE enrols SET sem_id=%s, SRN=%s, SGPA=%s, section=%s, attendance=%s WHERE sem_id=%s AND SRN=%s",
              (new_sem_id, new_SRN, new_SGPA, new_section, new_attendance, sem_id, SRN))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_faculty_data(new_name, new_faculty_id, new_address, new_dob, new_gender, new_dept_name, faculty_id):
    c.execute("UPDATE faculty SET name=%s, faculty_id=%s, address=%s, dob=%s, gender=%s, dept_name=%s WHERE faculty_id=%s",
              (new_name, new_faculty_id, new_address, new_dob, new_gender, new_dept_name, faculty_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_mentor_data(new_faculty_id, new_student_id, new_fam_date, new_issues, faculty_id, student_id,fam_date):
    c.execute("UPDATE mentor SET faculty_id=%s, student_id=%s, fam_date=%s, issues=%s WHERE faculty_id=%s AND student_id=%s AND fam_date=%s",
              (new_faculty_id, new_student_id, new_fam_date, new_issues, faculty_id, student_id,fam_date))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_payment_data(new_date, new_time, new_status, new_transaction_id,new_scholarship_id, transaction_id):
    c.execute("UPDATE payment SET date=%s, time=%s, status=%s, transaction_id=%s, scholarship_id=%s WHERE transaction_id=%s",
              (new_date, new_time, new_status, new_transaction_id,new_scholarship_id, transaction_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_scholarship_data(new_scholarship_id, new_amount, new_criteria, new_name, new_student_id, scholarship_id):
    c.execute("UPDATE scholarship SET scholarship_id=%s, amount=%s, criteria=%s, name=%s, student_id=%s WHERE scholarship_id=%s",
              (new_scholarship_id, new_amount, new_criteria, new_name, new_student_id, scholarship_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_semester_data(new_sem_number, new_sem_id, new_academic_year, sem_id):
    c.execute("UPDATE semester SET sem_number=%s, sem_id=%s, academic_year=%s WHERE sem_id=%s",
              (new_sem_number, new_sem_id, new_academic_year, sem_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_student_data(new_SRN, new_Name, new_Address, new_DOB, new_Dept_name, new_CGPA, new_Phone_no, new_Gender, new_Email_id, SRN):
    c.execute("UPDATE student SET SRN=%s, Name=%s, Address=%s, DOB=%s, Dept_name=%s, CGPA=%s, Phone_no=%s, Gender=%s, Email_id=%s WHERE SRN=%s",
              (new_SRN, new_Name, new_Address, new_DOB, new_Dept_name, new_CGPA, new_Phone_no, new_Gender, new_Email_id, SRN))
    mydb.commit()
    data = c.fetchall()
    return data



def delete_data(dealer_name):
    c.execute('DELETE FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
    mydb.commit()
    
#delete function acccording to my database
def delete_admin_data(admin_id):
    c.execute('DELETE FROM admin WHERE admin_id=%s', (admin_id,))
    mydb.commit()

def delete_administer_data(admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id):
    c.execute('DELETE FROM administer WHERE admin_id=%s AND student_id=%s AND faculty_id=%s AND scholarship_id=%s AND account_number=%s AND transaction_id=%s',
              (admin_id, student_id, faculty_id, scholarship_id, account_number, transaction_id))
    mydb.commit()

def delete_bankaccountdetails_data(account_number):
    c.execute('DELETE FROM bankaccountdetails WHERE account_number=%s', (account_number,))
    mydb.commit()

def delete_courses_data(sem_id, course_name):
    c.execute('DELETE FROM courses WHERE sem_id=%s AND course_name=%s', (sem_id, course_name))
    mydb.commit()

def delete_enrols_data(sem_id, SRN):
    c.execute('DELETE FROM enrols WHERE sem_id=%s AND SRN=%s', (sem_id, SRN))
    mydb.commit()

def delete_faculty_data(faculty_id):
    c.execute('DELETE FROM faculty WHERE faculty_id=%s', (faculty_id,))
    mydb.commit()

def delete_mentor_data(faculty_id, student_id):
    c.execute('DELETE FROM mentor WHERE faculty_id=%s AND student_id=%s', (faculty_id, student_id))
    mydb.commit()

def delete_payment_data(transaction_id):
    c.execute('DELETE FROM payment WHERE transaction_id=%s', (transaction_id,))
    mydb.commit()

def delete_scholarship_data(scholarship_id):
    c.execute('DELETE FROM scholarship WHERE scholarship_id=%s', (scholarship_id,))
    mydb.commit()

def delete_semester_data(sem_id):
    c.execute('DELETE FROM semester WHERE sem_id=%s', (sem_id,))
    mydb.commit()

def delete_student_data(SRN):
    c.execute('DELETE FROM student WHERE SRN=%s', (SRN,))
    mydb.commit()


def close():
    c.close()
    mydb.close()



'''
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, dealer_street TEXT)')

def add_data(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street):
    c.execute('INSERT INTO DEALER(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street) VALUES (%s,%s,%s,%s,%s)',(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM DEALER')
    data = c.fetchall()
    return data

def view_only_dealer_names():
    c.execute('SELECT dealer_name FROM DEALER')
    data = c.fetchall()
    return data

def get_dealer(dealer_name):
    c.execute('SELECT * FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
    data = c.fetchall()
    return data

def edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street):
    c.execute("UPDATE DEALER SET dealer_id=%s, dealer_name=%s, dealer_city=%s, dealer_pin=%s, dealer_street=%s WHERE dealer_id=%s and dealer_name=%s and dealer_city=%s and dealer_pin=%s and dealer_street=%s", (new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data(dealer_name):
    c.execute('DELETE FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
    mydb.commit()
    

'''


def get_mentor_admin(faculty_id, student_id,fam_date):
    c.execute('SELECT * FROM mentor WHERE faculty_id=%s AND student_id=%s AND fam_date=%s', (faculty_id, student_id,fam_date))
    data = c.fetchall()
    return data
######STUDENT

def get_bankaccountdetails_student(student_id):
    c.execute('SELECT * FROM bankaccountdetails WHERE student_id=%s', (student_id,))
    data = c.fetchall()
    return data

def get_courses_student(sem_id):
    c.execute('SELECT * FROM courses WHERE sem_id=%s ', (sem_id,))
    data = c.fetchall()
    return data


def get_mentor_student( student_id):
    c.execute('SELECT * FROM mentor WHERE  student_id=%s', ( student_id,))
    data = c.fetchall()
    return data

def get_scholarship_student(student_id):
    c.execute('SELECT * FROM scholarship WHERE student_id=%s', (student_id,))
    data = c.fetchall()
    return data

# def get_payment_student(scholarship_id):
#     c.execute('SELECT * FROM payment WHERE scholarship_id=%s', (scholarship_id,))
#     data = c.fetchall()
#     return data
def get_payment_student(scholarship_id):
    c.execute('SELECT * FROM payment WHERE scholarship_id=%s', (scholarship_id,))
    data = c.fetchall()

    # Convert 'Duration' values to strings
    for i, row in enumerate(data):
        if isinstance(row[2], timedelta):  # Assuming 'Duration' is at index 2
            data[i] = (row[0], row[1], str(row[2]), row[3], row[4])  # Assuming 'Duration' is at index 2

    return data




##########Faculty

def get_mentor_faculty(faculty_id):
    c.execute('SELECT * FROM mentor WHERE faculty_id=%s ', (faculty_id, ))
    data = c.fetchall()
    return data




def view_all_data_timer():
    c.execute('SELECT * FROM timer')
    data = c.fetchall()
    return data