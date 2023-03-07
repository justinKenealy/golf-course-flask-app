const quotes = [
    "hello1",
    "hello2",
    "hello3",
    "hello4",
    "hello5",
    "hello6",
    "hello7",
    "hello8",
    "hello9",
    "hello10"
]

const quotesDiv = document.getElementById('golfQuote')
const selectedQuote = quotes[Math.floor(Math.random()*quotes.length)]

quotesDiv.innerHTML = selectedQuote