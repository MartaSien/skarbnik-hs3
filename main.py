import streamlit as st
import pandas as pd

PATRONITE_SAMPLE = "data/sample/raw/raport-wplat-patronow-rok-2026.csv"

st.dataframe(pd.read_csv(PATRONITE_SAMPLE, sep=";"))
