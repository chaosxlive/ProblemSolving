text = "47%50%53%43%54%46%7b%30%65%32%38%33%64%64%37%64%63%37%63%31%64%38%62%39%66%37%38%65%61%31%36%62%30%32%62%32%30%38%33%7d"
text = "".join(text.split('%'))
result = []
for i in range(0, len(text), 2):
    result.append(chr(int(text[i:i + 2], 16)))
print("".join(result))