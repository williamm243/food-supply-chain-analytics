### FAOStat-Dataset-Time-Series
##### project authors : DATA JEDIS 
# Forecasting Food Production: Analyzing Trends, Challenges, and Opportunities in East Africa

![yfood_outlook_june23_pr_banner](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/70520367/30563c28-b0dd-4a1f-ad03-4e45385f8d1b)


## Business Understanding 

### Overview

East African food production plays a crucial role in ensuring food security for its population. The country's agricultural sector employs a significant portion of the population and contributes to the national economy. The countries are  known for their diverse agricultural activities, including crop cultivation, livestock rearing, and fisheries.

In recent years,  strides have been made  to improve food sufficiency  through various initiatives, including promoting modern farming techniques. The efforts have led to increased agricultural productivity and improved crop yields. The Supply Chain Analytics Forecast aims to assist users in analyzing and predicting supply chain dynamics for selected countries, enabling better decision-making and planning in the field of supply chain management.

The project aims to provide insights into the supply chain dynamics of different countries, specifically focusing on metrics such as import quantity, export quantity, domestic supply quantity, and production. It can be used by governments, businesses, and other organizations to make informed decisions about the supply chain of agricultural commodities. The project willl also  help users to identify potential shortages or surpluses of commodities, and to make plans to mitigate these risks. The forecast helps users to track the performance of the supply chain over time, and to identify areas where improvements can be made.


### Objectives

The objectives of the prediction model for food production in Kenya are as follows:

1. Forecasting Food supply balances : The primary objective of the model is to accurately predict food supply balances  in Kenya. By analyzing historical data, current conditions, and relevant variables, the model aims to provide forecasts that reflect the expected domestic supply quantity, imports and exports over a range of years.
2.Enhancing Food Security: Ultimately, the objective of the prediction model is to contribute to improving food security in Kenya. By accurately forecasting food production and assessing sufficiency, the model aims to support proactive measures that ensure a consistent and adequate food supply for the growing population.

3. Assessing Food Sufficiency: The model seeks to determine whether the projected food balances  will be sufficient to meet the needs of the population. It aims to assess the adequacy of food supply in order to identify potential shortfalls or surpluses.

4. Informing Decision-Making: The model aims to provide valuable insights to policymakers, government agencies, and agricultural stakeholders. By offering reliable predictions, the model can inform decision-making processes related to resource allocation, import/export planning, and interventions to ensure food security.

5. Optimizing Resource Allocation: The model aims to optimize the allocation of resources by identifying areas of potential food shortages or surpluses. This can help in directing resources, such as irrigation, fertilizers, and agricultural investments, to areas that require them the most.

6. Promoting Sustainable Farming Practices: By considering various factors that impact food production, such as climate conditions and agricultural practices, the model can promote sustainable farming techniques. It can provide recommendations for resilient and environmentally-friendly practices that enhance productivity while minimizing negative impacts.


### Success metrics
- Root Mean Square Error (RMSE): RMSE calculates the square root of the average squared difference between the predicted values and the actual values. It gives an estimate of the model's prediction error, with lower values indicating better performance.
### Data Understanding

The data from this project comes from the FAOStas site.
[Food Balances](https://www.fao.org/faostat/en/#data/SCL)

A snippet of some of the  columns:

1. Area: This column contains the country name or area name.
 
2. Element: This column provides a description or name for the entities or categories represented by the element code.

3. Item: This column contains the product or item classification name.

4. Year: This column represents the year when the data was collected or recorded.

5. Unit:  specifies the measurement unit  for the corresponding item 

6. Value: This column provides the numerical value associated with a specific item, measured in the units specified in the "Unit" column. It represents the quantity or magnitude of the item for a given year and area.
    
### Explanatory Data Analysis
##### Top 10 Items Produced in Eastern Africa
![1](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/99483846/7c324e49-febb-44e6-8f47-fcb008560297)

$ inference $
- After analyzing a visualization of the top 10 items produced by East African countries, we can observe distinct production patterns. Cassava and products emerges as the dominant product, closely followed by Bananas. Conversely, potatoes and associated products exhibit the lowest production levels among the selected items.
### Bivariate Analysis 
![import](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/99483846/5cdfb8dd-0b22-4458-ae20-ad23503c4f9a)
$ inference $   
- The bar graph represents the comparison between the import quantity and export quantity in the dataset. The x-axis shows the two elements: "Import Quantity" and "Export Quantity." The y-axis represents the corresponding quantities.

- The bars in the graph depict the quantities, with the cyan color indicating the import quantity and the magenta color indicating the export quantity.

- This graph provides a visual representation of the difference between the import and export quantities, allowing for easy comparison between the two elements.
### Multivariate Analysis
![line pl](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/99483846/9b7136a5-289a-42e5-991b-daf69090359a)
Overall, the plots provide an overview of the growth patterns in domestic supply quantity for these countries over the specified time period. They highlight the variations and trends in supply levels, allowing for a comparison between the different countries.
##### Preprocessing Kenyan dataset for  modeling  

![LINES](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/99483846/a149e6be-0b2b-4340-9d4b-072a4284d44d)

- There is an upward trend over the years across all the elements except for exports which seem to be stagnant
##### Correlation matrix kenya

![Corr](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/99483846/df7050f0-2136-4df5-b135-78b641290021)
The elements are highly correlated because they affect each other
#### Modelling 
### Baseline model
Baseline models serve as a reference point or a benchmark against which the performance of more complex or sophisticated models can be compared. They provide a simple and straightforward approach to modeling a problem, often with minimal assumptions or complexity.
Overall, baseline models offer a simple starting point and serve as a valuable reference for understanding and assessing the performance of more complex models. They provide a baseline against which advancements in modeling techniques and feature engineering can be measured, guiding the iterative process of model development and improvement.
Our baseline model is the AR model 
### AR Model 
Predicts the future values of a variable based on its own past values. the AR model can estimate future values and understand how the series evolves over time.
### Arima model 
A time series forecasting model that combines autoregressive (AR) and moving average (MA) components along with differencing to handle non-stationary data. By incorporating autoregressive, moving average, and differencing components, ARIMA models can capture both short-term and long-term patterns in the data

### SARIMA MODEL 
The SARIMA (Seasonal AutoRegressive Integrated Moving Average) model is a popular time series forecasting method that extends the capabilities of the ARIMA model to handle seasonal patterns. It is particularly useful when dealing with data that exhibits both trend and seasonal components.

The SARIMA model incorporates three main components: autoregression (AR), differencing (I), and moving average (MA). Additionally, it includes a seasonal component represented by an additional set of AR, I, and MA terms.

### Deployment 
The web application is built using Streamlit, a Python framework for creating interactive data applications. The purpose of the project is to visualize and analyze the forecasted supply chain data for different countries.
The application allows the user to select a country from a dropdown menu and enter the start year and end year for the forecast. After clicking the "show forecast" button, the application displays line graphs showing the import and export quantities as well as the domestic supply quantity and production for the selected country and specified time period. Additionally, a table with the forecasted values is shown.
  ![image (2)](https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/99483846/11432c70-c3ef-4945-9689-b49acc6e6374)
### Project authors 
##### Agape Gichuki
##### Marwa Osman 
##### William Onsare
##### Dorine Langat
##### Nyokabi Waiganjo 
##### Mary Wairimu






