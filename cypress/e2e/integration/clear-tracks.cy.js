describe('Clear Tracks Test', () => {
  it('should clear the track list', () => {
    cy.visit('http://localhost:8000'); // Replace with your actual application URL
    cy.get('#trackInput').type('Track1');
    cy.get('.add-btn').click();
    cy.get('.clear-btn').click();
    cy.get('#trackList li').should('have.length', 0);
  });
});