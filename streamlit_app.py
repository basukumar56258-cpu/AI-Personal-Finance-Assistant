import streamlit as st
from backend.app.services.finance_analyzer import analyze_transactions
from backend.app.ai.insights import generate_insights
st.set_page_config(page_title="AI Personal Finance Assistant",page_icon="💰",layout="wide")
st.title("💰 AI Personal Finance Assistant")
st.caption("AI-ready personal finance dashboard for spending, budgets and savings insights.")
rows=[
{"date":"2026-09-01","description":"Salary","category":"Income","amount":50000,"type":"income"},
{"date":"2026-09-02","description":"Rent","category":"Housing","amount":15000,"type":"expense"},
{"date":"2026-09-04","description":"Groceries","category":"Food","amount":5000,"type":"expense"},
{"date":"2026-09-07","description":"Internet","category":"Bills","amount":1200,"type":"expense"},
{"date":"2026-09-10","description":"Shopping","category":"Shopping","amount":4000,"type":"expense"}]
a=analyze_transactions(rows)
x,y,z=st.columns(3)
x.metric("Income",f"₹{a['total_income']:,.0f}")
y.metric("Expenses",f"₹{a['total_expenses']:,.0f}")
z.metric("Net Balance",f"₹{a['net_balance']:,.0f}")
st.subheader("📊 Spending by Category"); st.bar_chart(a["category_spending"])
st.subheader("🤖 AI Insights")
for i in generate_insights(a): st.write("•",i)
q=st.text_input("Ask your finance assistant","Where am I spending the most?")
if q: st.info(f"Highest recorded spending category: {a['top_spending_category']}")
