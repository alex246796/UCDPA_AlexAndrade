import requests
AverageWeeklyRent = requests.get('https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%22STATISTIC%22%5D,%22dimension%22:%7B%22STATISTIC%22:%7B%22category%22:%7B%22index%22:%5B%22E1021C13%22%5D%7D%7D%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22E1021%22%7D,%22version%22:%222.0%22%7D%7D')

print(AverageWeeklyRent.status_code)
print(AverageWeeklyRent.text)


AverageWeeklyRent2 = AverageWeeklyRent.json()
print(AverageWeeklyRent2)
print (type(AverageWeeklyRent2))

import pandas as pd

AverageWeeklyRent3 = pd.DataFrame (AverageWeeklyRent2)

print(AverageWeeklyRent3)


