import streamlit as st
from web3 import Web3

st.set_page_config(page_title="GBTNetwork RPC Switcher", page_icon="🌐")

# Session to store list of RPCs
if "rpc_list" not in st.session_state:
    st.session_state.rpc_list = [
        "https://gbtnetwork-render.onrender.com"  # Default original RPC
    ]

st.title("🌐 GBTNetwork RPC Dashboard")
st.image("https://raw.githubusercontent.com/openai-user-assist/GBTNetworkAssets/main/logo.png", width=150)

st.markdown("### Available RPC URLs:")
for i, rpc in enumerate(st.session_state.rpc_list):
    st.write(f"{i+1}. {rpc}")

# Input new RPC URL
new_rpc = st.text_input("🔗 Enter a new RPC URL (optional):")

if st.button("➕ Add RPC URL"):
    if new_rpc.startswith("http"):
        if new_rpc not in st.session_state.rpc_list:
            st.session_state.rpc_list.append(new_rpc)
            st.success("✅ New RPC added!")
        else:
            st.warning("⚠️ RPC URL already exists.")
    else:
        st.error("❌ RPC URL must start with http:// or https://")

# Dropdown to select active RPC
selected_rpc = st.selectbox("🔄 Select active RPC URL:", st.session_state.rpc_list)

try:
    w3 = Web3(Web3.HTTPProvider(selected_rpc))
    if w3.isConnected():
        st.success("✅ Connected to blockchain!")
        st.markdown(f"- **Chain ID**: `{w3.eth.chain_id}`")
        st.markdown(f"- **Latest Block**: `{w3.eth.block_number}`")
    else:
        st.error("❌ Could not connect. Invalid or offline RPC.")
except Exception as e:
    st.error(f"❌ Error: {e}")
