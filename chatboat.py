# Simple chatboat using python
 
import random #import random module
def simple_chatboat():
    print("Hello! i am saloni soni. Type 'exit' to end the conversation.")
    while True:
        chat_input=input("you:").lower()
        if chat_input=='exit':print("Goodbye ! Have a great day.")
        else:
            response=get_response(chat_input)
            print(f"Bot :{response}")
def get_response(chat_input):
    greeting=['Hello!','Hi there!','Greetings!']
    farewells=['Goodbye!','See you later!','Take care!']
    if 'how are you' in chat_input:
        return "I'am just a bot, but thanks for asking"
    elif 'name' in  chat_input:
        return  "I'am your friendly chatboat!"
    elif 'bye' in chat_input:
        return random.choice(farewells)
    else:
        return "I'am not sure how to responde to that. Feel free to ask something else"
simple_chatboat()




