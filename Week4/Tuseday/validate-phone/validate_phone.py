import re

phone_regex = r"[\d]{3}-[\d]{3}-[\d]{4}"

# Does a string contain a phone number?
def has_phone_number(input_string):
    return True if re.findall(phone_regex, input_string) else False

# Get a phone number back from a string
def get_phone_number(input_string):
    return re.search(phone_regex, input_string).group() if re.search(phone_regex, input_string) else None

# Gets and returns all phone numbers from an inputted string
def get_all_phone_numbers(input_string):
    return re.findall(phone_regex, input_string)


# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: xxx-xxx-1234
def hide_phone_numbers(input_string):
    return re.sub("[\d]{3}-", 'XXX-', input_string)


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    results = []
    split_nums = input_string.split(',')
    for num in split_nums:
        clean = re.sub("\D", '', num)
        results.append(clean[:3] + '-' + clean[3:6] + '-' + clean[6:])
    return ', '.join(results)

# def format_phone_number(input_string):
#     return re.sub(r'\(?(\d{3})\)?.?(\d{3}).?(\d{4})', r'\1-\2-\3', input_string)
