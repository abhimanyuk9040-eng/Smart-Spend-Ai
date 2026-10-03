import streamlit as st
from google import genai
from PIL import Image
import re
import time

from action_tool import send_email


# -----------------------------
# Page settings
# -----------------------------
st.set_page_config(
    page_title="SmartSpend AI",
    page_icon="💰"
)


# -----------------------------
# Gemini setup
# -----------------------------
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# -----------------------------
# App title
# -----------------------------
st.title("SmartSpend AI 💰")
st.write("Understand where your money goes.")


# -----------------------------
# Upload receipt
# -----------------------------
uploaded_file = st.file_uploader(
    "📸 Upload your receipt or bill",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Receipt",
        use_container_width=True
    )

    if st.button("🔍 Analyze Receipt"):

        with st.spinner("Analyzing your receipt..."):

            prompt = """
            Analyze this receipt carefully.

            Extract:

            1. Item name
            2. Quantity
            3. Price
            4. Subtotal
            5. Tax
            6. Discount
            7. Final total
            8. Payment method
            9. Expense category

            At the end, write:

            FINAL_TOTAL: followed by the final bill amount.

            Example:
            FINAL_TOTAL: ₹609

            Do not guess missing information.
            Keep the answer simple and easy to understand.
            """

            response = None

            for attempt in range(4):

                try:

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=[prompt, image]
                    )

                    break

                except Exception as e:

                    if "503" in str(e) and attempt < 3:

                        wait_time = 5 * (2 ** attempt)

                        st.warning(
                            f"Gemini is busy. Retrying in {wait_time} seconds..."
                        )

                        time.sleep(wait_time)

                    else:

                        st.error(
                            "Gemini is currently unavailable. Please try again later."
                        )

                        st.stop()

            analysis = response.text

            st.session_state["receipt_analysis"] = analysis

            # Extract total
            match = re.search(
                r"FINAL_TOTAL:\s*₹?\s*([0-9]+(?:\.[0-9]+)?)",
                analysis,
                re.IGNORECASE
            )

            if match:

                st.session_state["total"] = float(
                    match.group(1)
                )


# -----------------------------
# Expense Analysis
# -----------------------------
if "receipt_analysis" in st.session_state:

    st.subheader("📊 Expense Analysis")

    st.write(
        st.session_state["receipt_analysis"]
    )


# -----------------------------
# Bill Splitter
# -----------------------------
if "total" in st.session_state:

    st.subheader("👥 Split Your Bill")

    total = st.session_state["total"]

    st.write(
        f"💰 **Total Bill: ₹{total:.2f}**"
    )

    people = st.number_input(
        "How many people are sharing this bill?",
        min_value=1,
        step=1
    )

    if st.button("💸 Split Bill"):

        per_person = total / people

        st.session_state["per_person"] = per_person

        st.success(
            f"Each person should pay **₹{per_person:.2f}**"
        )


# -----------------------------
# Email Summary
# -----------------------------
if "receipt_analysis" in st.session_state:

    st.subheader("📧 Send Expense Summary")

    email = st.text_input(
        "Enter email address"
    )

    if st.button("📨 Send Summary"):

        if email == "":

            st.warning(
                "Please enter an email address."
            )

        else:

            total = st.session_state.get(
                "total",
                0
            )

            summary = f"""
SmartSpend AI - Expense Summary

{st.session_state["receipt_analysis"]}

Total Bill: ₹{total:.2f}
"""

            if "per_person" in st.session_state:

                summary += f"""
Amount per person: ₹{st.session_state["per_person"]:.2f}
"""

            success = send_email(
                email,
                "SmartSpend AI - Expense Summary",
                summary
            )

            if success:

                st.success(
                    "✅ Expense summary sent successfully!"
                )