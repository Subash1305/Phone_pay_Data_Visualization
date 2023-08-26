import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import PIL
from PIL import Image
import requests 
import seaborn as sns
import base64
import folium
from streamlit_folium import folium_static
from streamlit_lottie import st_lottie

mydb = mysql.connector.connect(host="localhost", user="root", passwd="@jaykumar_A04", database="phonepe_pulse")

cursor = mydb.cursor()

with st.sidebar:
    selected = option_menu(
    menu_title = None,
    options = ["Home", "Insights", "Locations"],
    icons = ["house", "book", "map", "envelope"],
    default_index=0,
)

#HOME

if selected == "Home":
    st.title("Welcome to PhonePe Pulse")
    st.image("FILES\\main.PNG")
    st.write("_____")
    col1, col2, col3= st.columns(3)
    col1.image(Image.open("FILES\\screen.jpg"))
   

    with col2:
        st.write("PhonePe transactions in India display diverse patterns across states, uncovering distinct trends in payment methods, merchant categories, and transaction volumes. Analyzing user data provides valuable insights into regional preferences and user behavior. Visualizing and comparing these findings offer a comprehensive understanding of the digital payment landscape, enabling effective strategies for optimizing services and enhancing user experiences based on specific state and user segment requirements.")
    with col3:
        st.image("FILES\\screen.jpg")
    "____"
    st.subheader("Overview of Digital Transactions")
    st.image("FILES\\india.PNG")
    st.image("FILES\\indian1.PNG")
    "____"
    st.subheader("Intro to PhonePe pulse")
    st.video("FILES\\phone_video.mp4")



#Insights

if selected == "Insights":

    st.title("DATA VISUALIZATION")
    st.subheader("This Section helps to indentify the Transactions and users details in the view of 'CHARTs'")

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_visualization = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_cuKhxGQKFB.json")

    st_lottie(lottie_visualization)
    
    def retrieve_data_from_mysql(table_name):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, mydb)
        return df

    def download_dataframe(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>'
        return href

    def visualize_pie_chart(df):
        st.subheader("Pie Chart")
        col_name = st.selectbox("Select a column for Pie Chart", df.columns)
        pie_data = df[col_name].value_counts()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    def visualize_plotly_chart(df):
        st.subheader("Plotly Chart")
        x_column = st.selectbox("Select X-axis column", df.columns)
        y_column = st.selectbox("Select Y-axis column", df.columns)
        fig = px.scatter(df, x=x_column, y=y_column, title="Plotly Chart")
        st.plotly_chart(fig)

    def visualize_line_chart(df):
        st.subheader("Line Chart")
        x_col = st.selectbox("Select x-axis column", df.columns)
        y_col = st.selectbox("Select y-axis column", df.columns)
        fig, ax = plt.subplots()
        ax.plot(df[x_col], df[y_col])
        ax.set_xticklabels(df[x_col], rotation=90, ha='center')
        st.pyplot(fig)

    def visualize_bar_chart(df):
        st.subheader("Bar Chart")
        x_col = st.selectbox("Select x-axis column", df.columns)
        y_col = st.selectbox("Select y-axis column", df.columns)
        fig, ax = plt.subplots()
        ax.barh(df[x_col], df[y_col])
        ax.set_yticklabels(df[x_col], rotation=90, ha='center')
        st.pyplot(fig)

    def visualize_scatter_plot(df):
        st.subheader("Scatter Plot")
        x_col = st.selectbox("Select x-axis column", df.columns)
        y_col = st.selectbox("Select y-axis column", df.columns)
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xticklabels(df[x_col], rotation=90, ha='center')
        st.pyplot(fig)

    def visualize_heatmap(df):
        st.subheader("Heatmap")
        corr_matrix = df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    
    def visualize_histogram(df):
        st.subheader("Histogram")
        col_name = st.selectbox("Select a column for Histogram", df.columns)
        fig, ax = plt.subplots()
        ax.hist(df[col_name], bins='auto')
        ax.set_xticklabels(df[col_name], rotation=90, ha='center')
        st.pyplot(fig)


    def main():
        st.title("Download DataFrame from Streamlit")
        
        # Define table names
        table_names = ["data_agg_trans", "data_agg_user", "data_map_trans", "data_map_user", "data_top_trans", "data_top_user"]
        
        # Selectbox to choose table
        selected_table = st.selectbox("Select a table", table_names)
        
        # Retrieve data for the selected table
        df = retrieve_data_from_mysql(selected_table)
        
        # Dataframe display
        st.subheader(selected_table)
        st.dataframe(df) 
        
        # Download CSV button
        st.markdown(download_dataframe(df), unsafe_allow_html=True)
        
        # Data visualization options
        st.subheader("Data Visualization")
        visualization_option = st.selectbox("Select a visualization", [
            "Pie Chart", "Line Chart", "Bar Chart", "Scatter Plot", "Heatmap", "Histogram", "Plotly Chart"])
        
        # Sample subset of data for visualization
        df_sample = df.sample(n=10, random_state=1)  # Sample 10 random rows
        
        # Perform data visualization based on selected option
        if visualization_option == "Pie Chart":
            visualize_pie_chart(df_sample)
        elif visualization_option == "Line Chart":
            visualize_line_chart(df_sample)
        elif visualization_option == "Plotly Chart":
            visualize_plotly_chart(df_sample)
        elif visualization_option == "Bar Chart":
            visualize_bar_chart(df_sample)
        elif visualization_option == "Scatter Plot":
            visualize_scatter_plot(df_sample)
        elif visualization_option == "Heatmap":
            visualize_heatmap(df_sample)
        elif visualization_option == "Histogram":
            visualize_histogram(df_sample)

    if __name__ == '__main__':
        main()


#Locations

if selected == "Locations":

    st.title("Indian Map Visualization")

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_mapping = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_hgdis2eb.json")
    "_____"

    st_lottie(lottie_mapping)

    def retrieve_data_from_mysql(table_name):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, mydb)
        return df
    
    center = [20.5937, 78.9629]  # India's approximate latitude and longitude

    def visualize_map(df):
        m = folium.Map(location=center, zoom_start=5)

        for index, row in df.iterrows():
            html = ""
            for column in df.columns:
                if column in row:
                    html += f"<b>{column}:</b> {row[column]}<br>"
                else:
                    html += f"<b>{column}:</b> Column Not Present<br>"
                
            iframe = folium.IFrame(html, width=300, height=150)
            popup = folium.Popup(iframe, max_width=300)

            folium.Marker([row['latitude'], row['longitude']], popup=popup).add_to(m)
                
        folium_static(m)

    def main():

        table_names = ["data_agg_trans", "data_agg_user", "data_map_trans", "data_map_user", "data_top_trans", "data_top_user"]

        selected_table = st.selectbox("Select a table", table_names)

        df = retrieve_data_from_mysql(selected_table)

        st.subheader("Click on the popup to see the details of that state")
        visualize_map(df)
        st.map(df)

    if __name__ == '__main__':
        main()


    