def validate_prompt(core_intent):
    if not core_intent or len(core_intent.strip()) < 10:
        return False, "No clear actionable intent found"
    return True, None
