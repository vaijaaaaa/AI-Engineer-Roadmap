message = input(">")

def play():
    words = message.split(' ')
    emojis = {
        ":)" : "😁",
        "):" : "🙌"
    }

    output = ""

    for word in words:
        output += emojis.get(word,word) + " "
    return output

print(play())