import re
def split_sentence(text):
    sentences = re.split('[.!?]',text)
    word_count = [ len(sentence.split()) for sentence in  sentences ]
    return max(word_count)

print(split_sentence('Forget CVs..Save time . x x'))