sentence = input("거꾸로 입력할 문자를 작성해주세요")
reverse_sentence = ''
for char in sentence:
    reverse_sentence = char + reverse_sentence
print(reverse_sentence)