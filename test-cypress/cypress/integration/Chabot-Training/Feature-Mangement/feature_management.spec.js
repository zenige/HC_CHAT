/// <reference types="cypress" />

context("Actions", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000/chatbot-training/feature-management");
  });

  it("search() - search for a feature", () => {
    cy.get('input[type="search"]').click({ force: true }).type("AGE").blur();
  });

  it("create() - create a new feature", () => {
    cy.get('button[class="hcb-btn btn btn_hcb_green btn-block"]').click({
      force: true,
    });
    cy.get('input[name="feature"]')
      .last()
      .click({ force: true })
      .type("new feature")
      .blur();
    cy.get("select").select("boolean");
    cy.get('input[name="question"]')
      .last()
      .click({ force: true })
      .type("ทดสอบการสร้าง new feature")
      .blur();
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click({
      force: true,
    });
  });

  it("edit() - edit feature", () => {
    cy.get('button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]')
      .last()
      .click({ force: true });
    cy.get('input[name="feature"]').click({ force: true }).type("test").blur();
    cy.get("select").select("input");
    cy.get('input[name="question"]')
      .click({ force: true })
      .type("ทดสอบแก้ไข feature")
      .blur();
    cy.get(
      'button[class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"]'
    ).click();
  });

  it("delete() - delete a question and answer", () => {
    cy.get('input[id="__BVID__48"]').last().click({ force: true });
    cy.get('button[class="hcb-btn btn btn_hcb_red btn-block"]').click({
      force: true,
    });
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click({
      force: true,
    });
  });
});
