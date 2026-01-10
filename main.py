import streamlit as st
import json
import os

# Import your logic
from refiner.input_classifier import classify_inputs
from refiner.text_processor import process_text
from refiner.image_processor import process_images
from refiner.document_processor import process_documents
from refiner.validator import validate_prompt
from refiner.prompt_template import build_prompt

# Page Configuration
st.set_page_config(page_title="DignifiedMe Refiner", layout="wide")

def run_refinement(inputs):
    """
    Orchestrates the refinement process:
    Classify -> Process -> Validate -> Build
    """
    # 1. Classify Inputs
    classified = classify_inputs(inputs)

    # 2. Process Data
    text_data = process_text(classified["text"])
    image_reqs = process_images(classified["image"])
    doc_reqs = process_documents(classified["document"])

    # 3. Aggregate Requirements
    all_requirements = (
        text_data["requirements"] +
        doc_reqs +
        image_reqs
    )

    # 4. Validate
    is_valid, reason = validate_prompt(text_data["problem_statement"])

    if not is_valid:
        return {
            "is_rejected": True,
            "rejection_reason": reason
        }

    # 5. Build Final JSON
    final_prompt = build_prompt(
        text_data["problem_statement"],
        all_requirements
    )
    return final_prompt

# --- Streamlit UI Layout ---
def main():
    st.title("🚀 Multi-Modal Prompt Refinement System")
    st.markdown("### Transform chaotic inputs into structured specs")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Input Context")
        user_text = st.text_area("Describe your idea:", height=200, placeholder="E.g., I want a food delivery app...")
        
        uploaded_files = st.file_uploader(
            "Upload Assets (Sketches, PDFs)", 
            type=["png", "jpg", "jpeg", "pdf"],
            accept_multiple_files=True
        )

        refine_btn = st.button("Refine Prompt", type="primary")

    with col2:
        st.subheader("2. Refined Output")
        
        if refine_btn:
            # Prepare inputs for your logic
            inputs_list = []
            
            # Add text if it exists
            if user_text:
                inputs_list.append(user_text)
            
            # Add files if they exist
            if uploaded_files:
                # Streamlit file objects need to be handled carefully. 
                # Ideally, save them temp or pass the bytes. 
                # For this prototype, we pass the file objects directly if your processors handle them,
                # OR we might need to save them temporarily.
                # Assuming your processors expect file paths or bytes:
                inputs_list.extend(uploaded_files)

            if not inputs_list:
                st.warning("⚠️ Please provide text or upload a file.")
            else:
                with st.spinner("Analyzing multi-modal inputs..."):
                    try:
                        # Run your main logic
                        result = run_refinement(inputs_list)
                        
                        # Display Result
                        if result.get("is_rejected"):
                            st.error(f"❌ Request Rejected: {result.get('rejection_reason')}")
                        else:
                            st.success("✅ Refinement Complete")
                            st.json(result)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()