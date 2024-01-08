def show_messages(text):
    for item in text:
        print(item)


def send_messages(text):
    sent_messages = []
    print(text)
    while len(text):
        message = text.pop()
        sent_messages.append(message)
    print(sent_messages)
    print(text)


if __name__ == '__main__':
    text = ['哈哈', '嘿嘿']
    # show_messages(text)
    send_messages(text)
