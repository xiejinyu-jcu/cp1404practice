"""
Word Occurrences
Estimate: 25 minutes
Actual:   37 minutes
"""
word_counts={}
text=input("Text: ")
words = text.split()
for word in words:
    if word in word_counts:
       word_counts[word]+=1
    else:
       word_counts[word]=1
sorted_words=sorted(word_counts.keys())
max_length=max(len(word)for word in word_counts)
for word in sorted_words:
    print(f"{word:{max_length}}:{word_counts[word]:2}")