/// <reference types="cypress" />

context("Actions", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000/");
  });

  it("test Search", () => {
    cy.get('input[name="Search"]').click({ force: true }).type("ดีครับ").blur();
  });
  it("test click edit", () => {
    cy.get('button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]')
      .last()
      .click({ force: true });
    cy.get('textarea[name="question"]')
      .last()
      .click({ force: true })
      .type("ดีครับ1")
      .blur();
    cy.get('textarea[name="answer"]')
      .last()
      .click({ force: true })
      .type("ดีครับ2")
      .blur();
    cy.get(
      'button[class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"]'
    ).click({ force: true });
  });

  it("test click deleted", () => {
    cy.get('label[class="custom-control-label"]').last().click({ force: true });
    cy.get('button[class="hcb-btn btn btn_hcb_red btn-block"]')
      .last()
      .click({ force: true });
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click({
      force: true,
    });
  });
});
