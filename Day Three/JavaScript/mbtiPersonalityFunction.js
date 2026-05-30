const prompt = require("prompt-sync")();

function personalityQuestions(){

    let questions = [["A.expend energy, enjoy groups", "B.conserve energy, enjoy one-on-one"],
    ["A.Interpret literally", "B.look for meaning and possibilities"],
    ["A.logical, thinking, questioning", "B.empathetic, feeling, accommodating"],
    ["A.organized, orderly", "B.flexible, adaptable"],
    ["A.more outgoing, think out loud", "B.more reserved, think to yourself"],
    ["A.practical, realistic, experiential", "B.imaginative, innovative, theoretical"],
    ["A.candid, straight forward, frank", "B.tactful, kind, encouraging"],
    ["A.plan, schedule", "B.unplanned, spontaneous"],
    ["A.seek many tasks, public activities, interaction with others", "B.seek private, solitary activities with quiet to concentrate"],
    ["A.standard, usual, conventional", "B.different, novel, unique"],
    ["A.firm, tend to criticize, hold the line", "B.gentle, tend to appreciate, conciliate"],
    ["A.regulated, structured", "B.easy-going, live and let live"],
    ["A.external, communicative, express yourself", "B.internal, reticent, keep to yourself"],
    ["A.focus on here-and-now", "B.look to the future, global perspective, big picture"],
    ["A.tough-minded, just", "B.tender-hearted, merciful"],
    ["A.preparation, plan ahead", "B.go with the flow, adapt as you go"],
    ["A.active, initiate", "B.reflective, deliberate"],
    ["A.facts, things, what is", "B.ideas, dreams, what could be, philosophical"],
    ["A.matter of fact, issue-oriented", "B.sensitive, people-oriented, compassionate"],
    ["A.control, govern", "B.latitude, freedom"]]
    
    return questions
}        


function responseCollection(){

    let questions = personalityQuestions()
    let responses = []
    
    for(let index = 0; index < questions.length; index++){

        let userResponse = prompt(`${questions[index][0]}, ${questions[index][1]}: `)
        while (userResponse.toLowerCase() != "a" && userResponse.toLowerCase() != "b"){
            console.log("Expected A or B as Response, Please try again")
            userResponse = prompt(`${questions[index][0]}, ${questions[index][1]}: `)
        }
        responses.push(userResponse)
    }
       
    return responses
}



function getExtrovertedIntrovertedPersonality(collectedResponses){

    let questions = personalityQuestions()
    
    let countOfA = 0
    let countOfB = 0
    let extrovertedIntroverted = []
    let choices = []
    
    for (let count = 0; count < collectedResponses.length; count+= 4){
                
        extrovertedIntroverted.push(collectedResponses[count]);
        
    }    
    index = 0
    
    for (let counter = 0; counter < extrovertedIntroverted.length; counter++){
        
        if (extrovertedIntroverted[counter].toLowerCase() == "a"){
            countOfA += 1
            choices.push(questions[index][0])
            index+=4
        }   
        else{
            countOfB += 1 
            choices.push(questions[index][1])
            index+=4
        }        
    }        
    
    return [choices, countOfA, countOfB]
    
}

          
        
function getSensingVsIntuitivePersonality(collectedResponses){

    questions = personalityQuestions()

    let countOfA = 0
    let countOfB = 0
    let sensingVsIntuitive = []
    let choices = []
    
    
    for (let count = 0; count < collectedResponses.length; count+= 4){
                
        sensingVsIntuitive.push(collectedResponses[count]);
        
    }  
    
    index = 1
    
    for (let counter = 0; counter < sensingVsIntuitive.length; counter++){
        
        if (sensingVsIntuitive[counter].toLowerCase() == "a"){
            countOfA += 1
            choices.push(questions[index][0])
            index+=4
        }   
        else{
            countOfB += 1 
            choices.push(questions[index][1])
            index+=4
        }        
    }        
    
    return [choices, countOfA, countOfB]
    
}


function getThinkingVsFeelingPersonality(collectedResponses){

    questions = personalityQuestions()

    let countOfA = 0
    let countOfB = 0
    let thinkingVsFeeling = []
    let choices = []
    
    for (let count = 2; count < collectedResponses.length; count+= 4){
                
        thinkingVsFeeling.push(collectedResponses[count]);
        
    }  
            
    index = 2
    
    for (let counter = 0; counter < thinkingVsFeeling.length; counter++){
        
        if (thinkingVsFeeling[counter].toLowerCase() == "a"){
            countOfA += 1
            choices.push(questions[index][0])
            index+=4
        }   
        else{
            countOfB += 1 
            choices.push(questions[index][1])
            index+=4
        }        
    }        
    
    return [choices, countOfA, countOfB]
    
}   

    
function judgingVsPerceptivePersonality(collectedResponses){

    questions = personalityQuestions()

    let countOfA = 0
    let countOfB = 0
    let judgingVsPerceptive = []
    let choices = []
        
    for (let count = 3; count < collectedResponses.length; count+= 4){
                
        judgingVsPerceptive.push(collectedResponses[count]);
        
    }  
        
    index = 3
    
    for (let counter = 0; counter < judgingVsPerceptive.length; counter++){
        
        if (judgingVsPerceptive[counter].toLowerCase() == "a"){
            countOfA += 1
            choices.push(questions[index][0])
            index+=4
        }   
        else{
            countOfB += 1 
            choices.push(questions[index][1])
            index+=4
        }        
    }        
    
    return [choices, countOfA, countOfB]
    
}

module.exports = {personalityQuestions, responseCollection,getExtrovertedIntrovertedPersonality, getSensingVsIntuitivePersonality, getThinkingVsFeelingPersonality, judgingVsPerceptivePersonality}













