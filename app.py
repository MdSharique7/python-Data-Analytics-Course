import streamlit as st
st.image('https://play-lh.googleusercontent.com/ZyWNGIfzUyoajtFcD7NhMksHEZh37f-MkHVGr5Yfefa-IX7yj9SMfI82Z7a2wpdKCA=w240-h480')
st.title("String App")
message = st.text_area("enter some text")
button = st.button("Process txt")

if button:
    st.write(message)
if st.sidebar.checkbox("Show Words"):
    words = message.split()
    st.write(words)
if st.sidebar.checkbox("character count"):
        for char in message:
         st.write(f'{char} : {message.count(char)}')       