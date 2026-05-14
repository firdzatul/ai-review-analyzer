# 🍽️ AI Review Analyzer — RM Salero Minang

Automated customer review analysis system using 
Claude AI with 3-step Prompt Chaining technique.

## 📋 About
Transforms 50 raw Google Maps reviews into a 
professional executive report — automatically 
in minutes.

## ⚙️ How It Works
Excel Input (50 reviews)
↓
Chain 1 → Sentiment classification + review type
↓
Chain 2 → Aggregation & analysis per category
↓
Chain 3 → Executive report for management

## 🛠️ Tech Stack
- Python 3.14
- Anthropic Claude API (claude-sonnet-4-6)
- Pandas (Excel reader)
- Techniques: Prompt Chaining, JSON Output Formatting

## 📁 Project Structure
Analisis-RM-Salero-Minang/
├── AnalisReview.py               ← main program
├── config.py                     ← API key (not uploaded)
├── data_review_salero_minang.xlsx← input data
├── README.md                     ← this file
└── output/
├── hasil_chain1.json         ← classification results
├── hasil_chain2.json         ← aggregated data
└── hasil_laporan_direksi.txt ← final executive report

## 🚀 Getting Started
1. Clone this repository
2. Install dependencies:

pip install anthropic pandas openpyxl
3. Create config.py with your API key:
```python
   API_KEY = "sk-ant-xxxx..."
```
4. Run the program:
python3 AnalisReview.py

## 📊 Sample Output
- 50 reviews automatically classified
- Summary: 26 Positive | 22 Negative | 2 Neutral
- Executive report ready for presentation

## 💡 Use Cases
Can be used for any business with customer reviews:
- Restaurants & cafes
- Hotels
- E-commerce
- Startups

## 👨‍💻 Built With
Claude AI + Python