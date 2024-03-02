def to_title_case(s):
    words = s.split()
    title_case = []
    for word in words:
        if word.isupper():  # Acronym remains unchanged
            title_case.append(word)
        else:
            title_case.append(word.capitalize())
    return ' '.join(title_case)

t = int(input())
for _ in range(t):
    s = input()
    print(to_title_case(s))
