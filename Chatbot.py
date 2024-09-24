def chatbot_response(user_input):
    responses = {
        "hi": "hello! how can i help you",
        "bye": "goodbye! have a nice day",
        "how are you": "i'm just a bunch of code, but i'm doing well",
        "help": "sure! i will do my best",
        "fix": "sure i will",
        "menu": "\n account details",
        "bank acc.":"\n bank account details",
        "my details":"\n name: \n fathers name: \n college: \n roll no: \n d.o.b:"
    }
    for key in responses.keys():
        if key in user_input.lower():
            return responses[key]
    return "sorry, i don't understand that."

while True:
    user_input = input("you: ")
    if user_input.lower() == "exist":
        break
    print("chatbot:",chatbot_response(user_input))
