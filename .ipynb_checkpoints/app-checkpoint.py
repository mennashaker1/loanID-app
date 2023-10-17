# Import the necessary modules and functions
from Search_From_CSV import Search_For_Matches  # Assuming Search_From_CSV contains a function to search for matches
import streamlit as st  # Streamlit library for creating a web application
import pandas as pd  # Pandas library for data manipulation

# Define the main function where the application logic resides
def main():
    
    # Set the title of the web application
    st.title('Exxon Codes Search')
    
    # Input field for the user to enter the Exxon Code
    desired_value = st.text_input('Enter the Exxon Code:')

    # Check if the 'Search' button is clicked
    if st.button('Search'):
        if desired_value:
            # Check if the entered value is a 14-digit number
            if desired_value.isdigit() and len(desired_value) == 14:
                # Call the Search_For_Matches function to find matches
                result = Search_For_Matches(int(desired_value))

                # Check if the result is a Pandas DataFrame
                if isinstance(result, pd.DataFrame):
                    # Display matching codes if found
                    st.write('Matching Code:')
                    st.write(result)
                else:
                    # Display an error message if there was an issue with the search
                    st.write(result)
            else:
                # Display a warning if an incorrect code format is entered
                st.warning('Wrong code Entered, Please Enter a 14-digit code')
        else:
            # Display a warning if the user didn't provide any input
            st.warning('Please Fill all required entries')

# Call the main function to start the web application
main()
