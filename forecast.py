import streamlit as st
import requests
from PIL import Image
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Disable the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the pickled forecast DataFrames for different areas
with open('Kenya_forecast.pkl', 'rb') as f:
    Kenya_forecast_df = pickle.load(f)

with open('Uganda_forecast.pkl', 'rb') as f:
    Uganda_forecast_df = pickle.load(f)

with open('Tanzania_forecast.pkl', 'rb') as f:
    Tanzania_forecast_df = pickle.load(f)

with open('rwanda_forecast.pkl', 'rb') as f:
    rwanda_forecast_df = pickle.load(f)
    
st.set_page_config(page_title="Food Supply Analytics Forecast", page_icon="🌾", layout="wide")
    

# Set page config and layout
st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; width: 100%; height: 60vh;">
            <img src='https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/70520367/30563c28-b0dd-4a1f-ad03-4e45385f8d1b' alt='Banner Image' style="max-width: 100%; height: auto;">
        
        </div>
        """,
        unsafe_allow_html=True
    )



page_bg_img = """
    <style>
    {
        background-image: url("https://img.freepik.com/premium-photo/ambitious-business-man-climbing-stairs-success_31965-3080.jpg?w=826");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-color: rgba(255,255,255,0);
    }
    
    
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)
# Add page title and heading
st.markdown("<h1 style='text-align: center; color: green;'>FOOD SUPPLY ANALYTICS FORECAST</h1>", unsafe_allow_html=True)

def main():
    # Streamlit app code

    
    # Create a dropdown select for the area input
    area_options = [None, 'Kenya', 'Uganda', 'Tanzania', 'Rwanda']
    area_input = st.selectbox('Country To Forecast', area_options)

    # Prompt the user to enter the start year and end year
    col1, col2 = st.columns(2)
    with col1:
        start_year_input = st.text_input("Enter the start year:")
    with col2:
        end_year_input = st.text_input("Enter the end year:")

    # Add some spacing between the input fields
    st.markdown("<br>", unsafe_allow_html=True)


    # Display the line graphs and table for the selected area and specified start and end years
    if st.button('show forecast'):
        forecast_df = None
        if area_input == 'Kenya':
            forecast_df = Kenya_forecast_df
        elif area_input == 'Uganda':
            forecast_df = Uganda_forecast_df
        elif area_input == 'Tanzania':
            forecast_df = Tanzania_forecast_df
        elif area_input == 'Rwanda':
            forecast_df = rwanda_forecast_df

        if forecast_df is not None:
            if start_year_input.isdigit() and end_year_input.isdigit():
                start_year = int(start_year_input)
                end_year = int(end_year_input)
                if start_year <= end_year:
                    forecast_subset = forecast_df.loc[(forecast_df.index.year >= start_year) & (forecast_df.index.year <= end_year)]
                    if not forecast_subset.empty:
                        # Plot the line graphs
                        plt.figure(figsize=(8, 6))
                        plt.plot(forecast_subset.index, forecast_subset['Import quantity'], label='Import quantity')
                        plt.plot(forecast_subset.index, forecast_subset['Export quantity'], label='Export quantity')
                        plt.xlabel("Year")
                        plt.ylabel("Quantity")
                        plt.title(f"Import and Export Quantities from {start_year} to {end_year}")
                        plt.legend()
                        st.pyplot()

                        plt.figure(figsize=(8, 6))
                        plt.plot(forecast_subset.index, forecast_subset["Domestic Supply Quantity"], label='Domestic Supply Quantity')
                        plt.plot(forecast_subset.index, forecast_subset['Production'], label='Production')
                        plt.xlabel("Year")
                        plt.ylabel("Quantity")
                        plt.title(f"Domestic Supply Quantity and Production from {start_year} to {end_year}")
                        plt.legend()
                        st.pyplot()

                        # Display the table with forecasted values
                        st.subheader(f"Forecasted values from {start_year} to {end_year} in Metric Tonnes(1000kgs)")
                        st.dataframe(forecast_subset)
                    else:
                        st.write("No forecast available for the specified start year and end year.")
                else:
                    st.write("Invalid input: Start year must be less than or equal to end year.")
            else:
                st.write("Invalid input: Start year and end year must be integers.")
        else:
            st.write(f"Kindly in the first dropdown select a country to forecast.")

    

    results_list = [
            "**Domestic Supply Quantity:** The total amount of agricultural commodity that is available for human consumption within a country. It is measured in metric tons.",
            "**Production:** The amount of a particular agricultural commodity that is produced within a country. It includes both crops and livestock products, and is measured in metric tons.",
            "**Export Quantity:** The amount of a particular agricultural commodity that is exported from a country to other countries. It is measured in metric tons.",
            "**Import Quantity:** The amount of a particular agricultural commodity that is imported into a country from other countries. It is measured in metric tons."
        ]

        # Display the predicted results and explanations as a list
    with st.expander("Click here for description about the columns"):
        for result in results_list:
            st.markdown(result)
    

if __name__ == '__main__':
    main()


