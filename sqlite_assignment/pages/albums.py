
import streamlit as st
import sqlite3
import db

st.title("Albums")
albums = db.get_all_albums()

st.subheader("Current Albums")
st.dataframe(albums)
option = st.selectbox(
    "Select an Operation",
    ["Add Album", "Update Album", "Delete Album"]
)

if option == "Add Album":
    st.subheader("Add New Album")
    with st.form("add_album"):
        title = st.text_input("Album Title")
        artist = st.text_input("Artist Name")
        label = st.text_input("Record Label")
        duration = st.text_input("Total Duration (HH:MM:SS)")
        submitted = st.form_submit_button("Save Album")
    if submitted:
        if title.strip() and artist.strip() and label.strip() and duration.strip():
            db.add_record(title, artist, label, duration)
            st.success("Album added successfully.")
        else:
            st.error("Please complete all fields.")

elif option == "Update Album":
    st.subheader("Update Album")
    if not albums.empty:
        albumid = st.selectbox(
            "Select Album ID", albums["albumID"]
        )
        record = albums[
            albums["albumID"] == albumid
        ].iloc[0]
        with st.form("update_album"):
            title = st.text_input(
                "Album Title", value=record["albumTitle"]
            )
            artist = st.text_input(
                "Artist Name", value=record["artistName"]
            )
            label = st.text_input(
                "Record Label", value=record["recordLabel"]
            )
            duration = st.text_input(
                "Total Duration", value=record["totalDuration"]
            )
            submitted = st.form_submit_button("Update Album")
        if submitted:
            if title.strip() and artist.strip() and label.strip() and duration.strip():
                db.update_record(
                    int(albumid), title, artist, label, duration
                )
                st.success("Album updated successfully.")
            else:
                st.error("Please complete all fields.")
    else:
        st.warning("No albums available.")

elif option == "Delete Album":
    st.subheader("Delete Album")
    if not albums.empty:
        albumid = st.selectbox(
            "Select Album ID", albums["albumID"]
        )
        confirm = st.checkbox("Confirm deletion")
        if st.button("Delete Album"):
            if confirm:
                try:
                    db.delete_record(int(albumid))
                    st.success("Album deleted successfully.")
                except sqlite3.IntegrityError:
                    st.error("Delete the album's tracks first.")
            else:
                st.warning("Please confirm deletion.")
    else:
        st.warning("No albums available.")
