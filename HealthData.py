def encode_education(degree):
    if degree == 'High School or GED' or degree =='Some highschool':      return 1
    elif degree =='Some Undergraduate' or degree == 'Completed Undergraduate': return 2
    elif degree =='Some\xa0Masters' or degree =='Completed Masters':    return 3
    elif degree =='Some Phd' or degree =='Completed Phd':return 4
    else:
        return 0

def encode_age(degree):
    if degree == '18-29' : return 1
    elif degree == '30-44' : return 2
    elif degree == '45-60' : return 3
    elif degree == '> 60' : return 4
    else:
        return 0

def encoder_gender(degree):
    if degree == 'Male' : return 1
    elif degree == "Female" : return 0

def encoder_income(degree):
    if degree == 'Prefer not to answer': return 0
    elif degree == '$0-$9,999' : return 1
    elif degree == '$10,000-$24,999' : return 2
    elif degree == '$25,000-$49,999': return 3
    elif degree == '$50,000-$74,999': return 4
    elif degree == '$75,000-$99,999': return 5
    elif degree == '$100,000-$124,999': return 6
    elif degree == '$125,000-$149,999': return 7
    elif degree == '$150,000-$174,999': return 8
    elif degree == '$175,000-$199,999': return 9
    elif degree == '$200,000+': return 10