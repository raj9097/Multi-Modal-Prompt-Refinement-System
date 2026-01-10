import os

def classify_inputs(inputs):
    classified = {
        "text": [],
        "image": [],
        "document": []
    }

    for item in inputs:
        if isinstance(item, str) and os.path.isfile(item):
            ext = item.lower().split(".")[-1]
            if ext in ["png", "jpg", "jpeg"]:
                classified["image"].append(item)
            elif ext in ["pdf", "docx"]:
                classified["document"].append(item)
        elif isinstance(item, str):
            classified["text"].append(item)

    return classified
