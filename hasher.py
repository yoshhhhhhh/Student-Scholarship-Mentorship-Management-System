import streamlit_authenticator as stauth
hashed_passwords = stauth.Hasher(['abc', 'def','ghi']).generate()
print(hashed_passwords)