function creditCardValidator(cardNumber){

    let doubleNumber = 0
    let singleDigits = []
    let sumOfIntegers = 0
    let sumOfSingleDigits = 0
    let sumOfDigits = 0
    let sumOfOddPlaces = 0
    

    for (let index = cardNumber.length - 2; index > -1; index -= 2){

        doubleNumber = Number(cardNumber[index]) * 2;
        singleDigits.push(doubleNumber);
        
    }
    
    for(let digit = 0; digit < singleDigits.length; digit++){  
    
        if ((String(singleDigits[digit])).length == 2){

            for(let number = 0; number < singleDigits[digit].length; number++){  
                sumOfIntegers += Number(String(singleDigits[digit][number]))
            }
            
        }    
        else
            sumOfSingleDigits += Number(String(singleDigits[digit]))
        
            
    }
            
    sumOfDigits = sumOfIntegers + sumOfSingleDigits;
    
    

    for (let index = cardNumber.length - 1; index > -1; index -= 2){
    
        sumOfOddPlaces += Number(cardNumber[index]) 
    }
       
    let result = sumOfDigits + sumOfOddPlaces;
    
    
    if (result % 10 == 0)
    
        validityStatus = "valid"
        
    else
    
        validityStatus = "Invalid"    

    return validityStatus;
        
}
        

function creditCardLength(cardNumber){

    return cardNumber.length;

}    


function creditCardType(cardNumber){

    validityStatus = creditCardValidator(cardNumber)
    cardType = "";
    
    
    if (cardNumber[0] == "4")
        cardType = "Visa card"
        
    else if (cardNumber[0] == "5")
        cardType = "Mastercard"
        
    else if (cardNumber[0] == "3" && cardNumber[1] == "7")
        cardType = "American Express card"
        
    else if (cardNumber[0] == "6")
        cardType = "Discover card"
        
    else
        cardType = "Invalid card"
        
    
    return cardType;
}        

        
module.exports = {creditCardValidator, creditCardLength, creditCardType}     




