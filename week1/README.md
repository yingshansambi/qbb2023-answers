2.2 
For the relationship between maternal inherited de novo mutations and the mother's age: 

Based on the least squares analysis, the mother's age cofficient in the regression equation is 0.3776, which represents that the mean increase of maternal inherited de novo mutation(dnm) in her offspring for every additional one year old in mother's age. In other words, if the mother ages one year old, the average number of the dnm that her offspring could potentially inherit is 0.3776.  The intercept is 2.5040. This number represents the predicted dnm number when the mother age is zero (was born, for my understanding). 

The mother's age cofficient is postitive, which also matches the overall increasing (but not obvious) distribution trend of the dnm in my 2.1 plot as the mother age progresses. 

With 95% confidence, R-squared number in the alaysis is 0.228, that means that only 22.8% of the variation in maternal inherited dnm can be explained by the mother's age. For my understanding, correlation above 0.7 are considered strong, because if r= 0.7, then squared r = 0.49, meaning 50% of the variance in the response variable can be explained by the explanatory variable. In this case, 22.8% is still below 50%, meaning the correlation between maternal age and inherited dnm is not strong. In conclusion, this relationship is not significantly strong. 


2.3 
For the relationship between paternal inherited de novo mutations and the father's age: 

Based on the least squares analysis, the father's age cofficient in the regression equation is 1.3538, which represents that the mean increase of paternal inherited de novo mutation(dnm) in his offspring for every additional one year old in father's age. In other words, if the father ages one year old, the average number of the dnm that his offspring could potentially inherit is 1.3538.  The intercept is 10.3263. This number represents the predicted dnm number when the father age is zero (was born, for my understanding). 

The father's age cofficient is postitive, which also matches the overall increasing distribution (more obvious than maternal) trend of the dnm in my 2.1 plot as the father age progresses. 

With 95% confidence, R-squared number in the alaysis is 0.619, that means that 61.9% of the variation in paternal inherited dnm can be explained by the father's age. With same logic explained above, 61.9% is above 50%, meaning the correlation between paternal age and inherited dnm is strong. In conclusion, this relationship is significantly strong. 

2.4 
Based on the 2.3 least squares analysis, we could formulate the equation to predict paternal inherited dnm of his offspring using the father's age, which is : 

paternal_dnm = 10.3263 + 1.3538 * (father's age)

Plug in the father's age  = 50.5 

Then the predicted number of the paternal dnm that the proband could potential inherit is 78.6932


2.5 