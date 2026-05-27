const {getBookSuggestion, getPageNumber, addNewBooks, removeBooks, updateBooks, showBooks} = require("./bookSuggestionSystem.js");

test("test that book page suggestion is between one and hundred", () => {

    expect(getPageNumber()).toBeGreaterThanOrEqual(1) && toBeLessThanOrEqual(100)


})


test("test that new book is added", () => {

    expect(addNewBooks("River")).toEqual(["The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom", "River"])


})


test("test that book is removed", () => {

    expect(removeBooks("The Hobbit")).toEqual(["The Mystery", "Animal Farm", "Brave kingdom", "River"])


})


test("test that book name is updated", () => {

    expect(updateBooks("The Mystery", "Mystery")).toEqual(["Mystery", "Animal Farm", "Brave kingdom", "River"])


})


test("test that all books are shown", () => {

    expect(showBooks()).toEqual(["Mystery", "Animal Farm", "Brave kingdom", "River"])


})

