history = []

def save_data(cv, result):
    history.append({
        "cv": cv,
        "result": result
    })

def get_history():
    return history
