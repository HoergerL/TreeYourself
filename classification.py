print('Import started')
from transformers import pipeline

print('Loading model')
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

tags = []
with open('tags') as file:
    for line in file:
        tags.append(line.strip('\n'))

topics = ['One Thing You Could Do Better', 'Things to Learn About', 'Improve Your Habits', 'Your Social Life in the Future',          'Your Leisure Activity in the Future', 'Your Family Life in the Future', 'Your Career in the Future',          'Qualities You Admire', 'The Ideal Future', 'A Future to Avoid']

#answers = ['Read more books.', 'More responsible Finances.', 'Eat less sweets.', 'Keep in touch with dear friends.', 'Workout more in gym.', 'Visit family more often.', 'Land dream job in IT.', 'Become better listener.', 'Family, with children and a picket fence.', 'Not prepared for unemployment.']
answers = [
    "I know that one thing I could do better is to manage my time more efficiently. There are days when I feel overwhelmed and struggle to balance my personal and professional responsibilities. I need to work on prioritizing my tasks and delegating when possible to avoid burnout and ensure that I'm making the most of my time.",
    "There are so many things that I want to learn about in order to broaden my perspective and deepen my understanding of the world. One area that I'm particularly interested in is learning more about different cultures and their customs. I also want to explore new subjects like philosophy and psychology, which I believe will help me to become a more well-rounded individual.",
    "I want to improve my daily habits so that I can live a healthier and more fulfilling life. This means making small changes like getting more exercise, eating a balanced diet, and practicing mindfulness. By making these habits a regular part of my routine, I know that I'll be able to improve my overall well-being and achieve my goals.",
    "In the future, I want to have a fulfilling social life that's filled with meaningful connections and experiences. This means surrounding myself with people who share my values and interests, and making time for fun activities like travel and trying new restaurants. I want to prioritize my relationships and create a community of like-minded individuals who support and inspire me.",
    "In the future, I want to continue pursuing my hobbies and interests, like reading, hiking, and painting. I believe that these activities are important for my personal growth and happiness, and I want to make sure that I'm always making time for them.",
    "Family is important to me, and I want to make sure that I'm building strong and supportive relationships with my loved ones. In the future, I hope to have a happy and healthy family life, filled with love, laughter, and cherished memories.",
    "In the future, I want to have a successful and fulfilling career that allows me to make a positive impact on the world. I hope to continue working in the field of data science, taking on leadership roles and tackling challenging projects that push me to grow and learn.",
    "There are many qualities that I admire in others, like kindness, resilience, and creativity. I strive to embody these qualities in my own life, and I believe that by doing so, I can make a positive impact on the world.",
    "My ideal future is one where I'm surrounded by love, happiness, and fulfillment. I hope to have a successful career, a supportive community, and a happy family life. I want to continue learning and growing as a person, and making a positive impact on the world.",
    "The future I want to avoid is one where I'm unfulfilled and unhappy. I don't want to settle for a career or lifestyle that doesn't bring me joy, and I don't want to surround myself with people who bring me down. I want to avoid a future where I'm stuck in a rut and not living up to my full potential."
]

relevant_tags = {}

print('Classifcation started')
for i, answer in enumerate(answers):
    results = classifier(answer, tags)
    temp = []
    for index, score in enumerate(results['scores']):
        if score >= 0.1:
            top_label = results['labels'][index]
            temp.append(top_label)
    relevant_tags[topics[i]] = temp

print(relevant_tags)


