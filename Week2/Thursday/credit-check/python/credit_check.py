def check_credit(card_num):
    result_sum = []
    for i in range(len(card_num) - 1, -1, -1):
        
        if i % 2 == 0 :
            two_times = str(int(card_num[i]) * 2)
            if int(two_times) > 9:
                result_sum.append(int(two_times[0]) + int(two_times[1]))
            else: result_sum.append(int(two_times))
        else:
            result_sum.append(int(card_num[i]))
    result_sum = sum(result_sum)
    if result_sum % 10 == 0:
        return "The number is valid!"
    else: return "The number is invalid!"

# print(check_credit('5541808923795240'))