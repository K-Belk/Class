# Character Count

For each unique character that appears in the input string, report the number of occurrences of that character in the input.  Report each character on its own line, in descending order based on the number of occurrences.  Each line should be formatted as follows:

```
<character>: <number of occurrences>
```

There is no defined order for reporting characters that have the same number of occurrences.  Such entries can appear in any order of your choosing in the output. Please also omit spaces when counting the characters.

Examples:

  **analyze("aaabbc")**
```python
{
  "a": 3,
  "b": 2,
  "c": 1,
}
```


  **analyze("an apple a day will keep the doctor away")**
```python
{
  "a": 5,
  "e": 4,
  "p": 3,
  "l": 3,
  "y": 2,
  "w": 2,
  "t": 2,
  "d": 2,
  "h": 1,
  "n": 1,
  "c": 1,
  "o": 1,
  "i": 1,
  "k": 1,
  "r": 1,
}
```
