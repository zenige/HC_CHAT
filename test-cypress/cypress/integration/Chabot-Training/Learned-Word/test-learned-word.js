

describe('test app', () => {
  it('test Search', () => {
    cy.visit('http://localhost:3000/chatbot-training/trained-word')
    cy.get('input[type="search"]').click({force:true}).type('สวัดดี').blur()
  })
  it('test add word', () => {
    cy.visit('http://localhost:3000/chatbot-training/trained-word')
    cy.get('button[class="hcb-btn btn btn_hcb_green btn-block"]').click()
    cy.get('input[name="question"]').type('test1').blur()
    cy.get('input[name="answer"]').type('test1').blur()
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click()
  })
  it('test click edit', () => {
    cy.visit('http://localhost:3000/chatbot-training/trained-word')
    cy.get('button[class="hcb-btn-light btn btn_hcb_blue_light btn-block"]').last().click({force:true})
    cy.get('textarea[name="question"]').last().click().type('ดีครับ1').blur()
    cy.get('textarea[name="answer"]').last().click().type('ดีครับ2').blur()
    cy.get('button[class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"]').click()
  })
  it('test delected word', () => {
    cy.visit('http://localhost:3000/chatbot-training/trained-word')
    cy.get('input[id="__BVID__33"]').last().click({force:true})
    cy.get('button[class="hcb-btn btn btn_hcb_red btn-block"]').click()
    cy.get('button[class="btn btn_green_modal h2dot5 btn-block py-2"]').click()
  })
  
})
