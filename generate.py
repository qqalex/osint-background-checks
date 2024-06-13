# Generate valid background check (cyberbackgroundchecks.com) queries from name, address, phone, or email data
# OSINT Lookup / Automation Tool using CyberBackgroundChecks.com

# Alex (github.com/qqalex)
# June 13th 2024

def searchByName(fName=None, mName=None, lName=None, city=None, state=None):
    query = "https://www.cyberbackgroundchecks.com/people/"

    if lName == None:
        print("Error: Last name is required")
        return
    
    query += fName + mName + lName

    if state is not None:
        query += "/" + state
    elif city is not None:
        query += "/" + city
    
    return query


def searchByAddress(address, city, state):
    return f"https://www.cyberbackgroundchecks.com/address/{address}-{city}-{state}"

def searchByPhone(phoneNum):
    return f"https://www.cyberbackgroundchecks.com/phone/{phoneNum}"

def searchByEmail(email):
    return f"https://www.cyberbackgroundchecks.com/email/{email}"