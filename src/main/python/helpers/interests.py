import random
from typing import Dict, List


class Interests:
    @staticmethod
    def get_all() -> List[List[str]]:
        all = []
        for interest in [Culture, Sports, Science]:
            for person in interest.persons:
                all.append(person)
            for topic in interest.topics:
                all.append(topic)

        # random.shuffle(all)
        return all


# CULTURE
class Culture:
    persons = [
        ['kamal', 'ravikant'],
        ['carl',  'sagan'],
        ['malcolm', 'gladwell'],
        ['dan', 'brown'],
        ['tim', 'ferris'],
        ['lex', 'fridman'],
    ]
    topics = [
        ['sleep'],
        ['meditation'],
        ['yoga'],
        ['latest', 'movies']
    ]


# SPORTS
class Sports:
    persons = []
    topics = [
        ['formula', 'one'],
        ['cycling'],
        ['cyclisme'],
        ['triathlon'],
        ['running'],
        ['bouldering'],
    ]


# SCIENCE
class Science:
    persons = []
    topics = [
        ['natural', 'language', 'processing'],
        ['pytorch'],
        ['tensorflow'],
        ['papers', 'with', 'code'],
        ['transformers'],
        ['huggingface'],
    ]


if __name__ == "__main__":
    kwords = Interests.get_all()
    print(kwords)
