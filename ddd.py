import streamlit as st
from PIL import Image
import streamlit as st
import streamlit_authenticator as stauth
st.title("expense tracker")

import streamlit as st
import bcrypt

 hashed_passwords = stauth.Hasher(['123cse','def']).generate()
   st.write(hashed_passwords)
