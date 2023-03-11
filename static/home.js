// render golf quote/joke on homepage
const quotes = [
    "The more I work and practice, the luckier I seem to get.",
    "For this game you need, above all things, to be in a tranquil frame of mind.",
    "The worst day at golf still beats the best day at work.",
    "A bad attitude is worse than a bad swing.",
    "The most important shot in golf is the next one.",
    "The secret of playing good golf is to hit the ball hard, straight, and not too often!",
    "The best person to play golf with is someone who is a little bit worse than you.",
    "Golf: a 10km walk punctuated with disappointments.",
    "You're the best, by par.",
    "This is all fore the best.",
    "May the course be with you.",
    "Golf is a day spent in a round of strenuous idleness."
]
const quotesDiv = document.getElementById('golfQuote')
const generateQuote = function(){
    const selectedQuote = quotes[Math.floor(Math.random()*quotes.length)]
    quotesDiv.innerHTML = `"${selectedQuote}"`
}
generateQuote()
setInterval(generateQuote, 10000)

// functionality to view all rounds on homepage
const viewAllButton = document.getElementById('viewAll')
const allRounds = document.getElementById('allRounds')
const closeAllRounds = document.getElementById('closeAllRounds')
const showAllRounds = function(){
    allRounds.style.display = 'block'
}
const hideAllRounds = function(){
    allRounds.style.display = 'none'
}
viewAllButton.addEventListener('click', showAllRounds)
closeAllRounds.addEventListener('click', hideAllRounds)

// functionality to scroll through stats on homepage
const lastRoundBox = document.getElementById('lastRound')
const lastThreeBox = document.getElementById('lastThree')
const lastFiveBox = document.getElementById('lastFive')
const lastTenBox = document.getElementById('lastTen')

const leftArrows = document.getElementsByClassName('leftArrow')
const rightArrows = document.getElementsByClassName('rightArrow')

let displayCounter = 0
const renderStats = function(){
    if (displayCounter === 0){
        lastRoundBox.style.display = 'grid'
        lastThreeBox.style.display = 'none'
        lastFiveBox.style.display = 'none'
        lastTenBox.style.display = 'none'
    } else if (displayCounter === 1){
        lastRoundBox.style.display = 'none'
        lastThreeBox.style.display = 'grid'
        lastFiveBox.style.display = 'none'
        lastTenBox.style.display = 'none'
    } else if (displayCounter === 2){
        lastRoundBox.style.display = 'none'
        lastThreeBox.style.display = 'none'
        lastFiveBox.style.display = 'grid'
        lastTenBox.style.display = 'none'
    } else if (displayCounter === 3){
        lastRoundBox.style.display = 'none'
        lastThreeBox.style.display = 'none'
        lastFiveBox.style.display = 'none'
        lastTenBox.style.display = 'grid'
    }
}

const displayCounterPlus = function(){
    if (displayCounter === 3){
        displayCounter = 0
    } else {
        displayCounter++
    } 
    renderStats()
}
const displayCounterMinus = function(){
    if (displayCounter === 0){
        displayCounter = 3
    } else {
        displayCounter--
    } 
    renderStats()
}

for (let arrow of leftArrows){
    arrow.addEventListener('click', displayCounterMinus)
}

for (let arrow of rightArrows){
    arrow.addEventListener('click', displayCounterPlus)
}

// export stats to excel
function exportReportToExcel() {
    const table= document.getElementById("allRoundsTable")
       const html = table.outerHTML;
       window.open('data:application/vnd.ms-excel,' + encodeURIComponent(html));
}
exportButton = document.getElementById('exportButton')
exportButton.addEventListener('click', exportReportToExcel)