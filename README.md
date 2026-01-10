Multi-Modal Prompt Refinement System

A system that accepts text, images, documents, or any combination and refines them into a standardized, validated, AI-ready prompt format suitable for downstream AI processing.

This project emphasizes design thinking, validation, and reliability when working with Large Language Models (LLMs).

🎯 Objective

Modern AI systems receive inputs in many formats—free-text ideas, screenshots, sketches, and PDFs.
Downstream AI pipelines, however, require consistent, structured, and machine-readable prompts.

This project aims to:

Normalize diverse multi-modal inputs

Preserve intent, requirements, and constraints

Handle ambiguity explicitly

Prevent LLM hallucinations using validation guardrails

🧩 Key Features

✅ Multi-modal input support (Text, Image, PDF, DOCX)

✅ Structured JSON output

✅ Schema-based validation using Pydantic

✅ Explicit ambiguity handling

✅ Rejection of irrelevant inputs

✅ Two execution modes (UI & Terminal)

🏗️ System Architecture
Input (Text / Image / Document)
        ↓
Input Classification
        ↓
Modality-Specific Processing
        ↓
Intent Consolidation
        ↓
Validation (Pydantic Guardrail)
        ↓
Structured AI-Ready Prompt


Design Principle:
The LLM is treated as an untrusted component and validated deterministically.

📁 Project Structure
multi_modal_prompt_refiner/
│
├── main.py        # Streamlit UI entry point
├── main2.py       # Terminal execution entry point
│
├── refiner/
│   ├── input_classifier.py
│   ├── text_processor.py
│   ├── image_processor.py
│   ├── document_processor.py
│   ├── validator.py        # Validation Guardrail (Pydantic)
│   └── prompt_template.py
│
├── samples/
│   ├── sample_text.txt
│   └── sample_image.png
│
├── requirements.txt
└── README.md


▶️ How to Run the Project
1️⃣ Create and Activate Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate


You should see (venv) in your terminal.

2️⃣ Install Dependencies
pip install -r requirements.txt

🔹 Option 1: Run Using Streamlit (UI Mode)

Best for:

Interactive demos

Reviewers

Multi-modal testing via browser

streamlit run main.py


The app opens automatically in your browser.

🔹 Option 2: Run Using Terminal (Script Mode)

Best for:

Quick testing

Debugging

Automation

python main2.py


The refined prompt is printed as structured JSON in the terminal.

🧪 Sample Inputs

Sample files are available in the samples/ directory:

sample_text.txt

sample_image.png

These are used in both UI and terminal modes.

⚠️ Notes for Windows Users

Always use:

python


Avoid using python3, which may bypass the virtual environment.

📤 Output Format
Successful Output
{
  "core_intent": "...",
  "functional_requirements": [...],
  "technical_constraints": {...},
  "expected_outputs": {...}
}

Rejection Output
{
  "rejection_reason": "No clear actionable intent found"
}

🔐 Validation as a Guardrail (Key Design Choice)

The core reliability mechanism lives in refiner/validator.py.

Why Pydantic?

Guarantees machine-readable output

Prevents hallucinated or incomplete fields

Enforces strict schema contracts

Fails explicitly and safely

The LLM is probabilistic. Validation must be deterministic.

🧠 Handling Ambiguity & Missing Information
Scenario	System Behavior
Missing details	Marked as Unknown
Ambiguous intent	Best-guess + documented assumption
Conflicting inputs	Text > Document > Image
No clear intent	Prompt rejected
🤝 AI Usage vs Original Contribution
AI-Assisted

Language refinement

API usage references

Brainstorming

Original Contribution

System architecture

Refinement pipeline

Validation strategy

Schema design

Rejection logic

Assumption handling

AI was used as a tool, not a decision-maker.

🚀 Future Enhancements

OCR for scanned PDFs

Confidence scoring per field

FastAPI backend wrapper

Persistent storage

Advanced LLM summarization

✅ Conclusion

This project demonstrates:

Structured problem-solving

Responsible AI usage

Validation-first mindset

Production-ready design thinking

The focus is not just on making it work, but on making it reliable, explainable, and safe.