# load libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure

def app():

    # Add Favicons, Page Titles etc
    st.set_page_config(
        page_title="Vehicle Pricing Database",
        page_icon="🎈",
        layout="wide",
        initial_sidebar_state="auto")

    # set logo, title and subheader
    st.image("image/serene.jpg", use_column_width="always")
    st.title("Vehicle Pricing Database 🎈")
    st.subheader("About this app")
    st.write(
        """ This app allow car enthusiasts to find some interesting car prices from various regions in the US based on the selections given by the user.""")

    # Read in the file
    df = pd.read_csv("data/vehicles.csv")
    df = df.reset_index(drop=True)

    # Using object notation
    with st.sidebar:
        man_output = st.selectbox("Select Car Manufacturer", df.Manufacturer.unique().tolist())
        condition_output = st.selectbox("Select Car Condition", df.Condition.unique().tolist())
        cylinder_output = st.selectbox('Pick the number of Cylinders', df.Cylinders.unique().tolist())
        year_output = st.select_slider('Select the car Year', df.Year.unique().tolist())
        trans_output = st.radio('Select the Transmission', df.Transmision.unique().tolist())
        type_output = st.selectbox('Select the Type of Car', df.Type.unique().tolist())
        colour_output = st.selectbox('Select the Colour of Car', df.Paint_Color.unique().tolist())
        submit = st.button('Submit')

    col1, col2 = st.columns(2)

    with col1:
        try:
            if submit:
                df1 = df[
                    (df.Manufacturer == man_output) & (df.Condition == condition_output) & (
                                df.Cylinders == cylinder_output) & (
                            df.Year == year_output) & (df.Transmision == trans_output) & (df.Type == type_output) & (
                            df.Paint_Color == colour_output)]
                st.subheader("Regions by Price")
                fig = Figure()
                ax = fig.subplots()
                sns.barplot(x=df1.Region, y=df1.Price, color='goldenrod', ax=ax)
                ax.set_xlabel('Region')
                ax.set_ylabel('Price')
                ax.set_xticklabels(df1.Region.unique().tolist(), rotation=45)
                st.pyplot(fig)
        except:
            st.write("No cars available. Try changing your options")

    with col2:
        try:
            if submit:
                df1 = df[
                    (df.Manufacturer == man_output) & (df.Condition == condition_output) & (
                                df.Cylinders == cylinder_output) & (
                            df.Year == year_output) & (df.Transmision == trans_output) & (df.Type == type_output) & (
                            df.Paint_Color == colour_output)]
                st.subheader("Current Mileages by Region")
                fig = Figure()
                ax = fig.subplots()
                sns.barplot(x=df1.Region, y=df1.Odometer, color='goldenrod', ax=ax)
                ax.set_xlabel('Region')
                ax.set_ylabel('Mileage')
                ax.set_xticklabels(df1.Region.unique().tolist(), rotation=45)
                st.pyplot(fig)
        except:
            st.write("No cars available. Try changing your options")

    with st.container():
        if submit:
            df1 = df[
                (df.Manufacturer == man_output) & (df.Condition == condition_output) & (df.Cylinders == cylinder_output) & (
                        df.Year == year_output) & (df.Transmision == trans_output) & (df.Type == type_output) & (
                        df.Paint_Color == colour_output)]
            if df1.shape[0] != 0:
                st.subheader("Car Price verses Mileage")
                fig = Figure(figsize=(10, 5))
                ax = fig.subplots()
                sns.scatterplot(x=df1.Odometer, y=df1.Price, color='goldenrod', ax=ax)
                ax.set_xlabel('Mileage')
                ax.set_ylabel('Price')
                st.pyplot(fig)

                st.subheader("Car Dataset")
                st.dataframe(df1)

            else:
                st.image('image/cat.jpg')

if __name__ == "__main__":
    app()