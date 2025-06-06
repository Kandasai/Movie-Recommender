import streamlit as st
import requests
import hashlib
import os
import pickle
import time

# Streamlit Page Config
st.set_page_config(page_title="🎥 Movie & TV Show Recommender", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body { background-color: #121212; color: #ffffff; }
        .title { text-align: center; font-size: 2.5em; color: #ff4a57; }
        .stTextInput > div > div > input { border-radius: 10px; border: 1px solid #ff4a57; padding: 10px; }
        .stButton > button { background-color: #ff4a57; color: white; padding: 12px 20px; border-radius: 10px; border: none; cursor: pointer; }
        .stButton > button:hover { background-color: #ff1e3d; }
    </style>
""", unsafe_allow_html=True)

# User Authentication System
USERS_DB = "users.pkl"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def load_users():
    return pickle.load(open(USERS_DB, "rb")) if os.path.exists(USERS_DB) else {}

def save_users(users):
    pickle.dump(users, open(USERS_DB, "wb"))

def login_page():
    """Login and Signup page"""
    st.markdown('<h1 class="title">🔑 Login / Signup</h1>', unsafe_allow_html=True)
    users = load_users()

    choice = st.radio("Select an option:", ["Login", "Signup"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if choice == "Signup":
        if st.button("Sign Up"):
            if username in users:
                st.warning("⚠️ Username already exists! Try another one.")
            elif not username or not password:
                st.warning("⚠️ All fields are required.")
            else:
                users[username] = {'password': hash_password(password)}
                save_users(users)
                st.success("✅ Account created successfully! Please login.")

    if choice == "Login":
        if st.button("Login"):
            if username in users and users[username]['password'] == hash_password(password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("✅ Login successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Invalid username or password!")

def logout():
    """Logout function"""
    for key in ["logged_in", "username"]:
        if key in st.session_state:
            del st.session_state[key]
    st.success("✅ Logged out successfully!")
    time.sleep(1.5)
    st.rerun()

# API Keys
OMDB_API_KEY = "eff36f78"
RAPIDAPI_KEYS = [
    "306b6505b2msh5655b88e228dffcp1e1f07jsne70b4dfcae65",
    "e5a945511fmsh25f9e3b1849cce7p1c6918jsn2bc667aa3d11",
    "f44e5e8f83msh3abbeee8bd13cc7p14c417jsn860c2e85dc58"
]

# Movie & TV Show Search Functionality
def fetch_movies_and_shows(query_term):
    """Fetch movies and TV shows from OMDb API"""
    if not query_term:
        return []
    
    results = []
    for category in ["movie", "series"]:
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={query_term}&type={category}"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("Search"):
                results.extend(data["Search"])
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error fetching {category}s: {str(e)}")
    return results

# Main UI Logic
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    login_page()
else:
    st.sidebar.button("🚪 Logout", on_click=logout)
    query_term = st.sidebar.text_input("Enter Movie or TV Show Name")

    if query_term:
        results = fetch_movies_and_shows(query_term)
        if results:
            st.markdown('<h2 class="title">🎬 Movie & TV Show Results</h2>', unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, item in enumerate(results):
                with cols[idx % 3]:
                    poster_url = item.get("Poster", "https://via.placeholder.com/150")
                    title = item.get("Title", "Unknown Title")
                    year = item.get("Year", "N/A")
                    imdb_id = item.get("imdbID", "")
                    
                    st.markdown(f"""
                        <div style="text-align:center;">
                            <img src="{poster_url}" width="80%">
                            <h3>{title} ({year})</h3>
                            <a href="https://www.imdb.com/title/{imdb_id}" target="_blank">🔗 IMDb</a><br>
                            <a href="https://www.youtube.com/results?search_query={title}+trailer" target="_blank">▶️ Watch Trailer</a>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown('<p style="text-align:center;">🔄 No results found.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="text-align:center;">🔍 Enter a movie or TV show name to search.</p>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("📧 **Contact Support:** [saikanda2004@gmail.com](mailto:saikanda2004@gmail.com)")
