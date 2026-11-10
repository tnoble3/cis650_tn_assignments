
import streamlit as st
import db
st.title("Tracks")

tracks = db.get_all_tracks()
albums = db.get_all_albums()

st.subheader("Current Tracks")
st.dataframe(tracks)
option = st.selectbox(
    "Select an Operation",
    ["Add Track", "Update Track", "Search Tracks", "Delete Track"]
)

if option == "Add Track":
    st.subheader("Add New Track")
    if not albums.empty:
        with st.form("add_track"):
            albumid = st.selectbox(
                "Select Album ID", albums["albumID"]
            )
            title = st.text_input("Track Title")
            duration = st.number_input(
                "Duration (seconds)", min_value=1, step=1
            )
            submitted = st.form_submit_button("Save Track")
        if submitted:
            if title.strip():
                db.add_track(
                    int(albumid), title, int(duration)
                )
                st.success("Track added successfully.")
            else:
                st.error("Track title is required.")
    else:
        st.warning("Please add an album first.")

elif option == "Update Track":
    st.subheader("Update Track")
    if not tracks.empty:
        trackid = st.selectbox(
            "Select Track ID", tracks["trackID"]
        )
        record = tracks[
            tracks["trackID"] == trackid
        ].iloc[0]
        with st.form("update_track"):
            title = st.text_input(
                "Track Title", value=record["trackTitle"]
            )
            duration = st.number_input(
                "Duration (seconds)",
                min_value=1,
                value=int(record["totalDuration"])
            )
            submitted = st.form_submit_button("Update Track")
        if submitted:
            if title.strip():
                db.update_track(
                    int(trackid), title, int(duration)
                )
                st.success("Track updated successfully.")
            else:
                st.error("Track title is required.")
    else:
        st.warning("No tracks available.")

elif option == "Search Tracks":
    st.subheader("Search Tracks by Album")
    if not albums.empty:
        albumid = st.selectbox(
            "Select Album ID", albums["albumID"]
        )
        if st.button("Search"):
            results = db.query_record(int(albumid))
            st.dataframe(results)
    else:
        st.warning("No albums available.")

elif option == "Delete Track":
    st.subheader("Delete Track")
    if not tracks.empty:
        trackid = st.selectbox(
            "Select Track ID", tracks["trackID"]
        )
        confirm = st.checkbox("Confirm deletion")
        if st.button("Delete Track"):
            if confirm:
                db.delete_track(int(trackid))
                st.success("Track deleted successfully.")
            else:
                st.warning("Please confirm deletion.")
    else:
        st.warning("No tracks available.")
