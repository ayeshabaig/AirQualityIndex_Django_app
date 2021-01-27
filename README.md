# AirQualityIndex(AQI)App

This application is based on the Django Framework. 
The front end utilzes the bootstrap front end. For the charts, it utilzes charts.js. 
This project is a basic data science project that allows you to use a ML to visualize test and train based on the model
The project is structured with nested urls with the roots linked to the visuals. Each application/url either render the routes or handles the data sent from the front end.
3 Apps: visualizations, models training and testing, authentication.
This is based on a monolithic framework.


# The predictive analytics ustilized Scikit-Learn API. 
The training was done in 2 phases using the form with a imput data values unique to the lablel and data point specified. (supervised learning)

It utlizes a Supervised Machine Learning Model. The Algorithm is based on Regression and Decision Trees.
Scikit-learn does not support incremental training, therefore we use a trained dataframe which was used to train the model and the data points. They are concatenated with this to create a new model with the old data points.
It utilizes historical data that can be concatenated with the new data to create a new model. To scale the input of new data, concatenation was utlized. 

Testing the data: While the training phase in effect the pickle file is stored and fetched whenever a testing route is called with a single data point with some values and the target value and the values are put into the testing bucket and the outcome by the model that outcome and the lable are test is done using the rmse.
You can also use a csv and use the predict action to predict the rmse.

# Overview: Motivation

The increase in fine particulate matter PM2.5 levels over the last 50 years has resulted in a significant decline in overall air quality for people living in urban hubs in the United States. The American Lung Association in their 2020 State of the Air study estimates that over 150 million people in the United States - 48.5% of the population - live in counties or zones with unhealthy air as measured by ozone concentrations and PM2.5 concentrations (2020). PM2.5, whose particle size is less than 2.5 microns in diameter, poses a significant health risk to overall public health. Due to its small size, these particles are dispersed widely and have the ability to enter deep into the lungs, and even the bloodstream causing a myriad of respiratory and cardiovascular issues such as increased respiratory problems, decreased lung function, asthma, irregular heartbeats, and premature death due to heart and lung disease (Environmental Protection Agency [EPA], 2020). Due to the seriousness of high PM2.5 levels, there is government monitoring of air pollution levels; however, a sparse network of air pollution monitors with infrequent data collection provide an incomplete analysis of air quality and begets the need for a more localized model. The ability to locate, measure, and predict PM2.5 levels is vital for protecting vulnerable populations within local communities. The goal of this study was to develop a high-resolution air pollution model which can predict air quality levels at hourly intervals providing residents in the District of Columbia a tool for making healthier decisions about where and when they spend their time outside.

Keywords: PM2.5, Air Quality, Ozone Concentrations, Health, Deep Lungs and Bloodstream, Premature Death.

## AirQuality Full-Stack App


This is a data science application based on AQI Data in the DC metro area.

https://github.com/ayeshabaig/Air-Pollution

This is a modification in a Full stack Django Project of the original as I have scaled down the features.  

http://ec2-3-141-20-138.us-east-2.compute.amazonaws.com/



