2.2 
For the relationship between maternal inherited de novo mutations and the mother's age: 

Based on the least squares analysis, the mother's age cofficient in the regression equation is 0.3776, which represents that the mean increase of maternal inherited de novo mutation(dnm) in her offspring for every additional one year old in mother's age. In other words, if the mother ages one year old, the average number of the dnm that her offspring could potentially inherit is 0.3776.  

The mother's age cofficient is postitive, which also matches the overall increasing (but not obvious) distribution trend of the dnm in my 2.1 plot as the mother age progresses. 

With 95% confidence, the p-value is 6.878208e-24, indicating that the relathinship between the mother's age and the number of the maternal inherited dnms is not statistically significant. 


2.3 
For the relationship between paternal inherited de novo mutations and the father's age: 

Based on the least squares analysis, the father's age cofficient in the regression equation is 1.3538, which represents that the mean increase of paternal inherited de novo mutation(dnm) in his offspring for every additional one year old in father's age. In other words, if the father ages one year old, the average number of the dnm that his offspring could potentially inherit is 1.3538.  

The father's age cofficient is postitive, which also matches the overall increasing distribution (more obvious than maternal) trend of the dnm in my 2.1 plot as the father age progresses. 

With 95% confidence, the p-value is 1.552294e-84, indicating that the relathinship between the father's age and the number of the paternal inherited dnms is not statistically significant. 

2.4 
Based on the 2.3 least squares analysis, we could formulate the equation to predict paternal inherited dnm of his offspring using the father's age, which is : 

paternal_dnm = 10.3263 + 1.3538 * (father's age)

Plug in the father's age  = 50.5 

Then the predicted number of the paternal dnm that the proband could potential inherit is 78.6932


2.6

To test whether there is a significant difference between the number of maternally vs. paternally inherited DNMs per proband:

I would choose between groups t-test, the indepedent variable is gender (maternally vs. paternally), the dependent variable is the number of the DNMs. The null hypothesis is maternally and paternally inherited DNMs have the same average(expected) values. 

The test result: 
TtestResult(statistic=53.40356528726923, pvalue=2.198603179308129e-264, df=790.0)

The conclusion they are significantly different. 





