import streamlit as st
# import numpy as np
# import pandas as pd
# #画像
# from PIL import Image

import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

#テーブル
# df=pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })
# st.table(df.style.highlight_max(axis=0))



#マークアップ
# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """



#折れ線グラフ・エリアチャート・棒グラフ
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df=pd.DataFrame(
#     #lat:経度,lon:緯度 乱数は0〜1の値を取り幅が大きくなってしまうため
#     #緯度・経度の乱数を50で割り、新宿付近の座標（35.69,139.70）を足すことで
#     #振れ幅は小さいがバラバラの座標情報を100個分生成する
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

#---------------------------------------------------------------------------------------------------------

# st.write('Display Image')

#画像
# img = Image.open('SampleImage.png')
# st.image(img,caption='testSS',use_column_width=True)


#チェックボックス
#if文でチェックボックスがついていたら画像を表示させる
# if st.checkbox('Show Image'):
#     img = Image.open('SampleImage.png')
#     st.image(img,caption='testSS',use_column_width=True)


#---------------------------------------------------------------------------------------------------------

st.write('Interrective Widgets')

#セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい',
#     list(range(1,11))
# )
# 'あなたの好きな数字は', option,'です。'



#テキスト入力
# text = st.text_input('あなたの趣味を教えて下さい')
# 'あなたの趣味：',text


#スライダー
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition


#---------------------------------------------------------------------------------------------------------
#レイアウト
#サイドバー
# st.sidebar.write('Interrective Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えて下さい')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション：',condition


#2カラムレイアウト
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の内容')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の内容')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の内容')

# text = st.text_input('あなたの趣味を教えて下さい')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション：',condition


#
st.write('プログレスバーの表示')
'start!!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'