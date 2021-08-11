def fifty_thirty_twenty(ati):
    r = (ati/100)
    print(r)
    return {
           "Needs": int(r*50),
           "Wants": int(r*30),
           "Savings": int(r*20)
    }

a = fifty_thirty_twenty(13450)
print(a)