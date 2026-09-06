import streamlit as st
import re

st.set_page_config(
    page_title="Scam Shield AI",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef4ff 0%, #f8f0ff 50%, #ffffff 100%);
}

.hero {
    background: linear-gradient(135deg, #3155d9, #7b3ff2);
    padding: 35px 25px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(70, 60, 180, 0.25);
}

.hero-icon {
    font-size: 65px;
}

.hero-title {
    font-size: 43px;
    font-weight: 800;
    margin-top: 5px;
}

.hero-subtitle {
    font-size: 17px;
    opacity: 0.92;
}

.info-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border-left: 6px solid #5b4bea;
    box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    margin-bottom: 25px;
}

.section-title {
    font-size: 26px;
    font-weight: 750;
    margin-top: 20px;
}

.result-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.08);
    margin-top: 15px;
}

.tip-card {
    background: linear-gradient(135deg, #fff7df, #fff1c2);
    padding: 20px;
    border-radius: 18px;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #777;
    padding: 30px 0 10px;
    font-size: 14px;
}

div.stButton > button {
    width: 100%;
    border-radius: 14px;
    height: 52px;
    background: linear-gradient(135deg, #3155d9, #7b3ff2);
    color: white;
    font-size: 17px;
    font-weight: 700;
    border: none;
    box-shadow: 0 6px 15px rgba(80,70,190,0.25);
}

div.stButton > button:hover {
    transform: scale(1.01);
}

</style>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
    <div class="hero-icon">🛡️</div>
    <div class="hero-title">Scam Shield AI</div>
    <div class="hero-subtitle">
        Detect suspicious messages. Stay safe online.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- INTRO ----------------

st.markdown("""
<div class="info-card">
    🔐 <b>Protect yourself from online scams</b><br><br>
    Paste a suspicious SMS, email, message, or website link below.
    Scam Shield AI checks it for common scam warning signs.
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT ----------------

st.markdown(
    '<div class="section-title">🔍 Check a suspicious message or link</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Paste your message here:",
    height=180,
    placeholder="Example: Congratulations! You won ₹50,000. Click this link to claim your prize..."
)

check_button = st.button("🚨 Check for Scam")


# ---------------- SCAM ANALYSIS ----------------

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


        # -------- HIGH RISK --------

        if risk_score >= 60:

            st.error(f"🚨 HIGH RISK — {risk_score}%")

            st.progress(risk_score)

            st.markdown("""
            <div class="result-card">
                <h3>🚨 Be extremely careful</h3>
                This message contains several common scam warning signs.<br><br>
                ❌ Do not share passwords or OTPs.<br>
                ❌ Do not send money.<br>
                ❌ Avoid clicking suspicious links.
            </div>
            """, unsafe_allow_html=True)


        # -------- MEDIUM RISK --------

        elif risk_score >= 30:

            st.warning(f"⚠️ MEDIUM RISK — {risk_score}%")

            st.progress(risk_score)

            st.markdown("""
            <div class="result-card">
                <h3>⚠️ Something looks suspicious</h3>
                This message contains some warning signs.<br><br>
                🔎 Verify the sender through an official source
                before taking any action.
            </div>
            """, unsafe_allow_html=True)


        # -------- LOW RISK --------

        else:

            st.success(f"✅ LOW RISK — {risk_score}%")

            st.progress(risk_score)

            st.markdown("""
            <div class="result-card">
                <h3>✅ No major warning signs detected</h3>
                The message does not contain many common scam indicators.<br><br>
                Remember: a low score does not guarantee that a message is safe.
            </div>
            """, unsafe_allow_html=True)


        # ---------------- WARNING SIGNS ----------------

        if found_words:

            st.markdown("### 🚩 Warning Signs Detected")

            for word in found_words:
                st.write(f"🔸 **{word}**")


        if suspicious_link:

            st.markdown("### 🔗 Suspicious Link Detected")

            st.write(
                "A website or shortened link was detected. "
                "Be careful before opening it."
            )


# ---------------- HOW IT WORKS ----------------

st.divider()

st.markdown(
    '<div class="section-title">💡 How Scam Shield AI Works</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📋 1. Paste")
    st.write("Paste a suspicious message or link.")

with col2:
    st.markdown("### 🔎 2. Analyze")
    st.write("The system checks for scam warning signs.")

with col3:
    st.markdown("### 🛡️ 3. Protect")
    st.write("Use the result to make safer decisions.")


# ---------------- SAFETY TIPS ----------------

st.divider()

st.markdown(
    '<div class="section-title">🛡️ Stay Safe Online</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="tip-card">

<b>💡 Remember:</b><br><br>

🔐 Never share your OTP or password.<br>
💳 Be careful with unexpected payment requests.<br>
🔗 Think before clicking unknown links.<br>
📞 Verify suspicious messages using official sources.

</div>
""", unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    🛡️ <b>Scam Shield AI</b><br>
    Stay alert • Think before you click
</div>
""", unsafe_allow_html=True)
