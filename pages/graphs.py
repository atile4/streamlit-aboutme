import streamlit as st
import requests

st.header("Graphs")

st.text_input("Type in a Tetrio username: ", key="name", placeholder="")
name = st.session_state.name

def ranking():
    rank_data = requests.get("https://ch.tetr.io/api/users/" + str(st.session_state.name)) 
    rank = rank_data.json()['data']['user']['league']['percentile_rank'].upper()
    tr = rank_data.json()['data']['user']['league']['rating']

    col1.markdown("TETRA League Standings: ")
    if rank == 'Z':
        col1.markdown("# N/A")
    else:
        col1.markdown("# " + rank)

def records():
    record_data = requests.get("https://ch.tetr.io/api/users/" + str(st.session_state.name) + "/records/")
    col2.markdown("Fastest 40 line sprint: ")
    col3.markdown("Blitz Score Record: ")

    testscore = record_data.json()['data']['records']
    if record_data.json()['data']['records']['40l']['record'] == None: col2.markdown("# N/A")
    else: 
        scorel = testscore['40l']['record']['endcontext']['finalTime'] / 1000
        scorel_min = int(scorel) // 60
        scorel_sec = scorel % 60
        if scorel_sec < 10: col2.markdown("# " + str(scorel_min) + ":0" + f'{scorel_sec:.3f}')
        else: col2.markdown("# " + str(scorel_min) + ":" + f'{scorel_sec:.3f}')

    if record_data.json()['data']['records']['blitz']['record'] == None: col3.markdown("# N/A")
    else: 
        blitz = testscore['blitz']['record']['endcontext']['score']
        col3.markdown("# " + f'{blitz:,}')


if name != "":
    r = requests.get("https://ch.tetr.io/api/users/" + name)
    if r.json()['success'] != False:
        col1, col2, col3 = st.columns(3)
        ranking()
        records()
    else:
        st.markdown("# [ERROR]: \"" + name + "\" is not a valid username")
    



st.markdown("API: https://ch.tetr.io/api/")








