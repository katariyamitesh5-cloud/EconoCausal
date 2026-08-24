# EconoCausal

## Dynamic Pricing via Double Machine Learning

EconoCausal is a machine learning based dynamic pricing system that uses **Double Machine Learning (DML)** and causal inference to estimate the effect of discounts on customer sales.

Instead of only predicting sales, the system estimates the **causal effect of a discount** and uses that effect to recommend an appropriate discount level for each customer.

---

## 🚀 Project Overview

Traditional machine learning models mainly identify correlations.

For example:

> "Customers who receive discounts may have higher sales."

However, correlation does not tell us whether the discount actually caused the increase in sales.

EconoCausal addresses this problem using **causal inference and Double Machine Learning**.

The system:

1. Generates customer pricing data.
2. Preprocesses the dataset.
3. Builds a causal relationship model.
4. Estimates Individual Treatment Effects (ITE).
5. Generates customer-level pricing recommendations.
6. Provides recommendations through a FastAPI backend.
7. Displays analytics through a web dashboard.

---

## 🎯 Problem Statement

Businesses often provide discounts without knowing their actual causal impact on customer purchases.

Giving a large discount to every customer can reduce profit, while giving no discount to customers who need an incentive can reduce sales.

The goal of EconoCausal is to answer:

> **"What is the estimated effect of giving a discount to a particular customer?"**

The system then uses this estimated treatment effect to recommend a suitable discount strategy.

---

## 🧠 Key Concepts

### Treatment

The treatment variable is:

```text
Discount
The treatment represents the discount offered to a customer.

### Outcome

The outcome variable is:

Sales

The outcome represents customer sales after receiving a discount.

### Confounders

The model uses customer characteristics as confounders:

- Age
- Income
- Previous Purchases
- Gender

These variables may influence both the discount received and customer sales.

### Individual Treatment Effect (ITE)

The Individual Treatment Effect estimates how much the treatment is expected to affect a specific customer.

ITE = Expected Sales With Treatment - Expected Sales Without Treatment

A positive ITE suggests that offering a discount is expected to increase sales.

---

## Project Workflow

Customer Dataset
↓
Data Preprocessing
↓
Causal Model
↓
Double Machine Learning
↓
Treatment Effect Estimation
↓
Pricing Recommendation
↓
FastAPI Backend
↓
Analytics Dashboard

---

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- EconML
- DoWhy
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript
- Chart.js