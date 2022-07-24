from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser


cheap = FreeUser('Kevin', 'kevin@email.com', '2/29/1904', 'K-Belk')
money = PremiumUser('Rich', 'rich@rich.com', '12/30/2000', 'Money_Money_Money')


print(cheap.new_post())
print(cheap.new_post())
print(cheap.new_post())
print(money.new_post())
print(money.new_post())