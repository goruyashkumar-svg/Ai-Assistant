import os
from datetime import datetime

def commit_code(code):

    filename = f"daily_{datetime.now().date()}.py"

    with open(filename, "w") as f:
        f.write(code)

    os.system("git add .")
    os.system(f'git commit -m "AI Assistant commit {datetime.now().date()}"')
    os.system("git push")