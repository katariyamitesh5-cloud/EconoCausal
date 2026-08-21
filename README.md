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

## 🧠 Key Concept

### Treatment

The treatment variable is:

```text
Discount