import pandas as pd
import streamlit as st

df = pd.read_excel('posts1.xlsx')

tabata_df = df[df['Profile'] == 'Tabata Amaral']

st.set_page_config(page_title="Análise do Instagram de Tabata Amaral", page_icon="📐", layout="wide")

st.title('Análise do Instagram de Tabata Amaral')

df2 = tabata_df.sort_values(by='Post interaction rate', ascending=False).head(10)

st.header("Nuvem de palavras das legendas escritas pela pré-candidata em suas publicações:")

url_imagem = 'fototabata.png'
st.image(url_imagem)

st.header("As 10 publicações com maior taxa de engajamento:")
st.markdown("Na análise eu foquei apenas nas três primeiras publicações:")
st.markdown("1° https://www.instagram.com/reel/C1UQXF1OSRc/")
st.markdown("2° https://www.instagram.com/reel/C16_3gcuNm4/")
st.markdown("3° https://www.instagram.com/reel/C0T7jIgOuB_/")

st.dataframe(df2)
