from transformers import pipeline


def tag_answers(answers, tags):
    classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
    
    relevant_tags = {}

    for answer in answers:
        results = classifier(answer, tags)
        for index, score in enumerate(results['scores']):
            if score >= 0.1:
                relevant_tags.setdefault(results['labels'][index], [])
                relevant_tags[results['labels'][index]].append(answer)

    return relevant_tags



tags = []
with open('tags') as file:
    for line in file:
        tags.append(line.strip('\n'))

answers = ['Read more books.', 'More responsible Finances.', 'Eat less sweets.', 'Keep in touch with dear friends.', 'Workout more in gym.', 'Visit family more often.', 'Land dream job in IT.', 'Become better listener.', 'Family, with children and a picket fence.', 'Not prepared for unemployment.']

result = tag_answers(answers=answers, tags=tags)
print(result)