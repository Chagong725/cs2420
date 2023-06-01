'''
Project:
Author: 
Course: 
Date: 

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST

class Pair:
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    tree = BST()
    filepath = 'around-the-world-in-80-days-3.txt'
    with open(filepath, 'r') as file:
        for line in file:
            for char in line:
                char = char.lower()
                if char not in whitespace and char not in punctuation:
                    try:
                        searched_pair = tree.find(Pair(char))
                        searched_pair.count += 1
                    except ValueError:
                        tree.add(Pair(char))
    return tree

def main():
    tree = make_tree()
    tree.print_tree()

if __name__ == "__main__":
    main()

