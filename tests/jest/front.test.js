const {
  renderTrackList,
  submitRequest,
  displayRecommendedPlaylistIds,
  searchPlaylistsBySong,
  searchSongsByPlaylist,
} = require('../../frontend/script');

const fetchMock = require('jest-fetch-mock');

fetchMock.enableMocks();
global.fetch = jest.fn(() => Promise.resolve({ json: () => Promise.resolve({ playlist_ids: [1, 2, 3] }) }));

describe('Your Script File Tests', () => {
  beforeEach(() => {
    // Reset the trackList before each test
    trackList = [];
  });

  test('submitRequest should display an alert if trackList is empty', () => {
    global.alert = jest.fn();
    submitRequest();
    expect(alert).toHaveBeenCalledWith('Please add tracks before submitting.');
  });

  test('displayRecommendedPlaylistIds should render playlist IDs to the result div', () => {
    document.getElementById = jest.fn(() => ({ innerHTML: '', appendChild: jest.fn() }));
    const playlistIds = [1, 2, 3];
    displayRecommendedPlaylistIds(playlistIds, 'result');
    expect(document.getElementById).toHaveBeenCalledWith('result');
  });

  test('renderTrackList should render tracks to the list', () => {
    // Mocking the DOM elements
    document.getElementById = jest.fn(() => ({ innerHTML: '', appendChild: jest.fn() }));
    trackList = ['Track1', 'Track2'];
    renderTrackList();
    expect(document.getElementById).toHaveBeenCalledWith('trackList');
  });

  test('searchPlaylistsBySong should make a fetch call and display playlists by song', async () => {
    // Mocking the input value
    document.getElementById = jest.fn(() => ({ value: 'Song1' }));

    // Mocking the DOM elements
    document.getElementById = jest.fn(() => ({ innerHTML: '', appendChild: jest.fn() }));
    await searchPlaylistsBySong();
    expect(fetch).toHaveBeenCalled();
  });

  test('searchSongsByPlaylist should make a fetch call and display songs by playlist', async () => {
    document.getElementById = jest.fn(() => ({ value: '1' }));
    document.getElementById = jest.fn(() => ({ innerHTML: '', appendChild: jest.fn() }));
    await searchSongsByPlaylist();
    expect(fetch).toHaveBeenCalled();
  });
});