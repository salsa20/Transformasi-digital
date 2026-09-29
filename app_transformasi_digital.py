import streamlit as st

st.set_page_config(
    page_title="Pertemuan | Transformasi Digital",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
.hero {
    padding: 2rem;
    border-radius: 22px;
    background: linear-gradient(135deg, #f6f8ff 0%, #eefaf7 100%);
    border: 1px solid rgba(120,120,120,.18);
    margin-bottom: 1.2rem;
}
.hero h1 {
    margin: 0 0 .4rem 0;
    font-size: 2.35rem;
}
.hero p {
    font-size: 1.05rem;
    margin: 0;
    opacity: .82;
}
.card {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    background: rgba(255,255,255,.65);
}
.small-card {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 16px;
    padding: 1rem;
    min-height: 120px;
}
.flow {
    border-radius: 16px;
    padding: 1rem 1.1rem;
    background: rgba(120,120,120,.06);
    border: 1px dashed rgba(120,120,120,.35);
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    line-height: 1.75;
}
.badge {
    display: inline-block;
    padding: .28rem .7rem;
    border-radius: 999px;
    border: 1px solid rgba(120,120,120,.25);
    margin: .15rem .2rem .15rem 0;
    font-size: .86rem;
}
.note {
    padding: 1rem 1.1rem;
    border-left: 5px solid #6c63ff;
    background: rgba(108,99,255,.08);
    border-radius: 12px;
}
.quiz-box {
    border: 1px solid rgba(120,120,120,.22);
    border-radius: 18px;
    padding: 1.15rem;
    margin-bottom: 1rem;
}
.case-box {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 18px;
    padding: 1.2rem;
    background: rgba(255,255,255,.55);
    margin-bottom: 1rem;
}
div[data-testid="stMetric"] {
    border: 1px solid rgba(120,120,120,.16);
    padding: .8rem;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Data
# -----------------------------
quiz = [
    {
