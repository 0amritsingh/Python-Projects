with open('Python-Projects\\P02 Madlibs Generator\\story.txt', 'r') as file:
    story = file.readlines()

new_story = []
for line in story:
    words = line.split(' ')
    for index, word in enumerate(words):
        if word[0] == '<':
            user_input = input(f'Enter {word}: ')
            words.remove(word)
            words.insert(index, user_input)
    new_story.append(' '.join(words) + '\n')
with open('Python-Projects\\P02 Madlibs Generator\\new_story.txt', 'w') as file:
    file.writelines(new_story)
        