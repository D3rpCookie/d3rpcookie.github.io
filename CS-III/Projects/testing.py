import sys
words_list = []
for line in sys.stdin:
        words_list.append(line.replace("\n", ""))
words_list.sort()
print(words_list)
