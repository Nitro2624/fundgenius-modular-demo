
import pandas as pd

def get_latest_navs():
    data = {
        "Fund Name": ["SBI Bluechip Fund", "SBI Liquid Fund", "SBI Balanced Advantage Fund"],
        "NAV (₹)": [74.25, 31.18, 45.03],
        "1Y Return (%)": [18.4, 6.2, 9.7],
        "Type": ["Equity", "Debt", "Hybrid"]
    }
    return pd.DataFrame(data)
