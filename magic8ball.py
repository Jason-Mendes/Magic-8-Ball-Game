# Magic 8-Ball Game
# The code below is a simple implementation of a Magic 8-Ball game.
# The user is prompted to ask a yes or no question, and the program randomly selects an answer from a predefined list of responses.
# The selected answer is then printed to the console.
# The game is a fun way to simulate fortune-telling or decision-making, and the randomness adds an element of surprise.

import random

Question = input("Ask a yes or no question please " "\n"
"What's your question: ")

answers = [
    "Yes - definitely.",
    "It is decidedly so.", 
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

Answer = random.choice(answers)
print("Magic 8-Ball: " + Answer)
