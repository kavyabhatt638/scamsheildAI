import streamlit as st
import re

st.set_page_config(
    page_title="Scam Shield AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Scam Shield AI")
st.write("Your simple AI-powered scam awareness assistant")
st.divider()

st.subheader("🔍 Check a suspicious message or link")

text = st.text_area(
    "Paste the message, SMS, email, or website link here:",
    height=180,
    placeholder="Example: Congratulations! You won ₹50,000. Click this link to claim your prize..."
)

if st.button("Check for Scam 🚨"):

    if not text.strip():
        st.warning("Please enter a message or link first.")
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
        st.subheader("📊 Scam Risk Result")

        if risk_score >= 60:
            st.error(f"🚨 HIGH RISK — {risk_score}%")
            st.write(
                "This message contains several common scam warning signs. "
                "Do not share passwords, OTPs, banking details, or send money."
            )

        elif risk_score >= 30:
            st.warning(f"⚠️ MEDIUM RISK — {risk_score}%")
            st.write(
                "This message has some suspicious characteristics. "
                "Verify the sender through an official source before taking action."
            )

        else:
            st.success(f"✅ LOW RISK — {risk_score}%")
            st.write(
                "No major scam indicators were detected. "
                "However, always verify unexpected messages independently."
            )

        if found_words:
            st.write("**Warning signs detected:**")
            for word in found_words:
                st.write(f"• {word}")

st.divider()

st.caption("Scam Shield AI • Stay alert. Think before you click.")