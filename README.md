# A Suicide Article
- The project we are working is on a Suicide data for the Big Data Course. 
- Group-04

## List of developers
- Sai Sri Lakshmi Vancha
- Rayaan Ahmed
- Gopi Amara
- Vinay Linginedi

## Links
- https://github.com/Lakshmi-reddy9/A-Suicide-Article
- https://github.com/Lakshmi-reddy9/A-Suicide-Article/issues

## Introduction
- In this project we will be sorting our suicide data and calculating the number of people dying due to suicide in a given year, at a given place and for a particular gender. The main reason we took this dataset is for suicide prevention.

## DataSource
- This dataset is created with data from 1985 to 2016, the data is retrieved from United Nations Development Program (2018) Human development index (HDI), World Bank (2018), World Health Organization (2018).

## DataSource Link

- [DataSource](https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016)



## The Challenge
- Volume: It is 2.58MB of dataset where we have 27821 records. It is a 31 years of dataset.
- Variety: It is a structured dataset and in a CSV format.
- Velocity: It is updated for every two years.
- Veracity: The dataset is clear with no unnecessary data, The dataset is collected from the World Bank Dataset Terms of Use so it is a certified and trustworthy.
- Value: From the dataset we can give the number of people commiting suicide for a year at a given place and at a particular age.

## Big Data Questions
1. For each year, I will calculate the total number of suicides taken place. -Rayaan Ahmed.
2. For each country, I will find out the total number of suicides taken place. -Lakshmi Vancha.
3. Far each sex, I will find the average number of sucides taken place. -Gopi Amara
4. For a given age span, I will find the total number of suicides taken place. -Vinay Linginedi. 
 
## Big Data Solutions
- Sai Sri Lakshmi Vancha 
    - Mapper input: One line of data that mapper will read:
        - 1 Albania	1995	male	55-74 years	9	178000	5.06	Albania1995	0.619	2,424,499,009	835	Silent
        
    - Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:
        - Albania 14
        - Cyprus 4
        - Qatar 0
        - Ukraine 19
        - United States 4199

    - Reducer output
        - Country = Albania total number of sucides = 1970

    - Language being used
        - I used Python for map reducing.

    - What kind of chart will you use to display your results?
        - I will use Box and Whisker to display my results.

        ![Box and Whisker](https://github.com/Lakshmi-reddy9/A-Suicide-Article/blob/master/images/total_suicides_by_country.png)
        
    - Summary : From the graph if we sort the data from highest to lowest order Russia tops the chart with arab countries in the second place Jamaica in the third place the other countries are ranged from 5000 to 1 suicide in the 31 years i.e. from 1985 to 2016. As per wikipedia the suicide rate in Russia is higher due to heavy alcohol consumption.
       
- Rayaan Ahmed 
    - Mapper input: One line of data that mapper will read:
        - 1 Albania	1995	male	55-74 years	9	178000	5.06	Albania1995	0.619	2,424,499,009	835	Silent
        
    - Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:
        - 1987 14
        - 1988 17
        - 1995 13
        - 1997 36
        - 2007 29

    - Reducer output
        - year = 1987 total number of sucides = 126842

    - Language being used
        - I used Python for map reducing.

    - What kind of chart will you use to display your results?
        - I will use Scatter plot to display my results.
        
        ![Scatter Plot](https://github.com/Lakshmi-reddy9/A-Suicide-Article/blob/master/images/total_suicides_by_year.png)
        
     - Summary : The given graph is sorted from highest rate of suicides to lowest rate where the year 2008 has the count 1100 approximately and the year 2015 has the lowest range of suicides taken place that is around 180. According to the Forbes the reason for the highest rate of suicides in 2008 is due to financial debts, job loss and home foreclosures.

- Gopi Amara 
    - Mapper input: One line of data that mapper will read:
        - 1 Albania	1995	male	55-74 years	9	178000	5.06	Albania1995	0.619	2,424,499,009	835	Silent
        
    - Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:
        - male 21
        - female 16
        - male 13
        - female 36
        - male 29

    - Reducer output
        - sex = male average number of sucides = 373.034 ~ (373)

    - Language being used
        - I used Python for map reducing.

    - What kind of chart will you use to display your results?
        - I will use Histagram to display my results.
     
     ![Histagram](https://github.com/Lakshmi-reddy9/A-Suicide-Article/blob/master/images/total_suicide_by_gender.png)
     
    - Summary : The graph says that Male suicides are far more when compared to female suicides, according to Forbes "The increase was four times higher in men than in women, which the researchers suggested was because men feel greater pressure and shame when faced with financial failure, and are also less likely to seek psychiatric care."
    
- Vinay Linginedi 
    - Mapper input: One line of data that mapper will read:
        - 1 Albania	1995	male	55-74 years	9	178000	5.06	Albania1995	0.619	2,424,499,009	835	Silent
        
    - Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:
        - 15years - 24years 21
        - 35years - 54years 16
        - 55years - 74years 4
        - 25years - 34years 19
        - 5years - 14years 11
    - Reducer output
        - Age = 15years - 24years Total number of suicides taken place = 808542
    - Language being used
        - I used Python for map reducing.

    - What kind of chart will you use to display your results?
        - I will use Box and Whisker chart to display my results.

     ![Box and Whisker](https://github.com/Lakshmi-reddy9/A-Suicide-Article/blob/master/images/total_suicides_by_age.png)
     
     Summary: From the chart we can observe that there is a exponential growth of suicides as the age span increases and there is a drastic decrease of suicides from age 70.
