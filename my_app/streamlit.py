import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
from onglets import pages_2
from onglets import main_pages






def page1() :
  main_pages.main_page()



def page2():

  pages_2.page2()







names = ['John Smith','Rebecca Briggs']
usernames = ['jsmith','rbriggs']
passwords = ['1','456']

hashed_passwords = stauth.Hasher(passwords).generate()

credentials = {"usernames":{}}

for uname,name,pwd in zip(usernames,names,hashed_passwords):
    user_dict = {"name": name, "password": pwd}
    credentials["usernames"].update({uname: user_dict})

authenticator = stauth.Authenticate(credentials,'cookie_name', 'signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')

if authentication_status == True:

    authenticator.logout("logout","main")



    page_names_to_funcs = {

    "Main Page": page1,
    "Page 2": page2
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

elif authentication_status == False:

    st.error('Username/password is incorrect')

elif authentication_status == None:

    st.warning('Please enter your username and password')











