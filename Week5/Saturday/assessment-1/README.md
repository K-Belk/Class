# Assessment 1: Algorithms
- **Change Maker**

## Important Grading Information
- Make sure you read the [Assessment-1 Grading Rubric](https://docs.google.com/spreadsheets/d/1CjVoEPvswccsGTU5xc0WLaQ87Ql_mqGSeCEoZhSFyCM/edit?usp=sharing).
  - Algorithm Correctness (50%)
  - Code Design (25%)
  - Testing (25%)
- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade. 
  - *10% penalty*: If you complete and submit the retake after that. A retake for this assessment WILL NOT be accepted after this date.

## Rules / Process
* Fork repo to your personal Github and clone as usual but don't open a pull request until the time is up. Others will be able to see your answers.
* This test is fully open notes and open Google
* Work independently - don't consult with other students!
* 4 hour time limit

# Part 1: Optimal Change
You are writing a computer program for an electronic vending machine to give you the optimal change for an item's cost. Write a method called `optimal_change` that takes in two arguments: `item_cost` and `amount_paid`. The method will `print` a string with optimal change which follows the following convention:

```
optimal_change(62.13, 100)
> "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

optimal_change(31.51, 50)
> "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
```

Don't forget to account for plural denominations (i.e., quarters, dimes, pennies, bills) and punctuation (i.e., commas and the period at the end of a sentence) to delineate between different denominations. Some other things to note:
- This is **optimal** change. Obviously, you can give the change in pennies, but we're looking for the most optimal (least amount of) change possible.
- Only consider *common* monetary denominations (i.e. ignore any denomination larger than $100-bill, ignore $2-bills, half-dollars, etc...)
- Fully understand the data types of your input and output
- Don't forget about edge cases and special cases!
- Write at least 4-5 unit tests. Feel free to start with the two examples above. Make sure you test various parts of your algorithm (common cases, edge cases, special cases, etc...)

# Part 2: Extra Questions
Answer the following questions in `answers.txt`:
1. What is the difference between a local variable and an instance variable? What does `self.ATTRIBUTE` give you the ability to do that `ATTRIBUTE` does not?
2. List and describe all the `git` commands you commonly use to create a pull request
3. Can you describe what recursion is? What does every recursive method need?
