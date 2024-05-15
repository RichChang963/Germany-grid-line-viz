# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: : Sangeeta Mohanty, Yu-Chi Chang
# SPDX-License-Identifier: MIT
# coding: utf-8

import pandas as pd
import streamlit as st

def plot_map(data: pd.DataFrame, config: dict):
    """Plot the grid lines and data on Germany map.

    Parameters
    ----------
    data: pd.DataFrame
        Input table.
    config : dict
        A dictionary of config settings.
    """
    st.set_page_config(
        layout="wide",
        page_title=config["layout"]["page_title"]
    )

    st.title(config["layout"]["chart_title"])
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
