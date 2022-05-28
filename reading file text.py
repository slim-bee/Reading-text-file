# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(str):
    # [assignment] Add your code here
    counts = dict()
    words = str.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            #return "Hello World"
    return counts

def count_words():
    text = read_file_content(str)
    #[assignment] add your code here

    #return {"as": 10, "would": 20}

file = open("story.txt", "r")


data = file.read()


print( read_file_content(data))
