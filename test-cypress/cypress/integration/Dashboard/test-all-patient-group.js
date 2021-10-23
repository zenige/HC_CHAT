{
  /* <reference types="cypress" /> */
}

describe("test app", () => {
  it("Go to group", () => {
    cy.visit("http://localhost:3000/dashboard/all-patient-group");
    cy.get('a[href="/dashboard/patient-group/group0"]').click({ force: true });
  });
  it("Search patient", () => {
    cy.get('input[name="search"]')
      .click({ force: true })
      .type("บวรศักดิ์")
      .blur();
  });
  it("Show patient information", () => {
    cy.get(
      'button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]'
    ).click({ force: true });
  });
});
