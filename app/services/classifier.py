def classify_message(message: str):
    message = message.lower()

    if "job" in message:
        return "job"
    elif "internship" in message:
        return "internship"
    elif "course" in message:
        return "course"
    else:
        return "general"