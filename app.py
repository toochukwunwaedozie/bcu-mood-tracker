import streamlit as st
import datetime
import random

st.set_page_config(page_title="Zenith Transfer - by NWAEDOZIE", page_icon="🏦", layout="centered")

# --- STYLING LIKE ZENITH RED ---
st.markdown("""
<style>
    .zenith-header { background: #E30613; padding: 15px; border-radius: 10px; color: white; text-align: center; }
    .balance-card { background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #E30613; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="zenith-header"><h2>🏦 Zenith Bank - Transfer Demo</h2><p>by ADAOBI EZEH MUMMY | BCU Project</p></div>', unsafe_allow_html=True)

st.write("")

# --- SESSION STATE FOR BALANCE ---
if 'balance' not in st.session_state:
    st.session_state.balance = 250000.75
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# Balance display
st.markdown(f'<div class="balance-card"><h4>Account: 221****890 - Savings</h4><h1>₦ {st.session_state.balance:,.2f}</h1><p>Available Balance</p></div>', unsafe_allow_html=True)

st.write("---")
st.subheader("💸 Make a Transfer")

with st.form("transfer_form"):
    col1, col2 = st.columns(2)
    with col1:
        bank = st.selectbox("Select Bank", ["Zenith Bank", "GTB", "Access Bank", "First Bank", "UBA", "OPay", "Moniepoint", "Kuda"])
    with col2:
        account_type = st.selectbox("Transfer Type", ["Zenith to Zenith", "To Other Banks"])

    account_number = st.text_input("Recipient Account Number", max_chars=10, placeholder="0123456789")
    account_name = st.text_input("Recipient Name (Auto-verify demo)", placeholder="e.g. JOHN DOE")
    amount = st.number_input("Amount (₦)", min_value=100.0, max_value=5000000.0, step=100.0)
    narration = st.text_input("Narration", placeholder="e.g. For school fees")
    
    pin = st.text_input("Enter 4-digit PIN (demo: 1234)", type="password", max_chars=4)

    submit = st.form_submit_button("Transfer Now", use_container_width=True)

    if submit:
        if not account_number or len(account_number) != 10:
            st.error("❌ Please enter valid 10-digit account number")
        elif amount > st.session_state.balance:
            st.error("❌ Insufficient balance")
        elif pin != "1234":
            st.error("❌ Incorrect PIN. Use 1234 for demo")
        elif not account_name:
            st.error("❌ Please enter recipient name")
        else:
            # Simulate transfer
            ref = f"ZBN{random.randint(100000000, 999999999)}"
            st.session_state.balance -= amount
            st.session_state.transactions.insert(0, {
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "to": f"{account_name} - {account_number} ({bank})",
                "amount": amount,
                "ref": ref,
                "narration": narration
            })
            st.success(f"✅ Transfer Successful!")
            st.balloons()
            st.code(f"""
TRANSACTION RECEIPT

Ref: {ref}
To: {account_name}
Bank: {bank}
Amount: ₦{amount:,.2f}
Date: {datetime.datetime.now()}
Status: SUCCESS
            """)

st.write("---")
st.subheader("📜 Recent Transactions")
if not st.session_state.transactions:
    st.info("No transactions yet")
else:
    for t in st.session_state.transactions[:5]:
        with st.expander(f"{t['date']} - ₦{t['amount']:,.2f} to {t['to'][:20]}..."):
            st.write(f"**Ref:** {t['ref']}")
            st.write(f"**Narration:** {t['narration']}")
            st.write(f"**Status:** Successful")

st.caption("⚠️ DISCLAIMER: This is a DEMO app for BCU learning project. Not connected to real Zenith Bank. No real money moves.")
