🎥 Movie Recommender System
This project is a Machine Learning-based Movie Recommender System done as part of minor project at my college, University School of Automation and Robotics, IPU East Campus, New Delhi. This project provides personalized movie recommendations based on the movie you select. The application is powered by Python, Streamlit, and machine learning techniques, leveraging cosine similarity and the TMDB dataset.

🌟 Features
Personalized Recommendations: Suggests similar movies based on user-selected titles.
Poster Display: Fetches and displays movie posters using the TMDB API.
Interactive UI: Provides a user-friendly interface built with Streamlit.
Efficient Deployment: Ready for deployment on Render or similar platforms.
🚀 Technologies Used
Machine Learning: Cosine similarity for recommendation.
Streamlit: For building the interactive front-end.
TMDB API: For fetching movie posters.
Python Libraries: Pandas, Scikit-learn, Requests, and more.
📂 Dataset
This project uses the TMDb 5000 Movies dataset from Kaggle, which includes:

Movie metadata (title, genre, keywords, cast, crew, etc.)
Revenue and budget details
TMDB IDs for fetching posters
Dataset Files:
tmdb_5000_movies.csv
tmdb_5000_credits.csv
These files are preprocessed to generate the recommendation system's core data.

🛠️ Setup Instructions
Follow these steps to set up and run the project locally:

Prerequisites
Ensure you have the following installed:

Python 3.8 or higher
Pip
Virtual environment tools (like venv or conda)
Steps
Clone the Repository:

git clone https://github.com/AbhiramSakha/T-06-Movie-Recommender.git
cd movie-recommender
Set Up the Virtual Environmnet:

python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Download Additional Files: The project requires the following preprocessed files:

movie_list.pkl

similarity.pkl # These files are automatically downloaded from Google Drive during the app's runtime.

Or if you want, you can run the python code available at google colab on here. Make sure you first upload the 2 datasets by downloading them from the following links:

Link for tmdb_5000_movies.csv and link for tmdb_5000_credits.csv.

Run the Application:

streamlit run app.py
Access the App: Open the URL displayed in the terminal, typically http://localhost:8501.

📄 Additional Files
The repository includes:

Project Report: A detailed explanation of the project in PDF format (Vedant Roy Minor Project Report on Movie Recommendation System.pdf).
Presentation Slides: A concise slide deck used for the college presentation in pdf format (Team-06 Minor Project Movie-Recommender-System PPT.pdf).
🔧 Deployment
This project is ready to be deployed on Render or similar platforms. Follow these steps:

Push your project repository to GitHub.
Create a new Web Service on Render.
Link your GitHub repository to Render.
Set up a requirements.txt file for dependencies.
Add environment variables if necessary (e.g., TMDB API key).
Deploy the app, and Render will handle the rest.
🎥 Demo Video
Excited to see how the Movie Recommender System works? Check out the demo video showcasing the project in action! It demonstrates:

The interactive Streamlit interface. Movie recommendation functionality. Poster fetching using the TMDB API. Click the link below to watch the full demo: Watch Demo Video

This video provides a comprehensive walkthrough of the project and its features. Let me know your feedback or suggestions! 😊

📬 Contact
For queries, suggestions, or collaboration, feel free to reach out to me:
 Email: aabhiramsakha@gmail.com

🔗 References
TMDB API: The Movie Database API Dataset: TMDb 5000 Movie Dataset on Kaggle

🙌 Acknowledgments
Special thanks to TMDB and Kaggle for providing the data and resources for this project.

🌟 Star the repository if you found this helpful!
