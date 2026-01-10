import json
from refiner.input_classifier import classify_inputs
from refiner.text_processor import process_text
from refiner.image_processor import process_images
from refiner.document_processor import process_documents
from refiner.validator import validate_prompt
from refiner.prompt_template import build_prompt

def run(inputs):
    classified = classify_inputs(inputs)

    text_data = process_text(classified["text"])
    image_reqs = process_images(classified["image"])
    doc_reqs = process_documents(classified["document"])

    all_requirements = (
        text_data["requirements"] +
        doc_reqs +
        image_reqs
    )

    is_valid, reason = validate_prompt(text_data["problem_statement"])

    if not is_valid:
        return {
            "rejection_reason": reason
        }

    final_prompt = build_prompt(
        text_data["problem_statement"],
        all_requirements
    )

    return final_prompt


if __name__ == "__main__":
    sample_inputs = [
        "Build an AI tool that converts sketches into structured prompts",
        "samples\sample_text.txt",
    ]

    output = run(sample_inputs)
    print(json.dumps(output, indent=2))
