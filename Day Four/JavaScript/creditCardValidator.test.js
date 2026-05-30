const {creditCardValidator, creditCardLength, creditCardType} = require("./creditCardValidatorFunction.js");

test("test that card number is valid", () => {

    cardNumber = "5399831619690403"
    expect(creditCardValidator(cardNumber)).toBe("valid")

})

test("test that card number is not valid", () => {

    cardNumber = "5399831619690404"
    expect(creditCardValidator(cardNumber)).toBe("Invalid")

})

test("test for card number length", () => {

    cardNumber = "5399831619690404"
    expect(creditCardLength(cardNumber)).toBe(16)

})

test("test for card type", () => {

    cardNumber = "5399831619690403"
    expect(creditCardType(cardNumber)).toBe("Mastercard")
    
    cardNumber = "234319283049582"
    expect(creditCardType(cardNumber)).toBe("Invalid card")

})
