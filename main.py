import schedule
import time

from ai_brain import select_problem, generate_code
from automation import open_platforms
from github_worker import commit_code
from tracker import track
from notifier import notify

def run_ai():

    problem = select_problem()

    notify(problem)

    open_platforms()

    code = generate_code(problem)

    commit_code(code)

    track(problem)

    print("AI Assistant completed today's tasks")

schedule.every().day.at("10:00").do(run_ai)

print("AI Assistant running...")

while True:

    schedule.run_pending()

    time.sleep(60)