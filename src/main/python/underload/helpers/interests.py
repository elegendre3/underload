import random
from typing import Dict, List, Tuple


class Interests:
    @staticmethod
    def get_all() -> List[Tuple[List[str], List[str]]]:
        all = []
        for (interest, tag) in [(Culture, ['culture']), (Sports, ['sports']), (Science, ['science']), (Persons, ['person'])]:
            for topic in interest.topics:
                all.append((topic, tag))
        return all


# PERSONS
class Persons:
    topics = [
        ['kamal', 'ravikant'],
        ['carl', 'sagan'],
        ['malcolm', 'gladwell'],
        ['dan', 'brown'],
        ['tim', 'ferris'],
        ['lex', 'fridman'],
        ['thomas', 'piketty'],
        ['sylvain', 'tesson'],
    ]


# CULTURE
class Culture:
    topics = [
        ['sleep'],
        ['meditation'],
        ['yoga'],
        ['latest', 'movies'],
        ['nutrition'],
        ['life', 'balance'],
        ['reading'],
        ['cooking'],
    ]


# SPORTS
class Sports:
    topics = [
        ['formula', 'one'],
        ['cycling', 'cyclisme'],
        ['triathlon'],
        ['running'],
        ['rock', 'climbing'],
        ['motorsport']
    ]


# SCIENCE
class Science:
    topics = [
        ['natural', 'language', 'processing'],
        ['neural', 'networks'],
        ['pytorch', 'tensorflow'],
        ['papers', 'with', 'code'],
        ['transformers'],
        ['huggingface'],
    ]


if __name__ == "__main__":
    kwords = Interests.get_all()
    print(kwords)
