# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: : Sangeeta Mohanty, Yu-Chi Chang
# SPDX-License-Identifier: MIT
# coding: utf-8

import pandas as pd
import streamlit as st

def plot_map(data: pd.DataFrame):
    """Plot the grid lines and data on Germany map.

    Parameters
    ----------
    data: pd.DataFrame
        Input table.
    """
    st.set_page_config(
        layout="wide",
        page_title="Germany-grid-line-viz"
    )

    st.title("Grid Lines of Germany")
    st.info("Move the slide bar to see the load changes across different periods")

    year_list = data["year"].to_list()
    year = st.slider("Select year",year_list[0],year_list[-1], key="load")
    st.map(data[data.year == year], zoom=5)
