def personality_questions():

    questions = [["A.expend energy, enjoy groups", "B.conserve energy, enjoy one-on-one"],
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
        


def response_collection():

    questions = personality_questions()
    responses = []
    for question in questions:

        user_response = input(f"{question[0]}, {question[1]}: ")
        while not (user_response.lower() == "a" or user_response.lower() == "b"):
            print("Expected A or B as Response, Please try again")
            user_response = input(f"{question[0]}, {question[1]}: ")
        responses.append(user_response)
        
    return responses



def extroverted_introverted_personality(collected_responses):

    questions = personality_questions()
    
    count_of_a = 0
    count_of_b = 0
    extroverted_introverted = []
    choices = []
    
    for count in range(0, len(collected_responses), 4):
                
        extroverted_introverted.append(collected_responses[count])
        
    index = 0
    
    for response in extroverted_introverted:
        
        if response == "a":
            count_of_a += 1
            choices.append(questions[index][0])
            index+=4
            
        else:
            count_of_b += 1 
            choices.append(questions[index][1])
            index+=4
                
            
    return [choices, count_of_a, count_of_b]
            
            
def sensing_vs_intuitive_personality(collected_responses):

    questions = personality_questions()

    count_of_a = 0
    count_of_b = 0    
    sensing_vs_intuitive = []
    choices = []
    
    for count in range(1, len(collected_responses), 4):

        sensing_vs_intuitive.append(collected_responses[count])
        
    index = 1
    
    for response in sensing_vs_intuitive:
        
        if response == "a":
            count_of_a += 1
            choices.append(questions[index][0])
            index+=4
            
        else:
            count_of_b += 1 
            choices.append(questions[index][1])
            index+=4
            
    return [choices, count_of_a, count_of_b]
    


def thinking_vs_feeling_personality(collected_responses):

    questions = personality_questions()
    
    count_of_a = 0
    count_of_b = 0   
    thinking_vs_feeling = []
    choices = []
    
    for count in range(2, len(collected_responses), 4):
        
        thinking_vs_feeling.append(collected_responses[count])
            
    index = 2
    
    for response in thinking_vs_feeling:
        
        if response == "a":
            count_of_a += 1
            choices.append(questions[index][0])
            index+=4
            
        else:
            count_of_b += 1 
            choices.append(questions[index][1])
            index+=4
            
    return [choices, count_of_a, count_of_b]
    

    
def judging_vs_perceptive_personality(collected_responses):

    questions = personality_questions()
    
    count_of_a = 0
    count_of_b = 0  
    judging_vs_perceptive = []
    choices = []
        
    for count in range(3, len(collected_responses), 4):
        
        judging_vs_perceptive.append(collected_responses[count])
        
    index = 3
    
    for response in judging_vs_perceptive:
        
        if response == "a":
            count_of_a += 1
            choices.append(questions[index][0])
            index+=4
            
        else:
            count_of_b += 1 
            choices.append(questions[index][1])
            index+=4
            
    return [choices, count_of_a, count_of_b]
            
















