import streamlit as st
import re

st.set_page_config(
    page_title="Scam Shield AI",
    page_icon="🛡️",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }

    .hero {
        text-align: center;
        padding: 25px 10px 15px 10px;
    }

    .hero-icon {
        font-size: 55px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 20px;
    }

    .info-card {
        padding: 18px;
        border-radius: 15px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .result-card {
        padding: 22px;
        border-radius: 18px;
        margin-top: 15px;
        margin-bottom: 15px;
        border: 1px solid rgba(128,128,128,0.25);
    }

    .risk-number {
        font-size: 36px;
        font-weight: 800;
        text-align: center;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        margin-top: 25px;
    }

    .footer {
        text-align: center;
        color: #888;
        padding: 25px 0 10px 0;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="hero-icon">🛡️</div>
    <div class="hero-title">Scam Shield AI</div>
    <div class="hero-subtitle">
        Your smart assistant for identifying suspicious messages and links.
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()


# ---------- INFO ----------
st.markdown("""
<div class="info-card">
    🔐 <b>Stay Safe Online</b><br>
    Paste a suspicious SMS, email, message, or website link below.
    Scam Shield AI will look for common warning signs.
</div>
""", unsafe_allow_html=True)


# ---------- INPUT ----------
st.markdown(
    '<div class="section-title">🔍 Check a suspicious message or link</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Paste your content below:",
    height=180,
    placeholder="Example: Congratulations! You won ₹50,000. Click this link to claim your prize..."
)

check_button = st.button(
    "🚨 Check for Scam",
    use_container_width=True
)


# ---------- SCAM CHECK ----------
if check_button:

    if not text.strip():
        st.warning("⚠️ Please enter a message or link first.")

    else:
        text_lower = text.lower()

        warning_words = [
            "urgent",
            "verify your account",
            "click here",
            "claim your prize",
            "you won",
            "winner",
            "otp",
            "password",
            "bank account",
            "send money",
            "pay now",
            "limited time",
            "congratulations",
            "kyc",
            "refund",
            "lottery",
            "gift card"
        ]

        found_words = [
            word for word in warning_words
            if word in text_lower
        ]

        suspicious_link = bool(
            re.search(r"https?://|www\.|bit\.ly|tinyurl", text_lower)
        )

        risk_score = 0

        if found_words:
            risk_score += min(len(found_words) * 10, 60)

        if suspicious_link:
            risk_score += 25

        if "otp" in text_lower or "password" in text_lower:
            risk_score += 15

        risk_score = min(risk_score, 100)

        st.divider()

        st.markdown(
            '<div class="section-title">📊 Scam Risk Result</div>',
            unsafe_allow_html=True
        )

        # ---------- HIGH RISK ----------
        if risk_score >= 60:

            st.error(f"🚨 HIGH RISK — {risk_score}%")

            st.progress(risk_score / 100)

            st.markdown("""
            <div class="result-card">
                <b>⚠️ Be extremely careful.</b><br><br>
                This message contains several common scam warning signs.
                Do not share passwords, OTPs, banking information, or send money.
            </div>
            """, unsafe_allow_html=True)

        # ---------- MEDIUM RISK ----------
        elif risk_score >= 30:

            st.warning(f"⚠️ MEDIUM RISK — {risk_score}%")

            st.progress(risk_score / 100)

            st.markdown("""
            <div class="result-card">
                <b>🔎 Something looks suspicious.</b><br><br>
                Verify the sender through an official website or trusted contact
                before clicking links or providing information.
            </div>
            """, unsafe_allow_html=True)

        # ---------- LOW RISK ----------
        else:

            st.success(f"✅ LOW RISK — {risk_score}%")

            st.progress(risk_score / 100)

            st.markdown("""
            <div class="result-card">
                <b>👍 No major warning signs detected.</b><br><br>
                This doesn't guarantee that the message is safe.
                Always be careful with unexpected messages and links.
            </div>
            """, unsafe_allow_html=True)


        # ---------- WARNING SIGNS ----------
        if found_words:

            st.markdown("### 🚩 Warning Signs Detected")

            for word in found_words:
                st.write(f"• **{word}**")

        if suspicious_link:

            st.markdown("### 🔗 Suspicious Link Detected")

            st.write(
                "The message appears to contain a website link or shortened URL. "
                "Check the destination carefully before opening it."
            )


# ---------- HOW IT WORKS ----------
st.divider()

st.markdown(
    '<div class="section-title">💡 How Scam Shield AI Works</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 1️⃣ Paste")
    st.write("Paste a suspicious message, email, or link.")

with col2:
    st.markdown("### 2️⃣ Analyze")
    st.write("The app checks for common scam warning signs.")

with col3:
    st.markdown("### 3️⃣ Protect")
    st.write("Review the risk level and stay cautious.")


# ---------- SAFETY TIPS ----------
st.divider()

st.markdown(
    '<div class="section-title">🛡️ Quick Safety Tips</div>',
    unsafe_allow_html=True
)

st.write("• Never share your OTP or password with anyone.")
st.write("• Be cautious with urgent payment requests.")
st.write("• Verify unexpected messages using official sources.")
st.write("• Think before clicking unfamiliar links.")


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    🛡️ Scam Shield AI<br>
    Stay alert. Think before you click.
</div>
""", unsafe_allow_html=True)
