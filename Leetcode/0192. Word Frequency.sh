# https://leetcode.com/problems/word-frequency/

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | xargs printf "%s\n" | sort | uniq -c | sort -nr | awk '{print $2,$1}'

# Input:
# the day is sunny the the
# the sunny is is
# Output:
# the 4
# is 3
# sunny 2
# day 1

# cat: prints out the file content
# xargs: apply function to each input
# sort: yes, sort
# uniq: -c is count it and output as "word cnt"
# sort: -nr is reversed sort
# awk: apply column rearrange