const {personalityQuestions, responseCollection, getExtrovertedIntrovertedPersonality, getSensingVsIntuitivePersonality, getThinkingVsFeelingPersonality, judgingVsPerceptivePersonality} = require("./mbtiPersonalityFunction.js")

const collectedResponses = responseCollection()



test("test that twenty responses are collected", () => {
    
    expect(collectedResponses.length == 20).toBe(true)
        
        
})
        

test("test for choices and count of responses of extrovert vs introvert questions", () => {
    
    
    expected = getExtrovertedIntrovertedPersonality(collectedResponses)
    actual = [['A.expend energy, enjoy groups', 'A.more outgoing, think out loud', 'A.seek many tasks, public activities, interaction with others', 'A.external, communicative, express yourself', 'A.active, initiate'], 5, 0]

    expect(expected).toEqual(actual)
    
})
        
 
test("test for choices and count of responses of sensing vs intuition questions", () =>{
    
    expected = getSensingVsIntuitivePersonality(collectedResponses)
    actual = [['A.Interpret literally', 'A.practical, realistic, experiential', 'A.standard, usual, conventional', 'A.focus on here-and-now', 'A.facts, things, what is'], 5, 0]

    expect(expected).toEqual(actual)

})

        
test("test for choices and count of responses of thinking vs feeling questions", () => { 
    
    expected = getThinkingVsFeelingPersonality(collectedResponses)
    actual = [['B.empathetic, feeling, accommodating', 'B.tactful, kind, encouraging', 'B.gentle, tend to appreciate, conciliate', 'B.tender-hearted, merciful', 'B.sensitive, people-oriented, compassionate'], 0, 5]

    expect(expected).toEqual(actual)
})


        
test(" test for choices and count of responses of judging vs perceptive questions", () => {
    
    expected = judgingVsPerceptivePersonality(collectedResponses)
    actual = [['B.flexible, adaptable', 'B.unplanned, spontaneous', 'B.easy-going, live and let live', 'B.go with the flow, adapt as you go', 'B.latitude, freedom'], 0, 5]

    expect(expected).toEqual(actual)
        
})      
