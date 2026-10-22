# VyapaarVoice — Voice-First Digital Ledger

[![Live Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vyapaarvoice.streamlit.app)

**VyapaarVoice** is a multilingual, voice-first digital ledger designed to simplify bookkeeping for small businesses in India. It enables shopkeepers to record sales, purchases, credit transactions, and payments using natural speech in Hindi, Marathi, or English, with spoken feedback to make everyday accounting more accessible.

🔗 **Live Demo:** https://vyapaarvoice.streamlit.app

## 🚀 Key Features

- **Multilingual Voice Input:** Record transactions using speech in Hindi, Marathi, and English.
- **Speech-to-Text:** Converts spoken commands into text using Gnani.ai speech recognition.
- **Natural-Language Transaction Parsing:** Extracts transaction details such as product, amount, quantity, customer or supplier, and due date.
- **Transaction Management:** Supports sales, purchases, credit sales, customer payments, and supplier payments.
- **Spoken Feedback:** Provides audio confirmations and asks users to repeat unclear commands.
- **Transaction Review:** Lets users verify extracted details before saving them.
- **Digital Ledger:** Maintains transaction records for reviewing and tracking business activity.
- **Due-Date Tracking:** Helps identify upcoming and overdue payments.
- **Simple Web Interface:** Built with Streamlit for an accessible, browser-based experience.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and transaction processing |
| Streamlit | Interactive web application |
| Gnani.ai Speech APIs | Speech-to-text and text-to-speech |
| Pandas | Transaction data processing |
| CSV | Local transaction storage |

## 💡 Example Usage

Speak naturally to record a transaction.

**Example 1 — Sale**

> "Sold five kg sugar for five hundred rupees."

Expected transaction details:
- Type: Sale
- Item: Sugar
- Quantity: 5 kg
- Amount: ₹500

**Example 2 — Purchase**

> "Bought two litres oil for three hundred and sixty rupees."

Expected transaction details:
- Type: Purchase
- Item: Oil
- Quantity: 2 litres
- Amount: ₹360

**Example 3 — Credit Sale**

> "Amit bought rice for eight hundred rupees and will pay in ten days."

Expected transaction details:
- Type: Credit sale
- Customer: Amit
- Item: Rice
- Amount: ₹800
- Due date: 10 days later

The extracted details should be reviewed before saving. Exact recognition depends on the speech transcript and the transaction parser.

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Harshgangapurkar/vyapaarvoice.git
cd vyapaarvoice
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gnani.ai API key

Create a `.env` file in the project root if your local configuration uses environment variables:

```env
GNANI_API_KEY=your_gnani_api_key
```

Replace the placeholder with your own API key. Check the application's configuration if your version uses a different variable name.

For Streamlit Community Cloud, configure the key under **App settings → Secrets**, using the secret format expected by your application.

**Never commit API keys, `.env` files, or other secrets to GitHub.**

### 5. Start the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 🔐 Privacy and Data Storage

VyapaarVoice is currently a prototype intended to demonstrate voice-driven bookkeeping.

- The current no-login version uses local CSV storage.
- A publicly accessible demo should only be used with sample or non-sensitive transaction data.
- Local files on hosted environments may not persist across restarts or redeployments.
- The application should not be treated as a production accounting system without stronger data protection, persistent storage, access controls, and transaction validation.

## 🔮 Future Improvements

- AI-powered multilingual transaction extraction.
- Better handling of regional accents and mixed-language speech.
- Conversational clarification for ambiguous transactions.
- Persistent cloud database integration.
- Customer balances, supplier balances, and outstanding-payment reports.
- Automated payment reminders and daily voice summaries.
- Improved transaction validation and audit history.

## 🎯 Project Goal

The goal of VyapaarVoice is to make digital bookkeeping simpler and more accessible for small Indian businesses by allowing shopkeepers to manage routine transactions in the languages they already speak.

## 👨‍💻 Author

**Harsh Gangapurkar**

- GitHub: [@Harshgangapurkar](https://github.com/Harshgangapurkar)
- Live Project: [VyapaarVoice](https://vyapaarvoice.streamlit.app)

---

*Built with Python, Streamlit, and Gnani.ai speech technology.*
