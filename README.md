# README
![Alt Text](https://media.giphy.com/media/3o6Ztr61bWRy8aDBJu/giphy.gif)


## What is this README and how to use it?
This README is a beefed up table of contents for my MOD-1 Data Science boot camp project with the Flatiron School. Use this to help navigate the files and or peruse the summary of each notebook!
__________________________________________________________________

## Relevant File Contents of This Repository
1. Raw DataCleaning
  1. zippedData folder - contains raw data used in this project <br/>

2. Project Notebooks (.ipynb)
  * DataCleaning - This notebook contains all of the steps to turn the raw data into the cleaned data used for analysis <br/>

  * Evaluating The Box Office
    - This notebook contains analyses pertaining to the profitability of movies through box domestic office numbers
    - link
  - Saif Question 1
    - brief description
    - link
  - Saif Question 3
    - brief description
    - link
  * Heather Final Notebook
    * brief description
    * link
___________________________________________________________________________________________
## Notebook Summaries

#### ***Reviewing the Prompt***
Microsoft sees all the big companies creating original video content, and they want to get in on the fun. They have decided to create a new movie studio, but the problem is they don’t know anything about creating movies. They have hired you to help them better understand the movie industry.

Your team is charged with doing data analysis and creating a presentation that explores what type of films are currently
doing the best at the box office. You must then translate those findings into actionable insights that the CEO can use when deciding what type of films they should be creating.
______________________________________________________________
### Evaluating The Box Office
#### ***Important Questions to Answer***<br/>
Firstly, before even evaluating how to produce great content, we must make sure the movie industry is showing healthy economic fundamentals. To evaluate if the movie industry is a healthy industry we will aim to answer the questions proposed in the beginning of this notebook.

#### ***1. Are ticket sales growing since 2000?***<br/>
[Figure 1.1](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%20%201.0.png) answers this question pretty plainly looking at the blue line representing ticket sales. Ticket sales shows an unicumbered picture of the demand for the movies created that year. From 2000 to 2015 ticket sales were not growing until a crazy spike going around 2018. Ticket sales after 2019 have declined dramatically after an impressive 2018 back to the same levels they were at the entire 2 decades we evaluated. ***There is no measurable growth in demand from 2000 to 2019.***


#### ***2. Are movies making more or less profit since 2000?***<br/>
This question is easily answerable looking at [Figure 1.1](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%20%201.0.png), [Figure 2.2](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%202.2.png), and [Figure 3.0](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%203.0.png). Looking at [Figure 2.2](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%202.2.png) we see the relationship of profit per movie over time with a line of best fit plotted showing the trend. The slope is flat to barely negative. [Figure 3.0](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%203.0.png) shows the correlation coefficient between profit per movie and the year it was released is -0.17. This also shows there is a negligible negative correlation to the year it was released and the profit of the movie. ***This shows that movies are not becoming more profitable over time.***


#### ***3. Are movies getting more expensive to make since 2000?***<br/>
Similarly to question 2 lets look at [Figure 2.1](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%202.1.png) and [Figure 3.0](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%203.0.png). [Figure 2.1](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%202.1.png) shows production budgets per movie over time. The line of best fit is showing a steep ascent which means that productions budgets have been growing as the years passed. [Figure 3.0](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%203.0.png) shows the correlation coefficient between these two variables is 0.64. This is proof of a strong positive correlation of these values as the years go on the production budgets also increase. ***This shows that movies are becoming increasingly expensive to make over time.***


#### ***4. Does a larger production budget increase your chances of producing a profitable movie?*** <br/>
[Figure 3.0](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/figureImages/Figure%203.0.png) measures the correlation between multiple variables including production budget and profit per movie and ROI. The values for production budget vs profit is 0.055 and production budget vs ROI is -0.14. This means that while production budget does have a little effect on ticket sales the increased cost in the budget is greater therefore hurting your return metrics. ***This shows that a larger production budget has no change to your profit and actually will hurt your return metrics.***

#### ***Conclusion***
In summary, on this data I would not recommend entering the movie industry as an inexperienced content creator. The majority of movies are not doing well and there is an extremely wide range in possible outcomes. That being said, I believe this data is leaving out a major part of the revenue stream for movies in the on demand market. If we had data on the income generated from on demand services such as Netflix it may shed a much more positive light on becoming a content creator.

### Saif Question 1
### Saif Question 3
### Heather Final Notebook
