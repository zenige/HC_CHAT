/// <reference types="cypress" />

context("Actions", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000/chatbot-training/learned-word");
  });

  it("search() - search for a question or answer", () => {
    cy.get('input[type="search"]').click({ force: true }).type("สวัสดี").blur();
  });

  it("create() - create a new learned word", () => {
    cy.get('button[class="hcb-btn btn btn_hcb_green btn-block"]').click();
    cy.get('input[name="question"]').type("ทดสอบสร้างคำถาม").blur();
    cy.get('input[name="answer"]').type("ทดสอบสร้างคำตอบ").blur();
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click();
  });

  it("edit() - edit question and answer", () => {
    cy.get('button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]')
      .last()
      .click({ force: true });
    cy.get('textarea[name="question"]')
      .last()
      .click({ force: true })
      .focus()
      .clear()
      .type("ทดสอบแก้ไขคำถาม")
      .blur();
    cy.get('textarea[name="answer"]')
      .last()
      .click({ force: true })
      .focus()
      .clear()
      .type("ทดสอบแก้ไขคำตอบ")
      .blur();
    cy.get(
      'button[class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"]'
    ).click({ force: true });
  });

  it("delete() - delete a question and answer", () => {
    cy.get('input[id="__BVID__33"]').last().click({ force: true });
    cy.get('button[class="hcb-btn btn btn_hcb_red btn-block"]').click();
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click();
  });
});
