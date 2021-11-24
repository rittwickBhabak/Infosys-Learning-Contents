var cards = document.querySelectorAll('.content-card')
data = '<ul>'
cards.forEach((card, chapInd) => {
    var title = card.querySelector('.margin-remove.text-truncate.mat-h2').textContent
    // console.log(title)
    var cAlBtn = card.querySelector('button.mat-focus-indicator.margin-left-m.mat-button.mat-button-base.mat-primary')
    cAlBtn.click()
    var lessonTitles = document.querySelectorAll('.margin-remove.text-truncate.mat-h3')
    var tempLi = ''
    lessonTitles.forEach((li, lessonInd) => {tempLi = tempLi + `<li class="lesson-title"><a href="./${chapInd+1}.${lessonInd+1}.html">${li.textContent}</a></li>`})
    // console.log(tempLi)
    data = data + `
        <li>
            <h2 class="chapter-title" id="chapter-${chapInd+1}">${title}</h2>
            <ol>
                ${tempLi}
            </ol>
        </li>
    `
    cAlBtn.click()
})
data = data + '</ul>'
copy(data)

// top-bar-container
// getoknow
// hidden-xs