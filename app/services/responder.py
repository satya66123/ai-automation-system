def generate_response(category: str):
    responses = {
        "job": "Thank you for your interest. Please share your resume.",
        "internship": "We have internship opportunities. Please provide details.",
        "course": "Here are details about available courses.",
        "general": "Thank you for your message. We will get back to you."
    }

    return responses.get(category, "Thank you!")