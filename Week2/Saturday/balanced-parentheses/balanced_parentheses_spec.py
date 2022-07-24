from balanced_parentheses import balance

print((balance("()")) == "()")
print((balance("a(b)c)")) == "a(b)c")
print((balance("(a)(bdd)c)")) == "(a)(bdd)c")
print((balance("a(dbvb)c)")) == "a(dbvb)c")
print((balance("a(b)(c)())")) == "a(b)(c)()")
print((balance(")(")) == "")
print((balance("(((((")) == "")
print((balance(")(())(")) == "(())")
print((balance(")())(()()(")) == "()()()")
print((balance("(()()(")) == "()()")