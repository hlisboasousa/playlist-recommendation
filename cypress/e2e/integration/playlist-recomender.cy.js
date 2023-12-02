describe('Playlist Recommender', () => {
    beforeEach(() => {
      cy.visit('http://localhost:8000');
    });
  
    it('should add a track to the track list', () => {
      cy.get('#trackInput').type('Track1');
      cy.get('.add-btn').click();
      cy.get('#trackList li').should('have.length', 1).contains('Track1');
    });
  
    it('should clear the track list', () => {
      cy.get('#trackInput').type('Track1');
      cy.get('.add-btn').click();
      cy.get('.clear-btn').click();
      cy.get('#trackList li').should('have.length', 0);
    });
  
    it('should submit a request and display recommended playlist IDs', () => {
      cy.get('#trackInput').type('Smells Like Teen Spirit');
      cy.get('.add-btn').click();
      cy.get('.submit-btn').click();
      cy.get('#result').should('be.visible');
      // Add assertions based on your expected behavior.
    });
  
    it('should search playlists by song', () => {
      cy.get('#songSearchInput').type('Smells Like Teen Spirit');
      cy.get('.playlist-by-song-btn').click();
      cy.get('#songSearchResult').should('be.visible');
      // Add assertions based on your expected behavior.
    });
  
    it('should get songs by playlist', () => {
      cy.get('#playlistIdInput').type('4050');
      cy.get('.songs-by-playlist-btn').click();
      cy.get('#songsByPlaylistResult').should('be.visible');
      // Add assertions based on your expected behavior.
    });
  });