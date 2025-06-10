# A/B Testing in Consumer Finance Analytics 🧪💳

This project demonstrates how to design and evaluate an A/B test for a credit card marketing offer using synthetic customer data. It includes dataset generation, exploratory segmentation, and statistical hypothesis testing to evaluate the effectiveness of targeted offers.

---

## 📌 Problem Statement

Financial institutions often run marketing campaigns to increase customer engagement or conversion. This project simulates a real-world use case of validating whether a new credit card offer (Treatment group) performs significantly better than a baseline offer (Control group), using data science techniques.

---

## 🧰 Tech Stack

- **Python**
- **Pandas & NumPy**
- **Matplotlib & Seaborn**
- **SciPy (for statistical testing)**
- **Jupyter Notebook**

---

## 📊 Project Structure

```text
📁 ab-testing-finance-analytics
├── _01_generate_dataset.ipynb       # Code to create synthetic customer data
├── 02_target_segmentation.ipynb     # Exploratory segmentation and A/B test logic
├── README.md                        # You are here
---

## 📈 Key Steps

### 1. Generate Synthetic Dataset
- Simulate realistic customer attributes (income, age, score, etc.)
- Randomly assign customers to Control and Treatment groups

### 2. Segment Target Audience
- Explore the data with descriptive statistics and visualizations
- Group customers by income, spending, or credit score

### 3. Perform A/B Testing
- Use statistical tests to compare the conversion rates
- Analyze p-values and confidence intervals for significance

---

## 📌 Results & Insights

- 🎯 Treatment group showed a statistically significant lift in conversion rate (p < 0.05)
- 💡 Middle-income customers were more responsive to marketing offers
- 📊 EDA helped identify key segments to target in future campaigns

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/Terraspace009/ab-testing-finance-analytics.git
cd ab-testing-finance-analytics

# Run the notebooks
jupyter notebook notebooks/_01_generate_dataset.ipynb
jupyter notebook notebooks/02_target_segmentation.ipynb

Aishwarya S


