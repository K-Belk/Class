

currency_amounts = {
    '$100 bill': 100,
    '$50 bill': 50,
    '$20 bill': 20,
    '$10 bill': 10,
    '$5 bill': 5,
    '$1 bill': 1,
    'quarter': .25,
    'dime': .10,
    'nickle': .05,
    'penny': .01
}


def optimal_change(item_cost, amount_paid):
    """
    Takes the cost of an item and the amount paid. Then returns a string with the cost amount paid and the amounts for change to return
    """

    item_cost = type_format(item_cost)
    amount_paid = type_format(amount_paid)
    change_amount = amount_paid - item_cost
    if change_amount == 0: 
        return f"There is no change for an item that costs ${item_cost} with an amount paid of ${amount_paid}."
    else:
        change = to_change(change_amount)
        string_response = change_to_string(change, item_cost, amount_paid)
    return string_response

def type_format(input):
    """
    Formats input to either a float or a int 
    """
    output = float(input)
    if output.is_integer():
        output = int(output)
    return output

def to_change(amount):
    """
    takes in an amount and returns a list with the change [quantity, name of value]
    """
    change = []
    for key in currency_amounts:
        value = currency_amounts[key]
        if amount >= value:
            quantity = int(amount // value)
            if key == 'penny' and quantity > 1:
                key = 'pennie'
            change.append([quantity, key])
            amount -= (quantity * value)
            amount = round(amount, 2)
    return change

def change_to_string(change, cost, paid):
    """
    Returns a string with the optimal change.
    Takes a change list [quantity, name of value], cost and paid and bulids a sentence with the change amounts
    """
    response = f"The optimal change for an item that costs ${cost} with an amount paid of ${paid} is "
    for index, amount in enumerate(change):
        quantity = amount[0]
        value = amount[1]
        if index == len(change) - 1:
            # if the there is only one form of change then no 'and' and end with a '.'
            if len(change) == 1:
                response += f"{quantity} {value}{'s' if quantity > 1 else ''}."
            else:
                # if at the end of the list of change. Then use 'and' and end with a '.'
                response += f"and {quantity} {value}{'s' if quantity > 1 else ''}."
        else:
            response += f"{quantity} {value}{'s' if quantity > 1 else ''}, "
    return response
