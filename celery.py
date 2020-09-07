def salary(years, kids, day_mis):
    min_wg = 400
    year_pay = 20 * years
    kid_pay = 30 * kids
    total = min_wg + year_pay + kid_pay
    output = ""
    if not day_mis:
        # total = total + 100
        total += 100
        output += " + 100$ for not missing a day at work"
        # output is now " + 100$ for not missing a day at work"
    output = f"The total amount is {total}$. {min_wg}$ minimum wage + {year_pay}$ for {years} years experience + {kid_pay}$ for {kids} kids" + output
    print(output)

salary(15, 2, False)
