# Balanced Parentheses

### Write an algorithm that takes in a string and returns a string with balanced parentheses only. The string will contain letters, numbers, and parentheses only.

```python
balance("()") # should return "()"
balance("a(b)c)") # should return "a(b)c"
balance("(a)(bdd)c)") # should return "(a)(bdd)c"
balance("a(dbvb)c)") # should return "a(dbvb)c"
balance("a(b)(c)())") # should return "a(b)(c)()"
balance(")(") # should return ""
balance("(((((") # should return ""
balance(")(())(") # should return "(())"
balance("(()()(") # should return "()()"
balance(")())(()()(") # should return "()()()"
```

### Challenge - Nested Parentheses
```python
balance(")(())(")) # should return "(())"
```
