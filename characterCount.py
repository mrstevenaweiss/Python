
import pprint

def charCount(message):
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    return count


while True:
    print("Drop a sentence in here and see it\'s letter count: (Type 'exit' to exit) ")
    sentence = input()

    if sentence == 'exit':
        break
    else:
        print(charCount(sentence))
        print("\n")
