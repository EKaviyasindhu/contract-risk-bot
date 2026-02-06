import streamlit as st
from src.loader import load_contract
from src.clause_splitter import split_clauses
from src.risk_engine import detect_risks, calculate_overall_risk
from src.summary import generate_summary
from src.audit import log_event
from src.llm_reasoning import explain_clause

st.set_page_config(page_title="Contract Risk Analysis Bot")

st.title("Contract Analysis & Risk Assessment Bot")
st.write("Upload a contract to analyze legal risks")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)


if uploaded_file:
    contract_text = load_contract(uploaded_file)
    clauses = split_clauses(contract_text)
    risks = detect_risks(clauses)

    overall_risk = calculate_overall_risk(risks)
    log_event(uploaded_file.name, overall_risk)

    st.subheader("📊 Overall Contract Risk")
    if overall_risk == "High":
        st.error("🔴 HIGH RISK CONTRACT")
    elif overall_risk == "Medium":
        st.warning("🟡 MEDIUM RISK CONTRACT")
    else:
        st.success("🟢 LOW RISK CONTRACT")

    st.subheader("Contract Summary")
    st.write(generate_summary(clauses, risks))

    st.subheader("Clause-by-Clause Analysis")

    for clause_id, clause_text in clauses.items():
        with st.expander(f"Clause {clause_id}"):
            st.write(clause_text)

            if clause_id in risks:
                for risk_name, risk_level in risks[clause_id]:
                    st.error(f"{risk_name} — {risk_level} Risk")

                    if st.button(f"Explain & Suggest Fix ({clause_id})",  key=f"explain_{clause_id}_{risk_name}_{risk_level}"):
                        explanation = explain_clause(clause_text, risk_name)
                        st.markdown("### AI Explanation & Recommendation")
                        st.write(explanation)
            else:
                st.success("No major risks detected")
