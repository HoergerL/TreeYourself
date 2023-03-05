from transformers import pipeline


def tags_from_answers(answers, tags):
    classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
    
    relevant_tags = {}

    for answer in answers:
        results = classifier(answer, tags)
        for index, score in enumerate(results['scores']):
            if score >= 0.08:
                relevant_tags.setdefault(results['labels'][index], [])
                relevant_tags[results['labels'][index]].append(answer)

    return relevant_tags