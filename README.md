# 📄 Contract Risk Analysis Bot

## Problem Statement
Small businesses often sign contracts without fully understanding hidden legal risks due to lack of legal expertise.

## Solution
We built a **GenAI-powered Contract Risk Analysis Bot** that:

- Accepts real contracts (PDF / DOCX / TXT)
- Extracts and splits contracts into clauses
- Detects risky legal clauses
- Computes clause-level and overall contract risk
- Provides explainable AI–ready reasoning and safer clause suggestions
- Maintains confidentiality through local processing and metadata-only audit logs

## Key Features
- Clause-level risk detection (indemnity, termination, non-compete, jurisdiction)
- Overall contract risk scoring
- Explainable AI design using GPT-4–class models
- Graceful fallback when AI access is unavailable
- Streamlit-based interactive UI
- Confidential, offline-first architecture

## Tech Stack
- Python
- Streamlit
- Rule-based NLP
- OpenAI-compatible GenAI architecture
- Local JSON audit logging

## Why This Matters
The solution helps SMEs make informed legal decisions quickly, reduces dependency on legal consultations, and improves contract transparency.

## Live Demo
👉 **Streamlit App URL:**  
[_Paste your Streamlit live link here_](https://contract-risk-bot-bmfzhgzbjhx4nmceveqz5v.streamlit.app/)
