import pandas as pd
import streamlit as st
from pathlib import Path
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "responses.csv"

@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame()

def append_response(row: dict):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
