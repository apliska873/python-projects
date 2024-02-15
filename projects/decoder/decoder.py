

def decode(message_file):
    encoded_message = open(message_file, "r")
    words = dict()
    # fills a dictionary with the first number in every line as the key and the word as the value
    for line in encoded_message:
        split_line = line.split()
        words[int(split_line[0])] = split_line[1]
    encoded_message.close()
    # sorts the dictionary by the integer key
    sorted_encoded_message = dict(sorted(words.items()))

    # uses a step system similar to the staircase problem
    step = 1
    num = 0
    decoded_message = ""
    while num < len(sorted_encoded_message): # retrieve the last word from every step in the pyramid
        decoded_message += str(sorted_encoded_message.get(num + 1)) + " " # add the word to the result string
        step += 1
        num += step     # update target key

    return decoded_message


print(decode("coding_qual_input.txt").lower())
