
def recommend_funds(risk, duration):
    funds_data = {
        "Debt & Liquid Funds": [
            "SBI Liquid Fund",
            "SBI Magnum Ultra Short Duration Fund",
            "SBI Magnum Low Duration Fund"
        ],
        "Hybrid Funds": [
            "SBI Equity Hybrid Fund",
            "SBI Balanced Advantage Fund",
            "SBI Conservative Hybrid Fund"
        ],
        "Equity Funds": [
            "SBI Bluechip Fund",
            "SBI Small Cap Fund",
            "SBI Focused Equity Fund"
        ]
    }

    if risk == "Low" and duration <= 1:
        cat = "Debt & Liquid Funds"
    elif risk == "Moderate" and duration <= 3:
        cat = "Hybrid Funds"
    elif risk == "High" and duration > 3:
        cat = "Equity Funds"
    else:
        cat = "Hybrid Funds" if duration <= 3 else "Equity Funds"

    return cat, funds_data[cat]

def get_fund_mix(fund_list, total_amount):
    ratio = [0.4, 0.3, 0.3] if len(fund_list) >= 3 else [1/len(fund_list)] * len(fund_list)
    mix = []
    for i, fund in enumerate(fund_list[:3]):
        amt = round(total_amount * ratio[i])
        mix.append({"fund": fund, "amount": amt})
    return mix
