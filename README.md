# Python 102

Practice exercises and solutions from the **Python 102** course by **Satr Academy**.

## Topics

- Dates and Numbers
- Advanced Sequences
- Advanced Strings
- Advanced Lists
- Advanced Functions
- Final Project


# Python102 Final Project – People Age Analyzer

## Overview

This project demonstrates working with Python dates, numbers, sequences, and functions by building a program that processes an unlimited number of people and their birth dates.

## Learning Objectives

By the end of this project, you will be able to:

* Work with dates using Python.
* Perform numerical calculations.
* Use advanced sequence data types and their methods.
* Apply Python functions in more advanced scenarios.

## Requirements

Build a program that accepts an unlimited number of people along with their birth dates.

For each person, the program should:

* Calculate the current age based on the reference date **2021-01-01**.
* Display the day of the week on which the person was born.
* Validate the entered date (day, month, and year).
* Reject invalid dates (such as month 14, negative values, non-numeric input, or impossible calendar dates) and display:

  ```
  Invalid date: <Person Name>
  ```

After processing all valid entries, the program should:

* Display the oldest person.
* Display the youngest person.
* Display the total number of people entered.
* If only one person is entered, print:

  ```
  There is no oldest or youngest person.
  ```

## Example Input

```text
Khalid, 1-2-1989
Nouf, 2-9-2004
Ali, 9-12-2009
```

## Example Output

```text
Khalid is 31 years old and was born on Saturday
Nouf is 16 years old and was born on Thursday
Ali is 11 years old and was born on Wednesday

The oldest one is Khalid
The youngest one is Ali
Total People: 3
```

> **Note:** All age calculations are based on the reference date **2021-01-01**. Birth dates follow the format **dd-mm-yyyy**.

## Bonus Tasks

* Sort and display people from oldest to youngest.
* Print the original input in reverse order.
* Display the names of people who were born on Sunday.

