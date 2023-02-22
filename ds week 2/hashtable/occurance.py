def word_count(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
srt = 'the quick brown fox jumps over the lazy dog'
print(word_count(srt))