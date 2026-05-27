listOfBooks = ["The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom"];

function getBookSuggestion(){

    let index = Math.floor(Math.random() * listOfBooks.length);
    return listOfBooks[index];  
}


function getPageNumber(){

     return Math.floor(Math.random() * 100) + 1

}
      
        
function addNewBooks(bookName){

    listOfBooks.push(bookName)
    return listOfBooks
}


function removeBooks(bookName){

    listOfBooks.splice(listOfBooks.indexOf(bookName),1)
    return listOfBooks

}


function updateBooks(oldBookName, newBookName){

    listOfBooks[listOfBooks.indexOf(oldBookName)] = newBookName
    return listOfBooks

}


function showBooks(){

    return listOfBooks
    
};
    
module.exports = {getBookSuggestion, getPageNumber, addNewBooks, removeBooks, updateBooks, showBooks};


