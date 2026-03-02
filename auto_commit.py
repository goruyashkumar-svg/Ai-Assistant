import os
import random
from datetime import datetime

# motivational lines
messages = [
    "Practicing data structures",
    "Improving problem solving skills",
    "Working on AI assistant project",
    "Learning machine learning",
    "Improving coding consistency",
    "Daily coding practice"
]

def make_commit():

    today = datetime.now().strftime("%Y-%m-%d")
    
    filename = f"daily_progress_{today}.txt"
    
    message = random.choice(messages)
    
    # create or append file
    with open(filename, "a") as f:
        f.write(f"{today}: {message}\n")
    
    # git commands
    os.system("git add .")
    os.system(f'git commit -m "AI Assistant auto commit {today}"')
    os.system("git push")
    
    print("GitHub auto commit done")

make_commit()