from collections import Counter
from typing import List

'''
Generating DAIDE syntax
The eval process:
1. Clean the data, including
    - remove newline and "." generated by the few-shot model
    - remove duplicate DAIDE orders
    - remove invalid DAIDE orders
    - reformat the text file

2. Compute the accuracy
    - remove parentheses
    - get a list of DAIDE tokens for reference and translation
    - compute the overlap between the two lists (the order of the tokens does not matter)
    - compute the precision, recall and f-score

Problems of the few-shot model encountered when cleaning the data:
1. Incorrectly inserted "." and newline
2. Generate multiple orders
3. Generate invalid DAIDE syntax (missing parentheses, invalid tokens, etc.)
4. Generates English to complete the English sentence (e.g., when the sentence ends with 
    prepositions), and include that in the generated DAIDE orders
5. Fail to infer the message sender and receiver (although it's impossible without looking at
    AMR or the order)
'''

# remove punctuations and use lowercase
def tokenize(sentence: str) -> List[str]:
    def trim_all(token: str) -> str:
        while token[0] == '"' or token[0] == '(' or token[0] == ' ':
            token = token[1:]
        while token[-1] == '"' or token[-1] == '.' or token[-1] == ',' or token[-1] == ')' or token[-1] == ' ':
            token = token[:-1]
        return token

    words = sentence.split(' ')
    tokens = []
    for word in words:
        lowercase = word.lower()
        trimmed = trim_all(lowercase)
        tokens.append(trimmed)
    return tokens

# remove parentheses
def trim(token: str) -> str:
    while token.startswith('('):
        token = token[1:]
    while token.endswith(')'):
        token = token[:-1]
    return token

def compute_accuracy(reference: str, translation: str) -> float:
    translated_tokens = translation.split(' ')
    reference_tokens = reference.split(' ')
    trimmed_translated_tokens = [trim(token) for token in translated_tokens]
    trimmed_reference_tokens = [trim(token) for token in reference_tokens]

    # precision = correct / output-length
    # recall = correct / reference-length
    # f = p * q * 2 / (p + q)
    correct = list((Counter(trimmed_reference_tokens) & Counter(trimmed_translated_tokens)).elements())
    overlap = len(correct)
    # return if denom is 0
    if overlap == 0:
        return 0
    precision = overlap / len(trimmed_translated_tokens)
    recall = overlap / len(trimmed_reference_tokens)
    f = precision * recall * 2 / (precision + recall)
    return round(f, 3)

def read_file():
    print()

if __name__ == '__main__':
    lines = read_file()
    