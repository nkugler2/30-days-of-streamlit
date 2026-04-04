import streamlit as st

st.header("30-days-of-streamlit")
st.caption("Can Noah write code without AI (kind of)")

st.header("st.button")

if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
