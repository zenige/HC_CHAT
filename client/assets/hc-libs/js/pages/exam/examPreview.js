function openQuestion() {
  let theToggle = document.getElementById('openQuestionBtn')
  let toggleStatus = theToggle.dataset.status
  switch (toggleStatus) {
    case 'off':
      theToggle.dataset.status = 'on'
      document.getElementById('questionCircle').style.height = '100%'
      document.getElementById('questionCircle').style.display = 'block'
      break
    case 'on':
      theToggle.dataset.status = 'off'
      document.getElementById('questionCircle').style.height = '0%'
      document.getElementById('questionCircle').style.display = 'none'
      break
  }
}
