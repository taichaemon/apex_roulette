import collections.abc
import streamlit as st
import random as rd
import streamlit.components.v1 as stc

HIDE_ST_STYLE = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
				        .appview-container .main .block-container{
                            padding-top: 1rem;
                            padding-right: 3rem;
                            padding-left: 3rem;
                            padding-bottom: 1rem;
                        }  
                        .reportview-container {
                            padding-top: 0rem;
                            padding-right: 3rem;
                            padding-left: 3rem;
                            padding-bottom: 0rem;
                        }
                        header[data-testid="stHeader"] {
                            z-index: -1;
                        }
                        div[data-testid="stToolbar"] {
                        z-index: 100;
                        }
                        div[data-testid="stDecoration"] {
                        z-index: 100;
                        }
                </style>
"""

st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)
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
