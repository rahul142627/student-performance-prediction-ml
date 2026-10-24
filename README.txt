# 🎓 Student Performance Prediction System using Machine Learning

> Predict early. Intervene sooner. Improve outcomes.

An end-to-end data science project that analyzes student academic records
(study hours, attendance, previous marks, assignments, internal marks) to
**predict Pass/Fail results, estimate grades, and identify at-risk students**
before final exams, so teachers can take corrective action in time.

## ✨ Highlights
- 📈 Compared **5 ML models**: Logistic Regression, Decision Tree, Naive Bayes, SVM, Random Forest
- 🏆 Best model: **Naive Bayes with 94.5% accuracy and 0.971 F1-score**
- 🚨 Automatically generates an **at-risk student list** (CSV)
- 🔮 Includes a **prediction function** for any new student
- 📊 Full EDA, confusion matrices, model comparison and feature importance charts

## 🛠️ Tech Stack
Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn · Jupyter Notebook

## 🚀 How to Run
1. `pip install -r requirements.txt`
2. `jupyter notebook`
3. Open `notebooks/student_performance.ipynb` → **Restart & Run All**

## 📂 Project Structure
├── dataset/        # student_performance.csv
├── notebooks/      # main notebook + outputs (at-risk list, saved model)
├── generate_dataset.py
└── requirements.txt

## 🔭 Future Enhancements
Mobile app · Real-time tracking · AI-based personalized recommendations · LMS integration
