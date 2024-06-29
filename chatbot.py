import re
from datetime import datetime

def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
       
        user_input = input("You: ").strip().lower()
        
       
        if user_input in ["bye", "quit", "exit"]:
            print("Chatbot: See you later!")
            break
        
        
        elif re.search(r'\b(hi|hello|hey|greetings|what\'s up|howdy)\b', user_input):
            print("Chatbot: Hi there! How can I assist you?")
        
        elif re.search(r'\b(tell me a joke|can you tell me a joke)\b', user_input):
            print("Chatbot:  Did you hear about the first restaurant to open on the moon?It had great food, but no atmosphere.")
             
        elif re.search(r'\b(bye|goodbye|see you|later|take care)\b', user_input):
            print("Chatbot: Goodbye! Have a great day!")    
            break
        
        elif re.search(r'\b(how are you|how\'s it going|how do you do|what\'s new)\b', user_input):
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking! How can I assist you?")
        
       
        elif re.search(r'\b(what can you do|your capabilities|what are you capable of)\b', user_input):
            print("Chatbot: I can answer simple questions, tell you the time and date, and have basic conversations. I'm still under development!")
        
        
        elif re.search(r'\b(what time is it|current time|time now)\b', user_input):
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}.")
        
        
        elif re.search(r'\b(what is the date|current date|today\'s date)\b', user_input):
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {today}.")
        
       
        elif re.search(r'\b(weather|what\'s the weather|current weather)\b', user_input):
            print("Chatbot: I currently cannot provide weather updates. Please check a weather website or app.")
        
        elif re.search(r'\b(who is|what is|where is|tell me about)\b', user_input):
            print("Chatbot: I'm not equipped to answer general knowledge questions in detail. You might want to look that up online.")
        
        
        elif re.search(r'\b(thank you|thanks)\b', user_input):
            print("Chatbot: You're welcome! Is there anything else I can help with?")
        
        
        elif re.search(r'\b(yes|yeah|sure|ok|okay)\b', user_input):
            print("Chatbot: Great! How can I assist you further?")
        
        
        elif re.search(r'\b(no|nope|nah)\b', user_input):
            print("Chatbot: Alright, let me know if there's anything else you need.")
        
        
        else:
            print(f"Chatbot: I'm not sure I understand what you mean by '{user_input}'.")
            print("Chatbot: Could you please rephrase or ask something else?")


chatbot()