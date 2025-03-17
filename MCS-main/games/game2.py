import random
from MCS.games.engine import run_game


def generate_progression(length, start, ratio):

    return [start * (ratio ** i) for i in range(length)]


def hide_element(progression):

    index = random.randint(0, len(progression) - 1)
    hidden_value = progression[index]
    progression[index] = ".."
    return progression, hidden_value


def generate_question():

    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression, hidden_value = hide_element(generate_progression(length, start, ratio))
    question = " ".join(map(str, progression))
    return question, hidden_value


def play():

    rules = "What number is missing in the progression?"
    run_game(generate_question, rules)


if __name__ == "__main__":
    play()
