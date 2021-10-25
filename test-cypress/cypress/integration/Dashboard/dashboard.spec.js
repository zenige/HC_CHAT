{
  /* <reference types="cypress" /> */
}

describe("Actions", () => {
  it("go() - go to group", () => {
    cy.visit("http://localhost:3000/dashboard/all-patient-group");
    cy.get('a[href="/dashboard/patient-group/group0"]').click({ force: true });
  });
  it("search() - search a patient", () => {
    cy.get('input[name="search"]')
      .click({ force: true })
      .type("บวรศักดิ์")
      .blur();
  });
  it("show() - show patient information", () => {
    cy.get(
      'button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]'
    ).click({ force: true });
  });
});
