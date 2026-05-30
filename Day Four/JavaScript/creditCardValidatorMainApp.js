const {creditCardValidator, creditCardLength, creditCardType} = require("./creditCardValidatorFunction.js");

const prompt = require("prompt-sync")();
cardNumber = prompt("Hello. Kindly Enter Card number to verify: ")

cardValdityStatus = creditCardValidator(cardNumber)
cardLength = creditCardLength(cardNumber)
cardType = creditCardType(cardNumber)

console.log(` 
    Credit Card Type: ${cardType}
    Credit Card Number: ${cardNumber}
    Credit Card Digit Length: ${cardLength}
    Credit Card Validity Status: ${cardValdityStatus}
    
    `)
