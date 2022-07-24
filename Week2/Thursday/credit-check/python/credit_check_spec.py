# Can you translate this driver code to unit tests?

from credit_check import check_credit

print(check_credit('5541808923795240') == "The number is valid!")
print(check_credit("4024007136512380") == "The number is valid!")
print(check_credit("6011797668867828") == "The number is valid!")

print(check_credit("5541801923795240") == "The number is invalid!")
print(check_credit("4024007106512380") == "The number is invalid!")
print(check_credit("6011797668868728") == "The number is invalid!")
