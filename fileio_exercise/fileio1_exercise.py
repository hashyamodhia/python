word_stats = {}

file = open("poem.txt", "r")
for line in file:
    words = line.split(" ")
    for word in words:
        if word in word_stats:
            word_stats[word] += 1
        else:
            word_stats[word] = 1
print(word_stats)

word_occurances = list(word_stats.values())
# print(word_occurances)
max_count = max(word_occurances)
print("\nMaximum word count is:", max_count)

print("Words with maximum occurance: ")

for word, count in word_stats.items():
    if count == max_count:
        print(word)

file.close()