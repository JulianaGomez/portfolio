# Taming turbulence with Machine Learning

Project developed for the Machine Learning at Scale Class, as part of my Masters in Information and Data Science at UC Berkeley.  This project predicts flight departure delays of 15 minutes or more at least 2 hours before the scheduled departure time to improve airport customer satisfaction. We leveraged the 5-year (2015-2019) On-Time Performance and Weather (OTPW) dataset that included flight, airport, and weather data for performing Exploratory Data Analyzes (EDA) and feature selection/engineering, data pipeline construction, and modeling. We experimented with various machine learning models to determine the best predictive results. We engineered features such as previous flight features, weather features, and time-dependent features, and built a modeling pipeline that could be used to predict on unseen data. We experimented with numerous models: linear regression (LR), random forest (RF), gradient-boosted random forest (GBRF), and Multilayer Perceptron Classifier (MLP). We evaluated the models with regression metrics and classification metrics. Our main metric was F𝛽 (𝛽=0.5). F𝛽 combines precision and recall performance, considering both true delays (precision) and delays in all departures (recall). Our best (most comprehensive) model was Ensemble via MLP with an F𝛽 of 0.45 coupled with our best pipeline built in ML flow, taking the preprocessed dataset as input and model results as output. Included in the pipeline were feature normalization, training, and cross-validation. We also considered future works to increase value for our stakeholders.

*Authors*: Ray Cao, Jenna Sparks, Dhyuti Ramdas, Rachel Gao, Juliana Gómez Consuegra

 


## My role
I was in charge of sourcing new data for flights between 2016 and 2019, performing EDA and feature engineering on weather data, and performing a gap analysis for our best performing model. All of my code is included as follows: 

|Notebook|Contents|
|---|---|
|3m_OTPW_weather_EDA| EDA of weather data over 3 months|
|1Y_raw_weather_EDA| EDA of weather data over 1 year|
|2015_1YR_OTPW_parquet_train_s1_weather_feature_engineering| Feature engineering for weather variables|
|additional_data_sourcing_weather_2020|Code for sourcing additional weather information for the year 2020|
|additional_data_sourcing_weather_full_2020_2023|Code for sourcing additional weather information for the year 2020-2023|
|events_2015_2019|List of US holidays and special events between 2015 and 2019|
|natural_disasters_2015_2019| Natural disasters that took place between 2015 and 2019|
|gap_analysis_ensemble| Gap analysis, examining where the best performing model is struggling|