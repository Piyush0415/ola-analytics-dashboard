import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ola Analytics Dashboard", layout="wide")

# -------------------------------------------------
# FUNCTION TO LOAD SQL FILE
# -------------------------------------------------

def load_sql_queries():
    with open("queries.sql", "r") as file:
        sql_text = file.read()
    return sql_text


# -------------------------------------------------
# CUSTOM SIDEBAR STYLE
# -------------------------------------------------

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #0f172a;
    padding-top:5px;
}

[data-testid="stSidebar"] * {
    color: white;
}

.sidebar-title {
    font-size:22px;
    font-weight:bold;
    margin-bottom:5px;
}

.section-title {
    font-size:15px;
    font-weight:bold;
    margin-top:10px;
    margin-bottom:3px;
}

div.stButton > button {
    width:100%;
    margin-top:2px;
    margin-bottom:2px;
    padding:6px;
}

hr {
    margin-top:8px;
    margin-bottom:8px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------------------------
# SIDEBAR PANEL
# -------------------------------------------------

with st.sidebar:

    st.image("ola_logo.png", width=150)

    st.markdown('<div class="sidebar-title">Analytics Menu</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('<div class="section-title">SQL Analysis</div>', unsafe_allow_html=True)

    if st.button("📊 Run SQL Query"):
        st.session_state.page = "sql"

    st.markdown("---")

    st.markdown('<div class="section-title">Power BI Dashboards</div>', unsafe_allow_html=True)

    if st.button("📈 Overall Analytics"):
        st.session_state.page = "dash1"

    if st.button("🚖 Vehicle Insights"):
        st.session_state.page = "dash2"

    if st.button("💰 Revenue Insights"):
        st.session_state.page = "dash3"

    if st.button("❌ Cancellation Insights"):
        st.session_state.page = "dash4"

    if st.button("⭐ Customer Experience"):
        st.session_state.page = "dash5"


# -------------------------------------------------
# MAIN PANEL
# -------------------------------------------------

page = st.session_state.page


# SQL QUERY PAGE
if page == "sql":

    st.header("SQL Queries Used in Analysis")

    sql_queries = load_sql_queries()

    st.code(sql_queries, language="sql")


elif page == "dash1":

    st.header("Overall Analytics")

    st.image("dashboard1.png", use_container_width=True)


elif page == "dash2":

    st.header("Vehicle Insights")

    st.image("dashboard2.png", use_container_width=True)


elif page == "dash3":

    st.header("Revenue Insights")

    st.image("dashboard3.png", use_container_width=True)


elif page == "dash4":

    st.header("Cancellation Insights")

    st.image("dashboard4.png", use_container_width=True)


elif page == "dash5":

    st.header("Customer Experience")

    st.image("dashboard5.png", use_container_width=True)


else:

    st.title("📊 Ola Analytics Dashboard")

    st.info("Select a feature from the left panel to explore analytics.")