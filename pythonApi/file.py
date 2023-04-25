with open("18887916.txt", "r") as file:
    text = file.read()

# Split the text into words and count their occurrences
word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Convert the dictionary to a list of tuples
word_count_tuples = list(word_counts.items())

# Define a custom sorting function
def sort_by_count(item):
    return item[1]

# Sort the list of tuples by count in descending order
for i in range(len(word_count_tuples)):
    for j in range(len(word_count_tuples) - i - 1):
        if sort_by_count(word_count_tuples[j]) < sort_by_count(word_count_tuples[j+1]):
            word_count_tuples[j], word_count_tuples[j+1] = word_count_tuples[j+1], word_count_tuples[j]

# Write the sorted words and their frequencies to a file
with open("word_count_report.txt", "w") as file:
    for item in word_count_tuples:
        word, count = item
        file.write(f"{word}: {count}\n")