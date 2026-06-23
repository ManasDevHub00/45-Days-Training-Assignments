# Assignment 5: NumPy, Pandas & Data Visualization

**Name:** Manas Sharma

**Date:** 23/06/2026

**Python Version:** 3.11.5

**Libraries Used:** NumPy, Pandas, Matplotlib, Seaborn

---

# Section A – NumPy

### 1.

Create a 1D NumPy array of 20 random integers between 1 and 100. Find the minimum, maximum, mean, and standard deviation without using Python built-in functions — use only NumPy aggregation functions.

### 2.

Create a 4×4 matrix using NumPy. Perform the following operations:

* Extract the diagonal elements
* Replace all even numbers with 0
* Find the index of the maximum value using `argmax()`

### 3.

Write a program to create two 3×3 NumPy arrays and perform:

* Element-wise addition
* Element-wise subtraction
* Matrix multiplication

Display results with proper labels.

### 4.

Using `np.linspace()`, `np.zeros()`, and `np.ones()`, create three different arrays and stack them vertically using `np.vstack()`. Display the final stacked array.

---

# Section B – Pandas

### 5.

Create a DataFrame of at least 10 students with columns:

* Name
* Age
* Marks
* City

Perform the following:

Create a DataFrame with some missing values intentionally placed in the Marks and City columns.

Perform the following:

* Identify missing values using `isnull()`
* Fill missing marks with the column mean using `fillna()`
* Drop rows where City is missing using `dropna()`

### 7.

Read a CSV file (you may create it manually) containing product sales data with columns:

* Product
* Category
* Sales
* Region

Perform:

* Group by Category and calculate total Sales using `groupby()` and `agg()`
* Find the top 3 products by sales using `sort_values()` and `head()`

### 8.

Merge two DataFrames:

**DataFrame 1**

* StudentID
* Name
* Department

**DataFrame 2**

* StudentID
* Marks
* Grade

Merge on `StudentID` and display students who scored Grade 'A'.

---

# Section C – Data Visualization

### 9.

Using Matplotlib, create the following plots from a student marks dataset (create the dataset yourself):

* A line plot showing marks trend across 5 subjects
* A bar chart comparing marks of 5 students

Add:

* Proper title
* X-axis label
* Y-axis label
* Legend
* Grid

to both plots.

### 10.

Using Pandas built-in plotting, load or create a dataset with at least 4 numeric columns.

Create:

* A histogram for marks distribution
* A box plot to visualize spread and outliers
* A pie chart showing category-wise percentage

### 11.

Using Seaborn, create a dataset of at least 50 records with columns:

* Age
* Salary
* Department
* Experience

Plot:

* A scatter plot of Age vs Salary with hue as Department
* A heatmap showing correlation between numeric columns
* A bar plot showing average Salary per Department

### 12.

Create a subplot layout of 2 rows × 2 columns using Matplotlib containing:

* Line Plot
* Scatter Plot
* Bar Chart
* Histogram

All using the same dataset.

Add a main title using `suptitle()`.

---

# Conclusion

This assignment covers the fundamentals of NumPy, Pandas, Matplotlib, and Seaborn, including array operations, DataFrame manipulation, handling missing values, CSV processing, statistical analysis, and data visualization techniques.
