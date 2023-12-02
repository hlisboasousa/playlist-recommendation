describe('Submit Request Test', () => {
    it('Should show an alert if no tracks are added before submitting', () => {
      cy.visit('http://localhost:8000'); // Replace with your actual application URL
  
      cy.get('.submit-btn').click();
  
      cy.on('window:alert', (str) => {
        expect(str).to.equal('Please add tracks before submitting.');
      });
    });
  });