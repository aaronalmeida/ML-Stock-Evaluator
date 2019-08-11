# ML-Stock-Evaluator
A Machine Learning based stock evaluator that will label stocks as buys or sells based on certain fundametal signals.

First let me start of with an obligatory meme to sum up the entire project
![alt text](https://github.com/aaronalmeida/ML-Stock-Evaluator/blob/master/machineLearning.png)

I'd like to shout out @sentdex on YouTube for an amazing guide that I used to create this.


## Technologies used
- Python 3
- Scikit-learn
- matplotlib
- Pandas
- RegEx

## Data Source
- Quandl
- Yahoo Finance

## Major Features
- Backtesting strategy after a train and validation 
- Comparing return to the market average

## Machine Learning Framework

The code followed the framework for almost all machine learning processes. 
1. Data Collection: the data was pulled using a scraper that would use regular expressions to strip data from yahoo html files, the amazing Quandl API helped fill in the rest of the data

2. Data Preparation: Using the SKLearn library on python, the data was randomized and split int training and evaluation sets. An additional script was used to fill in missing values

3. Model: Linear Support Vector Classification

4. Train: 0 for underperforming stocks, 1 for outperforming stocks. A simple function call from the SKLearn library 

5. Evaluate: Compares the return of the stocks chosen to the return of the S&P 500.

6. Parameter Tuning: More of an artform, test size was manipulated, features were added and removed. Feature weighting was a little hard for my first Machine learning algorithm.

7. Predict and Test: Used a very basic backtester to measure the return if the algorithm was used. On average the predictions were 56% correct. This may not seem bad but it's unknown. The problem is if you are right 56% of the time, if the losses from the other 44% outweigh the gains made, then the algorithm was unsuccessful. Overall, the algo outperformed the S&P 500 by 9% which is actually pretty good (and probably unrealistic)!


## Future Implementation 
- Automate data pull to update weekly 
- Use techincal signals 
- A more in-depth backtester 
- Future week prediction 
