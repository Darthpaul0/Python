msg = input(">")
message = msg.split(' ')

emojis = {
    ":)": "🙂",
    ":(": "😢",
}

output = ""
for word in message:
    output += emojis.get(word, word) + " "

print(output)
