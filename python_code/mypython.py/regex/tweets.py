tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
from re import *
rule="[@][a-zA-Z0-9_]+"
matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group())