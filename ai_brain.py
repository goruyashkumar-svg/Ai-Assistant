import random

# list of problems
easy_problems = [
    {
        "name": "Two Sum",
        "hint": "Use a dictionary to store visited numbers and check complement."
    },
    {
        "name": "Palindrome Number",
        "hint": "Reverse the number and compare with original."
    },
    {
        "name": "Valid Parentheses",
        "hint": "Use stack data structure."
    },
    {
        "name": "Maximum Subarray",
        "hint": "Use Kadane's algorithm."
    }
]

# function to select problem
def select_problem():
    return random.choice(easy_problems)

# function to generate starter code
def generate_code(problem):

    code = f'''
# Problem: {problem["name"]}

def solution():
    print("Solving problem: {problem["name"]}")

solution()
'''

    return code