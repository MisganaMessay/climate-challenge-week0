# 🌍 African Climate Trend Analysis (COP32 Support)

## 🎯 Business Objective
As a **Junior Data Analyst** at **EthioClimate Analytics**, this project was commissioned by the **Ethiopian Ministry of Planning and Development** to support Ethiopia’s strategic preparations for hosting the **United Nations Climate Change Conference (COP32)** in Addis Ababa in 2027.

The objective is to generate **evidence-based, negotiation-grade insights** from historical climate data (2015–2026) across five African countries: **Ethiopia, Kenya, Sudan, Nigeria, and Tanzania.**

---

## 🪜 The Three-Layer Framework (Ladder of Insight)
All analyses follow a structured framework aligned with international climate policy standards:

1. **What is changing?**  
   Trend analysis relative to baselines, including variability and uncertainty.

2. **What did it cause?**  
   Impact analysis (e.g., effects of temperature variability on humidity and agricultural conditions).

3. **What does it demand?**  
   Translation of findings into actionable **policy recommendations and financial requirements** for COP32 negotiations.

---

## 📊 Project Implementation Summary

- **Task 1: Engineering**  
  Established a professional development environment using Git, virtual environments, and automated **CI/CD pipelines via GitHub Actions**.

- **Task 2: Data Science**  
  Conducted comprehensive **data profiling and exploratory data analysis (EDA)** for all five countries.
  - Handled NASA sentinel values (`-999`)
  - Removed duplicates
  - Applied **Z-score-based outlier detection**

- **Task 3: Statistical Analysis**  
  Performed cross-country comparison using **one-way ANOVA** to assess climate variability differences.
  - **F-statistic: 18938.75**, indicating statistically significant variation between countries.

- **Task 4: Interactive Tool**  
  Developed a **Streamlit dashboard** to enable policymakers to explore data and insights interactively in real time.

---

## 📁 Folder Structure
```text
├── .github/          # CI/CD workflows (GitHub Actions)
├── .vscode/          # Editor configuration files
├── app/              # Streamlit dashboard application
├── data/             # Raw and cleaned datasets (ignored via .gitignore)
├── notebooks/        # EDA and statistical analysis notebooks
├── scripts/          # Utility and helper scripts
├── tests/            # Unit tests
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

---

## 🛠️ Setup & Reproducibility

### 1. Environment Setup (Windows)
```cmd
# Clone the repository
git clone https://github.com/MisganaMessay/climate-challenge-week0.git
cd climate-challenge-week0

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 2. Run the Dashboard
```cmd
streamlit run app/main.py
```

---

## 💻 Tech Stack
- **Programming Language:** Python 3.12.4
- **Data Analysis:** Pandas, NumPy, SciPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Web Application:** Streamlit
- **DevOps & Version Control:** Git, GitHub Actions (CI/CD)