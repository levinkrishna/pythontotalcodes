"""mobiles=[
{"name":"galaxya10","brand":"samsung","price":24000,"network":"4g","colours":["red","black","blue"]},
{"name":14,"brand":"apple","price":140000,"network":"5g","colours"["red"]},
{"name":"note10","brand":"redmi","price":19000,"network":"5g","colours":["green"]},
{"name":"note3","brand":"realme","price":20000,"network":"4g","colours":[blue]"}

]"""


clothes=[
    {"material":"linen","name":"uspoloshirt","sizes":["s","m","l"],"brand":"uspolo","colours":["black","white","green"],price:5000},
    {"material":"cotton","name":"ottoshirt","sizes":["s","m","l"],"brand":"otto","colours":["black","white","green"],price:2500},
    {"material":"silk","name":"levis","sizes":["s","m","l"],"brand":"uspolo","colours":["black","white","yellow"],price:2000},
    {"material":"lycra","name":"peterengland","sizes":["s","m","l"],"brand":"uspolo","colours":["black","blue","red"],price:2000}
]

for c in clothes:
 print(c.get("name"))