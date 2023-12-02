describe('Search Playlists by Song Test', () => {
    it('Should search playlists by song and display the result', () => {
      cy.visit('http://localhost:8000'); // Replace with your actual application URL
  
      cy.get('#songSearchInput').type('Song1');
      cy.get('.playlist-by-song-btn').click();
  
      cy.get('#songSearchResult').should('contain', 'Playlists Containing the Song');
    });
  });