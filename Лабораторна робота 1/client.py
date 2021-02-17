from nltk.parse.corenlp import CoreNLPParser
from nltk.tree import Tree
from rules_handler import load_rules, handler

parser = CoreNLPParser()


def get_tree(sent: str) -> Tree:
    return next(parser.raw_parse(sent))

# Example phrases:
# "How can I get to the store?"
# "Where is the station?
# "What time is it?"

if __name__ == '__main__':

    rules = load_rules("patterns.json")

    while True:
        request = input("Question: ")
        print("Response:", end=" ")
        if request == "Bye" or request == "Good bye":
            print("Have a good day!")
            break
        tree = get_tree(request)
        response = handler(tree, rules)
        print(response)
