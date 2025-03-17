from MCS.games.engine import run_game
import random
import math


def generate_question():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = math.lcm(*numbers)
    return question, correct_answer


def play():
    rules = "Find the smallest common multiple of given numbers."
    run_game(generate_question, rules)


if __name__ == "__main__":
    play()
