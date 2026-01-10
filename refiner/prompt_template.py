def build_prompt(core_intent, requirements):
    return {
        "prompt_metadata": {
            "confidence_level": "Medium",
            "missing_information": [],
            "assumptions_made": [
                "Image-based requirements are inferred heuristically"
            ]
        },
        "core_intent": {
            "problem_statement": core_intent,
            "primary_goal": "Refined AI-ready prompt generation"
        },
        "functional_requirements": requirements,
        "technical_constraints": {
            "platform": "Unknown",
            "performance_constraints": "Unknown",
            "design_constraints": "Unknown"
        },
        "expected_outputs": {
            "deliverables": ["Structured prompt"],
            "format": "JSON"
        },
        "rejection_reason": None
    }
