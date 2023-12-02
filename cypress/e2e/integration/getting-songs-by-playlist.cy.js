describe('Get Songs by Playlist Test', () => {
    it('Should get songs by playlist ID and display the result', () => {
      cy.visit('http://localhost:8000'); // Replace with your actual application URL
  
      cy.get('#playlistIdInput').type('1'); // Assuming there's a playlist with ID 1
      cy.get('.songs-by-playlist-btn').click();
  
      cy.get('#songsByPlaylistResult').should('contain', 'Songs in the Playlist');
    });
  });