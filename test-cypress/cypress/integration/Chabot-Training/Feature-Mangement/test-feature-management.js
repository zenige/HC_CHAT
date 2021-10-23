describe("test app", () => {
  it("test Search", () => {
    cy.visit("http://localhost:3000/chatbot-training/feature-management");
    cy.get('input[name="Search"]').click({ force: true }).type("AGE").blur();
  });
  it("test click create", () => {
    cy.visit("http://localhost:3000/chatbot-training/feature-management");
    cy.get('button[class="hcb-btn btn btn_hcb_green btn-block"]').click({
      force: true,
    });
    cy.get('input[name="feature"]')
      .last()
      .click({ force: true })
      .type("test")
      .blur();
    cy.get("select").select("input");
    cy.get('input[name="question"]')
      .last()
      .click({ force: true })
      .type("ดีครับ2")
      .blur();
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click({
      force: true,
    });
  });
  it("test click edit", () => {
    cy.visit("http://localhost:3000/chatbot-training/feature-management");
    cy.get('button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]')
      .last()
      .click({ force: true });
    cy.get('input[name="feature"]').click({ force: true }).type("test").blur();
    cy.get("select").select("input");
    cy.get('input[name="question"]')
      .click({ force: true })
      .type("ดีครับ2")
      .blur();
    cy.get(
      'button[class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"]'
    ).click();
  });
  it("test deleted", () => {
    cy.visit("http://localhost:3000/chatbot-training/feature-management");
    cy.get('input[id="__BVID__48"]').last().click({ force: true });
    cy.get('button[class="hcb-btn btn btn_hcb_red btn-block"]').click({
      force: true,
    });
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click({
      force: true,
    });
    cy.screenshot("name");
  });
});
