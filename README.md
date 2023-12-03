## Henrique Lisboa de Sousa - 2019436765


## Overview

The Playlist Recommendation App is a web application designed to generate playlist recommendations based on user-provided track inputs. It utilizes a recommendation model built using the Apriori algorithm, and it offers features to search for playlists containing a specific song and retrieve songs from a given playlist.

## Functionality

The application provides the following main features:

1. **Generate Playlist Recommendations**
   - Users can input a list of track names.
   - The app analyzes playlists containing those tracks using the Apriori algorithm.
   - It returns a list of recommended playlist IDs.

2. **Search Playlists by Song**
   - Users can search for playlists that contain a specific song.
   - The app returns a list of playlist IDs containing the requested song.

3. **Get Songs by Playlist**
   - Users can retrieve a list of songs from a specified playlist.
   - The app returns a list of song names in the requested playlist.

## Technologies Used

The Playlist Recommendation App is built using the following technologies:

- **Backend:**
  - Flask (Python web framework)
  - Pandas (Data manipulation library)
  - Apriori Algorithm for recommendation modeling
  - Docker for containerization

- **Frontend:**
  - HTML, CSS
  - JavaScript

- **Testing:**
  - Jest for JavaScript unit testing
  - Unittest for Python unit testing
  - Cypress for end-to-end testing

- **CI/CD:**
  - GitHub Actions for continuous integration and deployment
  - Docker for containerized deployment
  - 
- **Infra:**
  - The app is being served by an EC2 instance in AWS.
  - Access link: http://35.153.157.24:8000/
## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/playlist-recommendation.git
   cd playlist-recommendation
## How to run: Backend
    poetry install
    poetry run python3 models/itemsets_generator.py
    poetry run flask --app api/app.py run

## How to run: Frontend
    cd frontend
    python3 -m http.server 8000 
