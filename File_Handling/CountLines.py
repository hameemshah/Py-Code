output_file = open('abc.txt', 'r')
char_count = 0
line_count = 0
word_count = 0
for line in output_file:
    line_count += 1
    word_count += len(line.split())
    char_count += len(line)
output_file.close()
print("Characters =", char_count, "Lines =", line_count, "Words =", word_count)