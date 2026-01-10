def process_text(texts):
    requirements = []

    for text in texts:
        sentences = text.split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 10:
                requirements.append({
                    "requirement": sentence,
                    "priority": "Medium",
                    "source": "Text"
                })

    return {
        "problem_statement": texts[0] if texts else "",
        "requirements": requirements
    }
