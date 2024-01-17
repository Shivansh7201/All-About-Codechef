def phone_model(year):
    return 'K' + str(year)[-2:]

year = int(input())
print(phone_model(year))
