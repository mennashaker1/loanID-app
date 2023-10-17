import pickle 
from pathlib import Path

import streamlit_authenticator as stauth
import streamlit as st


# --- User Authentication ---

names = ["Menna Shaker", "Abdelrahman Akmal"]
usernames = ["mshaker", "aakmal"]

#Load hashed passwords

file_path = Path("Streamlit Authenticator Test").parent / "hashed_passwords.pkl"
with file_path.open("rb") as file:
	hashed_passwords = pickle.load(file)

credentials = {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                },
            usernames[1]:{
                "name":names[1],
                "password":hashed_passwords[1]
                }            
            }
        }

authenticator = stauth.Authenticate(credentials, "codes", "abcdef", cookie_expiry_days = 0)

name, authentication_status, username = authenticator.login("Login", "main")
authenticator.logout("Logout", "sidebar")

if authentication_status == False:
    st.error("Username/password is not correct")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status == True:

    # Import the necessary modules and functions
    from Search_From_CSV import Search_For_Matches  # Assuming Search_From_CSV contains a function to search for matches
    import streamlit as st  # Streamlit library for creating a web application
    import pandas as pd  # Pandas library for data manipulation
    
    # Define the main function where the application logic resides
    def main():

        # Set the title of the web application
        st.title('Loan ID Search')
        
        # Input field for the user to enter the Exxon Code
        desired_value = st.text_input('Enter the loan ID:')
    
        # Check if the 'Search' button is clicked
        if st.button('Search'):
            if desired_value:
                # Call the Search_For_Matches function to find matches
                result = Search_For_Matches(desired_value)
    
                # Check if the result is a Pandas DataFrame
                if isinstance(result, pd.DataFrame):
                    # Display matching codes if found
                    st.write('Matching loan ID:')
                    st.write(result)
                else:
                    # Display an error message if there was an issue with the search
                    st.write(result)
            else:
                # Display a warning if the user didn't provide any input
                st.warning('Please Fill all required entries')
    
    # Call the main function to start the web application
    main()
