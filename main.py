import pandas as pd
import numpy as np
import streamlit as st


st.set_page_config(layout="wide",
                   page_title="Germany-grid-line-viz",
                   )

def display():
    
    #getting result years
    # try:
    #     st.session_state.sce1_years = get_result_years(sc = st.session_state.sce1,
    #                                                sec= st.session_state.sector)
    # except FileNotFoundError:
    #     st.write('folder not found: {}'.format(st.session_state.result_path+
    #                             '/'+st.session_state.sce1+'/csvs/'+
    #                             st.session_state.sector+'/'))
    st.title("Grid Lines of Germany")
    st.info("Move the slide bar to see the load changes across different periods")
    data = pd.DataFrame({
        "year": [2020, 2021,2022],
        "load": [100,200,300],
        "latitude": [54, 52, 50],
        "longitude": [15, 8, 6]
    })
    year_list = data["year"].to_list()
    year = st.slider("Select year",year_list[0],year_list[-1], key="load")
    st.map(data[data.year == year], zoom=5)
    

if __name__ == '__main__':
    display()

    