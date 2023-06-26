import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ]
]

chatbot = Chat(pairs, reflections)

while True:
    user_input = input("User: ")
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
    if user_input == "quit":
        break
