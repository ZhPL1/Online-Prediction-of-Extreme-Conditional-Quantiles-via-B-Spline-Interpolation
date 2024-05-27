# Online Prediction of Extreme Conditional Quantiles via B-Spline Interpolation
This project provides a demo implementation of EMI for the task of online extreme conditional quantile prediction, as described in our paper:

Zhengpin Li, Jian Wang, and Yanxi Hou (2024+). Online Prediction of Extreme Conditional Quantiles via B-Spline Interpolation. arXiv:2311.13825.

# Requirements

amplpy   ==     0.14.0

pandas   ==     2.0.3 

scipy    ==     1.10

numpy    ==     1.24.4 

To solve the bilevel programming, we apply AMPL, which is a modeling language for describing and solving mathematical programming problems. For more information on how to use AMPL, please refer to https://ampl.com/. 

# Run This Demo

We provide the MPEC.mod file describing our bilevel model for ampl solving. In addition, you need to store the observation data (X,Y) as Observation.dat, and you need to store the covariates X separately as Observation_X.mat. For the detail of data format, please refer to https://amplpy.ampl.com/en/latest/intro.html. 

The real data we use is S&P 500, which is open source.
