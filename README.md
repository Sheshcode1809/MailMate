# 📧 MailMate – Think Less, Send Smart

> An AI-powered email responder that reads incoming emails, generates context-aware replies using GPT-4, and sends them directly — all from a simple web interface.

---

## 🚀 What is MailMate?

**MailMate** is a Streamlit web application that automates email responses using OpenAI's GPT-4 model. You paste an email you received, choose a tone, enter the recipient's address, and MailMate handles the rest — crafting a smart reply and delivering it via Gmail SMTP.

---

## 🔄 Project Flow

```
┌─────────────────────────────────────────────────────────┐
│                     USER (Browser)                      │
│                                                         │
│  1. Paste received email content                        │
│  2. Enter recipient email address                       │
│  3. Select response tone                                │
│  4. Click "Generate & Send Email"                       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   main.py  (Streamlit UI)               │
│                                                         │
│  - Renders the web interface                            │
│  - Captures user inputs (email text, tone, recipient)   │
│  - Calls email_agent and email_sender on button click   │
└────────────┬────────────────────────────┬───────────────┘
             │                            │
             ▼                            ▼
┌────────────────────────┐   ┌────────────────────────────┐
│  agents/email_agent.py │   │  utils/email_sender.py     │
│                        │   │                            │
│  - Builds a prompt     │   │  - Reads Gmail credentials │
│    with the email text │   │    from Streamlit secrets  │
│    and selected tone   │   │  - Connects via SMTP TLS   │
│  - Calls OpenAI GPT-4  │   │  - Sends generated reply   │
│  - Returns AI reply    │   │    to recipient's inbox    │
└────────────┬───────────┘   └────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────┐
│                   OpenAI GPT-4 API                      │
│                                                         │
│  - Receives the prompt (email + tone)                   │
│  - Generates a smart, context-aware reply               │
│  - Returns the reply text                               │
└─────────────────────────────────────────────────────────┘
```

---

## 🗂️ Project Structure

```
MailMate/
├── main.py                   # Streamlit UI – entry point
├── requirements.txt          # Python dependencies
├── .gitignore                # Excludes secrets from Git
│
├── agents/
│   └── email_agent.py        # GPT-4 prompt builder & caller
│
├── utils/
│   └── email_sender.py       # Gmail SMTP email dispatcher
│
└── .streamlit/
    └── secrets.toml          # 🔒 Local secrets (NOT pushed to GitHub)
```

---

## ⚙️ How Each Component Works

### `main.py` — The UI Layer
The heart of the app. Built with **Streamlit**, it renders:
- A text area to paste the incoming email
- A text input for the recipient's email address
- A dropdown to select the tone (`Professional`, `Friendly`, `Apologetic`, `Persuasive`)
- A button that triggers the full generate-and-send pipeline

### `agents/email_agent.py` — The AI Brain
This module is responsible for generating the email reply:
1. Receives the raw email text and the selected tone
2. Constructs a prompt: *"Write a reply to this email using a [tone] tone"*
3. Calls `OpenAI GPT-4` via the official Python client
4. Returns the generated reply as a string

### `utils/email_sender.py` — The Email Dispatcher
Handles the actual email delivery:
1. Reads credentials from `st.secrets` (not hardcoded)
2. Creates a MIME email with `From`, `To`, `Subject`, and body
3. Connects to Gmail's SMTP server on **port 587** using **STARTTLS**
4. Logs in and sends the message
5. Returns `True` on success, `False` on failure

---

## 🔐 Secrets & Configuration

Secrets are stored securely and are **never committed to GitHub**.

For **local development**, create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your-openai-api-key"
SENDER_EMAIL = "your-gmail@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

For **Streamlit Cloud deployment**, add the same values in the app's **Secrets** settings panel.

> ⚠️ Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your regular Gmail password. Requires 2FA enabled.

---

## 🛠️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Sheshcode1809/MailMate.git
cd MailMate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your secrets
Create `.streamlit/secrets.toml` with your credentials (see above).

### 4. Run the app
```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `openai >= 1.0.0` | GPT-4 API client |
| `smtplib` *(built-in)* | Email sending over SMTP |

---

## 🌐 Deploy on Streamlit Community Cloud

1. Push this repo to GitHub ✅
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub and select `Sheshcode1809/MailMate`
4. Set main file: `main.py`
5. Add your secrets in **Advanced Settings → Secrets**
6. Click **Deploy** 🚀

---

## 📝 License

This project is for personal/educational use. Feel free to fork and extend it!

---

*Built with ❤️ using Streamlit & OpenAI GPT-4*
