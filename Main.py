import streamlit as st
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client()

st.set_page_config(page_title="AIO Crypto scanner", page_icon="💰", layout="wide", initial_sidebar_state="expanded")
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
st.sidebar.success("Select a scanner from above.")







footer="""
<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
Made with 
<a href="https://www.buymeacoffee.com/iamashwin99"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a glue?&emoji=💔&slug=iamashwin99&font_family=Comic&outline_colour=000000&coffee_colour=ffffff" /></a>
</div>


<style>
/*#MainMenu {visibility: hidden;}*/
footer {visibility: hidden;}
/*header {visibility: hidden;}*/
</style>
            
"""
st.markdown(footer,unsafe_allow_html=True)

