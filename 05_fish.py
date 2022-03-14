import utils

# Load questions
questions_file = '05_questions.json'
questions = utils.open_json(questions_file)

# Set results for each option
answers = {
    'A': {'text': 'Вы — стайная селедка.', 'count': 0},
    'B': {'text': 'Вы — задумчивая камбала.', 'count': 0},
    'C': {'text': 'Вы — активная щука.', 'count': 0},
    'Непонятно': {'text': 'Мы не смогли определить, кто вы. Будете лещом!', 'count': 1}
}

# Ask questions and collect results
for question in questions:
    # print(question['text'])
    # print(question['options'])
    print(
        f'\n{question["text"]}\n'
        f'A. {question["options"]["А"]}\n'
        f'B. {question["options"]["B"]}\n'
        f'C. {question["options"]["C"]}\n'
    )

    user_input = input('Введите вариант: ').upper()
    answers[user_input]['count'] += 1

# Calculate and print results

result = answers['Непонятно']['count']
result_text = answers['Непонятно']['text']

for keys, values in answers.items():
    if values['count'] > result:
        result_text = values['text']
        result = values['count']

print(result_text)
print(answers)
