def emoji_converter(message):
    message = msg.split(' ')

    emojis = {
        ":)": "🙂",
        ":(": "☹",
    }

    output = ""
    for word in message:
        output += emojis.get(word, word) + " "
    return output


msg = input(">")
print(emoji_converter(msg))
