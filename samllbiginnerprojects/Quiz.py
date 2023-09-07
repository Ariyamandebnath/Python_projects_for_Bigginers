quiz ={
    "question1": {
        "question":"What is the capital of India?",
        "answer":"Delhi"
    },
    "question2": {
        "question":"What is the capital of Pakistan?",
        "answer":"Lahore"
    },
    "question3": {
        "question":"What is the capital of Bangladesh?",
        "answer":"Dhaka"
    },
    "question4": {
        "question":"What is the capital of Australia?",
        "answer":"Canberra"
    },
    "question5": {
        "question":"What is the capital of France?",
        "answer":"Paris"
    },
    "question6": {
        "question":"What is the capital of Canada?",
        "answer":"Ottawa"
    },
    "question7": {
        "question":"What is the capital of China?",
        "answer":"Beijing"
    },
    "question8": {
        "question":"What is the capital of Japan?",
        "answer":"Tokyo"
    }
      
}

score  = 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")
    
    if answer.lower()==value["answer"].lower():
        print("Correct")
        score+=1
        
        
    else:
        print("Wrong answer")
        print("The answer is :"+value["answer"])
        
        print("")
        
        
        
print("You got "+str(score)+ "out of 8 quiestions")

print(str(score/8 *100)+ "%"+"questions are answered correctly")
        
        
