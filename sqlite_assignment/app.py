
import streamlit as st
import db

db.init_db()

def home():
    st.title("Music Album Database")
    st.write("Use the sidebar to manage albums and tracks.")

pg = st.navigation([
    st.Page(home, title="Home"),
    st.Page("pages/albums.py", title="Albums"),
    st.Page("pages/tracks.py", title="Tracks")
])

pg.run()
