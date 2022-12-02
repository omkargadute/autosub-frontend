import streamlit as st
import requests

st.set_page_config(page_title="AutoSub",layout="wide")

st.title("AutoSub - Video Subtitle Genrator")
st.subheader("Upload Video for Generating subtitles")

generationStarted = False
gotSubtitle = False

def loadVideo():
    st.video('clip2_subtitled.mp4')

def getVideo(file_name):
    global generationStarted
    generationStarted = True
    URL = 'http://127.0.0.1:8000/getSubtitledVideo/'+file_name
    result = requests.get(URL)
    data = result.json()
    print(data['Message'])
    global gotSubtitle
    gotSubtitle = True
    return True

input_video = st.file_uploader("Please upload you video here",type=["mp4"])

if input_video is not None:
    file_name = input_video.name
    st.button(label="Generate Subtile",on_click=getVideo,args=(file_name,))
    load_video = st.button(label="Load Video")
    if load_video:
        st.video('clip2_subtitled.mp4')


