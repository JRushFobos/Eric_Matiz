messages = ['hello','bye','buy','sell','tell']
sent_message = []


def send_message (messages,sent_message):
    print(messages)
    print(sent_message)

    while messages:
        current_message = messages.pop()
        print(current_message.title())
        sent_message.append(current_message)
    
    print(messages)
    print(sent_message)

send_message (messages,sent_message)
