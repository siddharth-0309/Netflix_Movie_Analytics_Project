# Netflix_Movie_Analytics_Project
End-to-End Data Wrangling, Cleaning, and Exploratory Data Analysis (EDA) on 9,800+ TMDB movies using Python to drive strategic business insights for OTT content acquisition and localization.
# 🎬 Movie Content Strategy & International Localization Analytics (TMDB)

## 📌 Project Overview
This project focuses on executing an End-to-End Exploratory Data Analysis (EDA) and Data Wrangling workflow on a dataset containing 9,800+ movies from TMDB. The primary goal is to derive actionable business insights to help OTT platforms and production houses maximize their return on investment (ROI), fine-tune content acquisition, and optimize localization strategies.

---

## 🛠️ Data Wrangling & Cleaning (Technical Highlights)
Before running any analysis, the dataset underwent a strict data-cleaning pipeline:
* **Data Type Casting:** Transformed malformed string data (`object`) in critical columns like `Vote_Count`, `Vote_Average`, and `Release_Date` into clean numerical and datetime types.
* **Missing Value Management:** Handled missing rows (~0.1% null records) effectively via safe dropping mechanisms to maintain distribution consistency.
* **De-duplication:** Identified and eliminated duplicate entries using unique constraints on `Title` and `Release_Year`.
* **Advanced Explode Operations:** Handled multi-genre entries (comma-separated strings) by converting them to lists and exploding them to isolate individual performance metrics.

---

## 🚀 Business Problem Statements & Analytical Insights

### 📌 Problem 1: Content Strategy Selection (Genre vs. Success Metrics)
* **The Business Dilemma:** Where should we allocate our production budget to balance massive public engagement (commercial pull) with high audience appreciation (critical acclaim)?
* **Data-Driven Solution & My Suggestion:** * **The High-Yield Bets:** Data reveals that **Animation, Adventure, and Sci-Fi** dominate public popularity. If the primary goal is high user acquisition and trending visibility, these genres are non-negotiable.
  * **The Retention Drivers:** Genres like **History, War, and Documentary** score the highest in critical ratings despite lower release volumes. Use these niche genres as "User Retention Tools."

### 📌 Problem 2: International Market Expansion (Language Localization)
* **The Business Dilemma:** Beyond English content, which regional language markets show the highest and most consistent viewer satisfaction to justify high dubbing and licensing budgets?
* **Data-Driven Solution & My Suggestion:** * **The Power of Asian Content:** While English content dominates volume in this filtered subset, **Japanese (`ja`) and Korean (`ko`)** movies show exceptionally high and stable average critical ratings.
  * **My Suggestion:** Instead of blindly spending localization budgets on all European languages, the platform should aggressively secure streaming rights for top-tier Japanese Anime and Korean Thrillers/Dramas.

### 📌 Problem 3: Audience Engagement & Quality Paradox
* **The Business Dilemma:** Should our recommendation engine solely promote ultra-popular blockbusters with massive view/vote counts, or do smaller, niche films offer better quality?
* **Data-Driven Solution & My Suggestion:** * **The Paradox Uncovered:** Data shows that a massive surge in votes does not automatically mean a superior rating. In fact, the "High Reach" tier often exhibits equivalent or better structural ratings than over-hyped blockbusters.
  * **My Suggestion:** Optimize the Recommendation Engine. The algorithm should actively surface highly-rated hidden gems from the "High Reach" and "Niche" buckets based on user affinity to prevent content fatigue.

---

## 💻 Tech Stack Used
* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
* **Environment:** Google Colab
