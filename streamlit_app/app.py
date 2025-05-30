import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# --- Load Data ---
df = pd.read_csv('customers.csv')

# --- Title ---
st.title("📊 A/B Testing and Hypothesis Validation in Consumer Finance Analytics")

st.markdown("This dashboard simulates a credit card marketing campaign using A/B testing. The treatment group received a personalized bonus offer, and the control group did not.")

# --- Metrics ---
signup_rates = df.groupby('received_bonus_offer')['signed_up'].value_counts(normalize=True).unstack()

col1, col2 = st.columns(2)
col1.metric("📈 Control Signup Rate", f"{signup_rates.loc['No', 'Yes']*100:.2f}%")
col2.metric("🎯 Treatment Signup Rate", f"{signup_rates.loc['Yes', 'Yes']*100:.2f}%")

# --- Chart ---
st.subheader("📉 Signup Rates by Offer Group")

fig, ax = plt.subplots()
signup_rates.plot(kind='bar', stacked=True, ax=ax)
plt.ylabel("Proportion")
plt.title("Signup Rate Distribution")
st.pyplot(fig)

# --- Chi-Square Test ---
st.subheader("🔍 Hypothesis Testing Result")
ab_table = pd.crosstab(df['received_bonus_offer'], df['signed_up'])
chi2, p, dof, expected = chi2_contingency(ab_table)

st.write("Contingency Table:")
st.dataframe(ab_table)

st.markdown(f"""
- **Chi-square value:** {chi2:.4f}  
- **P-value:** {p:.4f}  
- **Significance Level (α):** 0.05  
""")

if p < 0.05:
    st.success("✅ Result: Statistically significant difference — the bonus offer improved signup rate!")
else:
    st.error("❌ Result: No statistically significant difference — bonus offer had no clear effect.")

# --- Footer ---
st.markdown("---")
st.caption("Built by Aishwarya Shukla | Data Science Portfolio Project")
