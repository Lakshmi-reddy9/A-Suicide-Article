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
2. For each country, I will find out the maximum number of suicides taken place. -Lakshmi Vancha.

 
 
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
        - Country = Albania maxium number of sucides = 1970

    - Language being used
        - I used Python for map reducing.

    - What kind of chart will you use to display your results?
        - I will use Pie chart to display my results.
        
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
        - I will use Pie chart to display my results.
