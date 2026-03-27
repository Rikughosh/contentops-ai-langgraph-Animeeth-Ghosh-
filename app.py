import streamlit as st
from workflows.langgraph_pipeline import run_langgraph
from evaluation.scorer import evaluate_content
from auth.roles import get_role_permissions
import json

st.set_page_config(layout="wide")
st.title("🚀 ContentOps AI Pro")

role = st.sidebar.selectbox("Role", ["Admin", "Reviewer"])
permissions = get_role_permissions(role)

idea = st.sidebar.text_area("Content Idea")
language = st.sidebar.selectbox("Language", ["Hindi", "Bengali"])
content_type = st.sidebar.selectbox("Type", ["LinkedIn Post", "Blog"])

if "generate" in permissions:
    if st.sidebar.button("Run Pipeline"):
        result = run_langgraph(idea, language, content_type)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Draft")
            st.write(result.get("draft"))
            st.subheader("Localized")
            st.write(result.get("localized"))

        with col2:
            st.subheader("Evaluation")
            score_raw = evaluate_content(result.get("localized", ""))
            try:
                score = json.loads(score_raw)
                for k, v in score.items():
                    st.metric(k, v)
            except:
                st.write(score_raw)

        if "publish" in permissions:
            st.subheader("Publishing")
            st.json(result.get("publish_result"))

        st.success("Done")
