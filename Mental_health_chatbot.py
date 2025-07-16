import random
import time

# Welcome message
print("👋 Hello! I'm your Mental Health Support Chatbot.")
print("I'm here to listen and support you. Let's talk.")
print("You can type 'exit' anytime to end the conversation.\n")

# Predefined user inputs and responses
responses = {
    "i feel sad": "I'm really sorry you're feeling this way. Want to talk more about what's making you sad?",
    "i am depressed": "You are not alone. Talking about it is the first step. Would you like some coping tips?",
    "i feel anxious": "Anxiety can be overwhelming. Let's take a deep breath together. Inhale... Exhale... Feel better?",
    "i am stressed": "Stress is tough. Taking short breaks and talking to someone can help. Want some relaxation tips?",
    "i need help": "Of course. I'm here for you. Would you like to speak with a mental health professional?",
    "thank you": "You're very welcome. I'm always here for you.",
    "i am lonely": "Loneliness can feel heavy. You're not alone. I'm here with you right now. Want to talk more?",
    "i can't sleep": "Sleep issues are common with stress. Would you like some sleep hygiene tips?",
    "i feel angry": "It's okay to feel angry. Would you like some ways to calm down?",
}

# Default responses
default_responses = [
    "I understand. Please tell me more.",
    "That sounds tough. I'm here to support you.",
    "Would you like to talk about something specific?",
    "You can share anything with me.",
    "I'm listening... take your time.",
]

# Function to simulate typing effect
def slow_type(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

# Chat loop
while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        slow_type("💬 It was good talking to you. Take care of yourself. Goodbye! 💚")
        break
    elif user_input in responses:
        slow_type("Bot: " + responses[user_input])
    else:
        slow_type("Bot: " + random.choice(default_responses))