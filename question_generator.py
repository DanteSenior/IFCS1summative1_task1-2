import random

def generate_questions(difficulty):
    """
    Generate questions based on difficulty level.

    args: 
        difficulty (str): The difficulty level of the question.
        
    returns:
        str 

    """
    if difficulty == "easy":
        a, b = random.randint(1, 12), random.randint(1, 12)
        easy_question_ans = a * b 
        return f"{a} * {b} = ?", easy_question_ans
    
    elif difficulty == "medium":
        a, b, c = random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)
        medium_question_ans = a * b + c
        return f"{a} * {b} + {c} = ?", medium_question_ans
    
    elif difficulty == "hard":
        a, b = random.randint(1, 12), random.randint(1, 12)
        c, d = random.randint(1, 12), random.randint(1, 12)
        hard_question_ans = ((a**2) * b + c * d) + c
        return f"{a}^2 * {b} + {c} * {d} + {c} = ?", hard_question_ans