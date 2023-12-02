describe('Adding Tracks Test', () => {
  it('Should add tracks and display them in the list', () => {
    cy.visit('http://localhost:8000'); // Replace with your actual application URL

    cy.get('#trackInput').type('Song1');
    cy.get('.add-btn').click();

    cy.get('#trackList').should('have.length', 1);
  });
});