from plyer import notification

def notify(problem):

    notification.notify(
        title="AI Coding Assistant",
        message=f"Today's problem: {problem['name']}\nHint: {problem['hint']}",
        timeout=15
    )