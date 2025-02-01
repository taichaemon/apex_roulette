import collections.abc
import streamlit as st
import random as rd
import streamlit.components.v1 as stc

st.title('レジェンドルーレットアプリ')
st.caption('created by taichaemon')
st.subheader('APEX全レジェンド26人')
population_category = st.radio('【人数】', ('1', '2', '3', '4'), horizontal=True)

l = ['アッシュ', 
     'バリおぢ', 
     'バンガ', 
     'ヒューズ',
     'マギー',
     'オクタン',
     'オルター',
     'パス',
     'ニュート',
     'レイス',
     'レヴ',
     'カイリ',
     'クリちゃん',
     'シア',
     'ブラちゃん',
     'エコーちゃん',
     'カタリスト',
     'ガスおじ',
     'ランパート',
     'ワットソン',
     'コンジット',
     'ジブ',
     'ニューキャ',
     'ミラージュ',
     'ライフラ',
     'ローバ']
l2 = rd.sample(l, 4)
if population_category == '1':
    order =  l2[0]
elif population_category == '2':
    order = '1,' + l2[0] +' 2,' + l2[1]
elif population_category == '3':
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2]
else:
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2] + ' 4,' + l2[3]

html_content = f"""
<button onclick="navigator.clipboard.writeText('{order}')">
    コピー
</button>
"""

if st.button('ルーレット実行'):
    st.code(order, language=None, wrap_lines=True)
    stc.html(html_content, height=50)