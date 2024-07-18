# Credit Card Fraud Detection using Machine Learning

## Overview

This project aims to detect fraudulent credit card transactions using machine learning models. By analyzing transaction data, the system identifies patterns indicative of fraud, helping financial institutions prevent unauthorized activities and protect customers.

## Aims and Objectives

The primary aim of this project is to use machine learning to build a system that identifies fraud within the financial industry, specifically in retail transactions. The objectives are:
1. Reviewing existing literature on financial fraud detection to gain insights into various facets of the issue.
2. Addressing the challenges of detecting financial fraud using supervised machine learning methods on a readily accessible dataset.
3. Evaluating and contrasting various classification methodologies to determine the most effective approach for credit card fraud detection.

# Methodology

## Data Source

The data for this study was sourced from [Kaggle](https://www.kaggle.com). It contains credit card transactions across Europe for the year 2023. The dataset spans 31 variables and contains 568,630 records. However, many of the variables were anonymized due to the nature of their sensitivity i.e. some contained Personally Identifiable Information e.g addresses, ID number, jobs, age etc such variables are marked by random names denoted by V1 - V27. This dataset is publicly available and commonly used for academic and research purposes in fraud detection.

## Modelling

The following machine learning algorithms were used for fraud detection:
- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVC)

## Results

The models yielded the following results:

- **Logistic Regression**: Achieved an accuracy of 95%, demonstrating its effectiveness in binary classification tasks.
- **Decision Trees and Random Forest**: Both models achieved perfect accuracy scores, which may indicate overfitting on the training data.
- **Support Vector Machines (SVM)**: Showed strong performance with an accuracy of 98%, balancing complexity and generalization.

## Limitations of the Study

Anonymization of data columns hindered the ability to discern interactions and correlations between various features, affecting feature engineering efforts. Future research may benefit from alternative approaches to data anonymization.

## References

1. Pozzolo, D., Caelen, O., Johnson, R. A., & Bontempi, G. (2015). Calibrating Probability with Undersampling for Unbalanced Classification. 2015 IEEE Symposium Series on Computational Intelligence, Cape Town, South Africa.
2. Raghavan, P., & Gayar, N. E. (2020). Fraud Detection using Machine Learning and Deep Learning. In 2019 International Conference on Computational Intelligence and Knowledge Economy (ICCIKE). IEEE.
3. Mijwil, M. M., & Salem, I. E. (2020). Credit card fraud detection in payment using machine learning classifiers. Asian Journal of Computer and Information Systems.
4. Dhankhad, S., Mohammed, E., & Far, B. (2018). Supervised machine learning algorithms for credit card fraudulent transaction detection: a comparative study. In 2018 IEEE International Conference on Information Reuse and Integration (IRI). IEEE.



## Contacts Details

Feel free to reach out via [naomimitchual@yahoo.co.uk](naomimitchual@yahoo.co.uk)

Thank you