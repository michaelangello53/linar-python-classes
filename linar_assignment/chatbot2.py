from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

while True:
    user_input = input("User: ")
    response = chatbot.get_response(user_input)
    print("ChatBot:", response)

    if user_input.lower() == 'bye':
        break
