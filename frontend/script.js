const API_URL = "http://localhost:5000/api";

let trackList = [];

function addTrack() {
    const trackInput = document.getElementById("trackInput").value;
    if (trackInput.trim() !== "") {
        trackList.push(trackInput);
        document.getElementById("trackInput").value = "";
        renderTrackList();
    }
}

function clearTrackList() {
    trackList = [];
    renderTrackList();
}

function renderTrackList() {
    const trackListUl = document.getElementById("trackList");
    trackListUl.innerHTML = "";
    trackList.forEach(track => {
        const li = document.createElement("li");
        li.textContent = track;
        trackListUl.appendChild(li);
    });
}

function submitRequest() {
    if (trackList.length === 0) {
        alert("Please add tracks before submitting.");
        return;
    }

    fetch(`${API_URL}/api/recommend`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ tracks: trackList })
    })
    .then(response => response.json())
    .then(data => {
        displayRecommendedPlaylistIds(data.playlist_ids, "result");
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function displayRecommendedPlaylistIds(playlistIds, resource) {
    const resultDiv = document.getElementById(resource);
    resultDiv.innerHTML = "<h2>Recommended Playlist IDs</h2>";
    const list = document.createElement("ul");
    list.classList.add("playlist-list");

    playlistIds.forEach(id => {
        const listItem = document.createElement("li");
        listItem.textContent = id;
        list.appendChild(listItem);
    });

    resultDiv.appendChild(list);
}

function searchPlaylistsBySong() {
    const songSearchInput = document.getElementById("songSearchInput").value;

    fetch(`${API_URL}/get-playlists-by-song`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ song: songSearchInput })
    })
    .then(response => response.json())
    .then(data => {
        displayPlaylistsBySong(data.playlist_ids, "songSearchResult");
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function displayPlaylistsBySong(playlistIds, resource) {
    const songSearchResultDiv = document.getElementById(resource);
    songSearchResultDiv.innerHTML = "<h2>Playlists Containing the Song</h2>";
    const list = document.createElement("ul");
    list.classList.add("playlist-list");
    
    playlistIds.forEach(id => {
        const listItem = document.createElement("li");
        listItem.textContent = id;
        list.appendChild(listItem);
    });

    songSearchResultDiv.appendChild(list);
}