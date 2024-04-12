# Crime Rate Prediction In California - Group 8 

## Team Members:
- Alexandre Lazzari
- Edward John Tagaca
- Eric Shih
- Hok Yin Cheung
- Marisol Cornejo

## Project Overview:
We aim to develop a machine learning model that predicts crime rates in California based on data from 2010 to 2019. Our hypothesis is that socioeconomic factors such as population, age distribution, income, unemployment rate, house prices, poverty rate, education level, and homeownership have measurable impacts on crime rates. Crime rate is defined as the total number of crimes per 100,000 people.

## Programs Used:
- Python (Pandas, Matplotlib)
- HTML/CSS/Bootstrap
- JavaScript (Plotly)
- Tableau

## Data Sources:
- [Crime Data (Open Justice)](https://openjustice.doj.ca.gov/data)
- [House Price Data (Zillow)](https://www.zillow.com/research/data/)
- [Census Data](https://data.census.gov/)
  - ACS DP02: Education Level
  - ACS DP03: Income and Unemployment Rate
  - ACS DP05: Population and Age
  - B25014: Rent vs. Homeowner
  - S1702: Poverty rate

## Machine Learning Models:
To address our project question, we tested three different machine learning algorithms:
- Multiple Linear Regression
- Random Forest Regression
- Neural Network Algorithm

## Feature and Target Variables:
Our target/dependent variable is crime rate, while our feature/independent variables include:
- % of owner-occupied homes
- % of renter-occupied homes
- Education level
- Average home price
- Age of population
- Income levels
- Unemployment rate
- Total number of crimes

## Data Preprocessing:
Before implementing machine learning models, we performed the following preprocessing steps:
- Imported libraries
- Loaded the final dataset as a CSV file
- Checked for missing values
- Split the dataset into training and testing sets

## Machine Learning Model - Linear Regression:
Linear regression is suitable for predicting numerical outcomes with a linear relationship between features. We utilized multiple linear regression to capture the linear association between crime rate and multiple independent variables. The linear regression model gave us a r-squared value of 0.52 with a accuracy of 51%.

## Machine Learning Model - Random Forest:
Random forest, a supervised learning algorithm, leverages ensemble methods to solve regression and classification tasks. We employed random forest regression to aggregate predictions from multiple decision trees. The random forest model gave us a r-squared value of .72 with a accuracy of 69%.

## Machine Learning Model - Neural Network (More Info):
In addition to linear regression and random forest, we experimented with neural network models, known for their ability to discern intricate patterns. Unlike linear regression, neural networks incorporate hidden layers to enhance prediction accuracy. Using the neural network model to preddict the crime rate based on our data gave us decent results. The neural network showed a r-squared value of 0.80 with an accuracy of 76%. 

## Summary

In our effort to find the best predictor of crime rates in California, we tried out three different machine learning models. To focus our analysis, we narrowed down our dataset by removing certain columns like Crime_Rate_per_100k, City, Violent Crime Sum, City_encoded, and Year, sticking to the most relevant variables.

We started with Linear Regression, a common approach for understanding relationships in data. While it provided some insights, it didn't perform as well as we hoped, with an R-squared value of 0.52 and an accuracy rate of 51%.

Next up was the Random Forest model, which showed more promise with an R-squared value of 0.74 and an accuracy rate of 70%. This model is known for handling complex datasets effectively.

However, the Neural Network model stole the spotlight. Known for its ability to detect intricate patterns in data, it delivered impressive results, boasting an R-squared value of 0.80 and an accuracy rate of 76%. It clearly outperformed both Linear Regression and Random Forest.

Based on these results, it's evident that the Neural Network model is the top choice for predicting future crime rates in California. Its capacity to navigate complex data and capture subtle relationships makes it the most reliable tool for this task.

# Dashboard
We utilized Tableau to create an engaging map of California, featuring cities from our dataset along with their crime rates per 100,000 population. Users can easily filter through the years from 2010 to 2019, witnessing the changes in crime rates over time. This dynamic visualization serves as an introduction, offering a clear picture of which areas experienced the highest levels of crime throughout the nine-year period.

[Crime Graphs 1](https://public.tableau.com/app/profile/alexandre.lazzari/viz/shared/B37N64Y6J)

[Crime Graphs 2](https://public.tableau.com/app/profile/hok.yin.cheung/viz/combine2_17126507246610/Story2)

# Demo crime predictor

### Requirements
In order to locally run the demo web ui you will need the following dependencies:
* python 3
* pip 3
* Flask 3
* Joblib
* pandas
* numpy
* tensorflow
* scikit-learn


You can easily install the required packages from pip3 using the following freeze requirements.txt
``` requirements.txt
flask==3.0.3
joblib==1.3.2
scikit-learn==1.3.2
scipy==1.10.1
numpy==1.24.4
pandas==2.0.3
# Optionals but recommended
keras==2.13.1
tensorboard==2.13.0
tensorboard-data-server==0.7.2
tensorflow==2.13.1
tensorflow-cpu-aws==2.13.1
tensorflow-estimator==2.13.0
tensorflow-io-gcs-filesystem==0.35.0
```

### Running the project

#### Local build
To run the project you need to execute main.py file and then navigate to `http://localhost:8000`

```
  cd demo-f;
  python3 main.py;
```
Note: on main.py  you can remove the argument `host=0.0.0.0` in case you face any host resolution error.

#### Docker build
In case you want to run it via Docker, just build the image using the Dockerfile inside demo-f, create the container and that's it.

#### Deploying on AwsAppRunner
* Point to the repository
* Branch: main
* Source directory: /demo-f

Set the following data in the runner portal:
![image](https://github.com/eshih22/crime_rate_prediction/assets/147443547/888e61bb-526f-4ca9-950c-fa102c4885ce)

Note: set the port 8000 
<img width="851" alt="image" src="https://github.com/eshih22/crime_rate_prediction/assets/147443547/109168aa-24ff-4d98-befe-bf08d8b9a700">

### Preview
<img width="961" alt="demo" src="https://github.com/eshih22/crime_rate_prediction/assets/147443547/5e761e12-0d96-4eeb-9d88-a5bff66b63ae">

<img width="819" alt="graph 1" src="https://github.com/eshih22/crime_rate_prediction/assets/147443547/f6c51351-ea94-45ed-868b-afe81ad2763a">

<img width="807" alt="graph 2" src="https://github.com/eshih22/crime_rate_prediction/assets/147443547/fb94562b-f765-4663-a3f2-2b31859c4f90">



