# rates={  "USD": 1,
#     "AED": 3.6725,
#     "AFN": 86.0330,
#     "ALL": 97.5499,
#     "AMD": 386.9256,
#     "ANG": 1.7900,
#     "AOA": 824.0658,
#     "ARS": 254.7465,
#     "AUD": 1.5099,
#     "AWG": 1.7900,
#     "AZN": 1.6979,
#     "BAM": 1.7974,
#     "INR":82.0914
#     }

# amount=int(input("enter amount you want to exchange :>"))
# fromCurrencycode=input("enter sourse currency code :>")
# toCurrencycode=input("enter destination currency code :>")
# #equation=(amount/from_currency_code_rate)*to_currency_code_rate
# from_currency_code_rate=rates.get(fromCurrencycode)
# to_currency_code_rate=rates.get(toCurrencycode)
# result=(amount/from_currency_code_rate)*to_currency_code_rate
# print(result)




from json import load
with open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\currencyexchange\\db.json")as f:
    data=load(f)
rates=data.get("conversion_rates")
amount=int(input("enter amount : "))
from_cur_code=input("enter source currency code : ")
to_cur_code=input("enter destination currency code : ")

from_rate=rates.get(from_cur_code)
to_rate=rates.get(to_cur_code)
result=(amount/from_rate)*to_rate
print(result)