"""
streamlitを試す、爆速でデータ可視化、分析アプリを作成できる。
**メモ
conda環境なのでconda installでインストールする
マークダウン言語の書式に対応、マークダウン：マークアップの簡単なやつ
#の数で構造を示し、バックコーテーションで囲いがつく
インタラクティブなウィジェットも作れるよー
"""
import streamlit as st
import numpy as np
import pandas as pd
#import time
from PIL import Image

st.title("Streamlit 入門")
st.write("display DataFrame")

#カラムに関する処理
left_columns, right_columns = st.beta_columns(2)
button1 = left_columns.button("右カラムに文字を表示")
button2 = left_columns.button("表示をリセット")

if button1:
    right_columns.write("ここは右カラムです")

if button2:
    pass

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [34.7338219,135.5014056],
    columns=['lat','lon']
    )

img = Image.open("IMG_7282.JPG")

#動的な表を表示させる場合はdataframeを利用
if st.checkbox("show dataframe"):
    st.dataframe(df,width = 400,height = 200)
#折れ線グラフ
#st.line_chart(df)
#エリアチャート
#st.area_chart(df)
#棒グラフ
#st.bar_chart(df)
#マップ表示
if st.checkbox("show maps"):
    """
    ## 新大阪付近
    ### ランダムに緯度経度をプロット
    """
    st.map(df)

if st.checkbox("show image"):
    st.write("Display images, good views")
    st.image(img, caption='good view',use_column_width=True)


st.sidebar.write('interactive widgets')

text = st.sidebar.text_input(
    "趣味は？"
)

option = st.sidebar.selectbox(
    "好きな数字を教えてください",
    list(range(1,10))
)

"あなたの好きな数字は",option,"ですよん"
"あなたの趣味は",text,"ですよん"

#expander
expander = st.beta_expander("問い合わせ先")
expander.write("please mail me xxx")
