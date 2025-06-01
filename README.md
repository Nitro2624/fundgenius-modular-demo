
# FundGenius (Modular Version)

FundGenius is an internal-use AI assistant for SBI Mutual Fund employees. It provides fund recommendations, manager insights, fund mixes, and basic real-time data.

## 🔧 Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/Nitro2624/fundgenius-demo.git
cd fundgenius-demo
```

2. Create folder structure:

```
fundgenius-demo/
├── app.py
├── requirements.txt
├── README.md
└── modules/
    ├── recommender.py
    ├── amfi_data.py
    └── manager_notes.py
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app locally:

```bash
streamlit run app.py
```

5. To deploy:
- Push this structure to GitHub under `Nitro2624/fundgenius-demo`
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Deploy from GitHub selecting `app.py`

---

✅ Internal Only — Not for public use.
