# def buy_ps4(hrs, income):
#     ps4 = 200
#     return int(hrs * income / ps4)

# ps4_bought = buy_ps4(h, i)

# def buy_samsung(hrs, income):
#     samsung = 900
#     return int(output / samsung)

# samsung_bought = buy_samsung(h, i)


# def buy_tv(hrs, income):
    # tv = 500
    # return int(hrs )

def buy_product(hrs, income, price):
    return int(hrs * income / price)

h = 40
i = 27

ps4_bought = buy_product(h, i, 200)
if ps4_bought == 1:
    single_ps4 = "PS4"
else:
    single_ps4 = "PS4s"

samsung_bought = buy_product(h, i, 900)
if samsung_bought == 1:
    single_samsung = "Samsung"
else:
    single_samsung = "Samsungs"

tv_bought = buy_product(h, i, 100000)
if tv_bought == 1:
    single_tv = "TV"
else:
    single_tv = "TVs"

gameskin_bought = buy_product(h, i, 9.99)
if gameskin_bought == 1:
    single_gameskin = "gameskin"
else:
    single_gameskin = "gameskins"
# test_bought = buy_product(h, i, "dumb") <--- will not work because you can't divide by a string

print(f"I can buy {ps4_bought} {single_ps4}, {samsung_bought} {single_samsung}, {tv_bought} {single_tv}, and {gameskin_bought} {single_gameskin}. ")