from dataclasses import dataclass
import time
import threading

@dataclass
class Question:
    prompt: str
    options: list[str]
    answer: str

quiz_questions = [
    Question(
        prompt="What is the capital of France?",
        options=["A) Berlin", "B) London", "C) Paris", "D) Rome"],
        answer="C"
    ),
    Question(
        prompt="Which language is primarily used for AI?",
        options=["A) Python", "B) Java", "C) C++", "D) Swift"],
        answer="A"
    ),
    Question(
        prompt="What year did World War II end?",
        options=["A) 1939", "B) 1945", "C) 1942", "D) 1950"],
        answer="B"
    ),
]

#Timer flag
time_up = False

def countdown_timer(seconds: int):
    global time_up
    for _ in range(seconds):
        time.sleep(1)
    time_up = True


def run_quiz(questions, time_limit=30):
    global time_up
    score = 0

    timer_thread = threading.Thread(target=countdown_timer,args=(time_limit,))
    timer_thread.start()

    print(f"\n You have {time_limit} seconds to answer all questions")

    for index, q in enumerate (questions, start=1):
        if time_up:
            print("\n time is up")
            break

        print(f"Q{index}:{q.prompt}")
        for opt in q.options:
            print(opt)
        
        try:
            answer = input("Your answer (A/B/C/D):").strip().upper()
            if answer == q.answer:
                print("Correct answer \n")
                score+=1

            else :
                print(f"Wrong! the correct answer is {q.answer}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    print(f"\n Your final score: {score}/{len(questions)}")

if __name__ =="__main__":
    run_quiz(quiz_questions,time_limit=30)