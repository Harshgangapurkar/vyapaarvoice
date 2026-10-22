import datetime
import os
import pandas as pd

COLS = ["time", "type", "customer", "item", "qty", "amount", "heard"]
DATA_FILE = os.path.join(os.path.dirname(__file__), "khata.csv")
TYPE = {
    "hi": {"sale": "बिक्री", "udhaar": "उधार", "payment": "जमा"},
    "hl": {"sale": "Bikri", "udhaar": "Udhaar", "payment": "Jama"},
    "en": {"sale": "Sale", "udhaar": "Credit", "payment": "Payment"},
}
HEAD = {
    "hi": ["समय", "प्रकार", "ग्राहक", "सामान", "मात्रा", "रकम", "सुना"],
    "hl": ["Samay", "Prakar", "Customer", "Saaman", "Matra", "Rakam", "Suna"],
    "en": ["Time", "Type", "Customer", "Item", "Qty", "Amount", "Heard"],
}
SUMMARY = {
    "hi": ("आज की बिक्री {} रुपये", "आज का उधार {} रुपये", "{} का बाकी {} रुपये", "अभी कोई एंट्री नहीं है"),
    "hl": ("Aaj ki bikri {} rupaye", "Aaj ka udhaar {} rupaye", "{} ka baaki {} rupaye", "Abhi koi entry nahi hai"),
    "en": ("Today's sales {} rupees", "Today's credit {} rupees", "{} owes {} rupees", "No entries yet"),
}
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
def now_ist(): return datetime.datetime.now(IST)
def today_ist(): return now_ist().date()
def _ensure_file():
    if not os.path.exists(DATA_FILE):
        pd.DataFrame(columns=["id"] + COLS).to_csv(DATA_FILE, index=False)
def _all():
    _ensure_file()
    try: df = pd.read_csv(DATA_FILE).fillna("")
    except (pd.errors.EmptyDataError, pd.errors.ParserError): df = pd.DataFrame(columns=["id"] + COLS)
    for c in ["id"] + COLS:
        if c not in df.columns: df[c] = ""
    return df[["id"] + COLS]
def load(user=None):
    return _all()[COLS].copy().fillna("")
def add(e, user=None):
    df = _all()
    try: next_id = int(pd.to_numeric(df["id"], errors="coerce").max()) + 1 if not df.empty else 1
    except (ValueError, TypeError): next_id = len(df) + 1
    amount = e.get("amount")
    row = {"id": next_id, "time": now_ist().replace(tzinfo=None).isoformat(timespec="seconds"),
           "type": e.get("type", "sale"), "customer": e.get("customer") or "",
           "item": e.get("item") or "", "qty": "" if e.get("qty") is None else str(e.get("qty")),
           "amount": 0 if amount is None else float(amount), "heard": e.get("heard", "") or ""}
    pd.concat([df, pd.DataFrame([row])], ignore_index=True).to_csv(DATA_FILE, index=False)
def recent(user=None, n=20):
    df = _all().tail(n).iloc[::-1].copy()
    return df.to_dict(orient="records")
def delete(entry_id, user=None):
    df = _all()
    new_df = df[pd.to_numeric(df["id"], errors="coerce") != int(entry_id)]
    removed = len(new_df) != len(df)
    if removed: new_df.to_csv(DATA_FILE, index=False)
    return removed
def show(lang, user=None):
    df = load(user).tail(20).iloc[::-1].copy()
    df["type"] = df["type"].map(TYPE[lang]).fillna(df["type"])
    df.columns = HEAD[lang]
    return df
def confirm_text(e, lang="hi"):
    a, c, k = f"{float(e.get('amount') or 0):g}", e.get("customer") or "ग्राहक", e.get("type", "sale")
    if lang == "hi":
        return {"udhaar": f"{c}, {a} रुपये का उधार लिखा", "payment": f"{c} से {a} रुपये मिले", "sale": f"{a} रुपये की बिक्री लिखी"}.get(k, f"{a} रुपये की एंट्री सेव की")
    if lang == "hl":
        return {"udhaar": f"{c}, {a} rupaye ka udhaar likha", "payment": f"{c} se {a} rupaye mile", "sale": f"{a} rupaye ki bikri likhi"}.get(k, f"{a} rupaye ki entry save hui")
    return {"udhaar": f"{c}, {a} rupees credit recorded", "payment": f"Received {a} rupees from {c}", "sale": f"Sale of {a} rupees recorded"}.get(k, f"Transaction of {a} rupees recorded")
def summary_text(lang="hi", user=None):
    s_sale, s_udh, s_bal, s_empty = SUMMARY[lang]
    df = load(user)
    if df.empty: return s_empty
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)
    df["time"] = df["time"].astype(str)
    today = df[df["time"].str.startswith(today_ist().isoformat())]
    sale = today[today["type"] == "sale"]["amount"].sum()
    udh = today[today["type"] == "udhaar"]["amount"].sum()
    given = df[df["type"] == "udhaar"].groupby("customer")["amount"].sum()
    paid = df[df["type"] == "payment"].groupby("customer")["amount"].sum()
    bal = given.sub(paid, fill_value=0)
    bal = bal[(bal > 0) & (bal.index != "")].sort_values(ascending=False).head(3)
    parts = [s_sale.format(f"{sale:g}"), s_udh.format(f"{udh:g}")]
    parts += [s_bal.format(n, f"{v:g}") for n, v in bal.items()]
    return ". ".join(parts)
