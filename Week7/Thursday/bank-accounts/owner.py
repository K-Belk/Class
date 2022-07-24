import csv


class Owner:

    def __init__(self, first_name, last_name, street_address, city, state, member_id):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.member_id = member_id
        self.account_numbers = member_id * 1000
        self.accounts = {}

    @classmethod
    def all_members(cls):
        mem = {}
        with open('support/owners.csv') as csvfile:
            members = csv.reader(csvfile)
            for m in members:
                hold = {}
                hold['member_id'] = int(m[0])
                hold['last_name'] = m[1]
                hold['first_name'] = m[2]
                hold['street_address'] = m[3]
                hold['city'] = m[4]
                hold['state'] = m[5]
                mem[int(m[0])] = Owner(**hold)
        return mem

    @classmethod
    def find(cls, member_id):
        with open('support/owners.csv') as csvfile:
            members = csv.reader(csvfile)
            for id in members:
                if id[0] == str(member_id):
                    found = {}
                    found['member_id'] = int(id[0])
                    found['last_name'] = id[1]
                    found['first_name'] = id[2]
                    found['street_address'] = id[3]
                    found['city'] = id[4]
                    found['state'] = id[5]
                    return found
            return "No account found"