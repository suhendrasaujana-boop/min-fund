import streamlit as st
import pandas as pd
from db.supabase_client import supabase

st.set_page_config(layout="wide")
st.title("📊 IHSG Fund Manager Dashboard")

# Ambil data dari Supabase
response = supabase.table("stock_price").select("*").limit(100).execute()

if response.data:
    df = pd.DataFrame(response.data)
    st.write("Data terakhir:")
    st.dataframe(df.tail())
else:
    st.warning("Belum ada data stock_price di database")
