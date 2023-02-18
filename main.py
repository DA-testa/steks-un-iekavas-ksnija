# python3 Ksenija Žuka, 221RDC024

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()    
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else: 
         return "Success"


def main():
    content = input()
    if "I" in content:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

    elif "F" in content:
        pass
    else:
        print("Jūsu tekstam jābūt I vai F burtam")

    main()
