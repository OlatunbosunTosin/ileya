const prompt = require("prompt-sync")();
const {getBookSuggestion, getPageNumber, addNewBooks, removeBooks, updateBooks, showBooks} = require("./bookSuggestionSystem.js");



while(true){

    console.log(` 
    Welcome to the Book Suggestion System!
    1. Get Suggestions
    2. Add Book
    3. Remove Book
    4. Update book
    5. Show all books
    0. Exit

    `)


    const userInput = Number(prompt("Choose an operation: "))
     
    if(userInput == 0)
        break;
            
    switch(userInput){
            
        case 1:
            process.stdout.write(`Book for the Day:\nBook Title: `)
            console.log(getBookSuggestion())
            process.stdout.write("Page: ")
            console.log(getPageNumber())
            
            let anotherSuggestion = prompt("Would you like to get another suggestion? (yes/no): ")
            
            while (anotherSuggestion.toLowerCase() == "yes"){
            
                process.stdout.write("Book for the Day:\nBook Title: ")
                console.log(getBookSuggestion())
                process.stdout.write("Page: ")
                console.log(getPageNumber())
                
                anotherSuggestion = prompt("Would you like to get another suggestion? (yes/no): ")

            }break;
            
        case 2:
            
            const bookTitle = prompt("Enter the book title: ");
            addNewBooks(bookTitle);
            console.log("Book added successfully!");
            break;
            
        case 3:

            const bookName = prompt("Enter the book title to remove: ");
            removeBooks(bookName);
            console.log("Book removed successfully!");
            break;
            
        case 4:

            const oldBookTitle = prompt("Enter the old book title: ");
            const newBookTitle = prompt("Enter the new book title: ");
            updateBooks(oldBookTitle, newBookTitle);
            console.log("Book updated successfully!");
            break;
            
        case 5:
            console.log("All Books");
            let count = 1;
            for (let book of showBooks()){
                console.log(`${count}. ${book}`)
                count+=1;
            }
            break;


    }


}














         

                
                
        
