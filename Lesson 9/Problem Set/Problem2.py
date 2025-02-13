import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)

    # read the high_score from the file
    with open("high_score.txt") as f:
        high_score = f.read()
        if high_score != "":
            high_score = int(high_score)
        else:
            high_score = 0

    print(f"Your score is {score}")

    if score > high_score:
        # write the high_score to the file
        with open("high_score.txt", "w") as f:
            f.write(str(score))

    return score

game()