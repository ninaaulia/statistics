# statistics

excersise from udemy course : [The Data Science Course 2021: Complete Data Science Bootcamp](https://www.udemy.com/course/the-data-science-course-complete-data-science-bootcamp/)

## Confidence interval for difference of two means, dependent samples
weight lose (ibs)

![alt text](https://cdn.scribbr.com/wp-content/uploads/2020/01/t-test-formula-300x121.png)


### Background
The 365 team has developed a diet and an exercise program for losing weight. It seems that it works like a charm. However, you are interested in how much weight are you likely to lose.You have a sample of 10 people who have already completed the 12-week program.


### Data


| Subject| Weight before| Weight after|
| -------|:-------------:| ----------:|
|   1    |    228.58     |   204.74   |
|   2    |    244.01     |   223.95   |
|   3    |    262.46  	 |   232.94   |
|   4    |    224.32	   |   212.04   |
|   5	   |    202.14	   |   191.74	  |
|   6    |    246.98	   |   233.47   |
|   7    |	  195.86	   |   177.60	  |
|   8	   |    231.88	   |   213.85	  |
|   9	   |    243.32	   |   218.85	  |
|   10	 |    266.74	   |  236.86	  |



### step by step

+ task 1 : `Calculate the mean and standard deviation of the dataset`
              
              1. mean : -20.02458725746
              2. standard deviasi : 6.85889281086411
              
+ task 2 : `Determine the appropriate statistic to use`

              data has a normal distribution, sample < 30 so we'll using T distribution
              Ci 95%,t0.025


+ task 3 : `Calculate the 95% confidence interval`
            
             1. Ci low -24.9308027152603
             2. Ci hight -15.1183717996597
              

+ task 4 : `Interpret the result`
          
            *From 95% Ci, we can losing weight between -24.93 & -15.118 ibs (11 - 6 kg) after completing the 12-weeks program*






*ps : actually this exercise is using excel but I tried another way using python*
