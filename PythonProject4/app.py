import streamlit as st
st.title('my first project')
st.code("""
for i in range(1,10):
    print('hi')  
    """)
st.subheader('description of my app')
st.info('this is info about my app')
yt_url = 'https://youtu.be/D0D4Pa22iG0?si=PnYTSw_41rDoTHct'
st.video(yt_url)
st.balloons()

