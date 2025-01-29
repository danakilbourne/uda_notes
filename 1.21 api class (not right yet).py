import json
import pandas as pd
import requests


pd.set_option('display.max_columns', None)

r = requests.get("http://api.zippopotam.us/us/il/redmon")

r.text

raw_text = r.text

json.loads(raw_text)

all_info = pd.read_json(raw_text)

pd.json_normalize(data=json.loads(raw_text), 
  record_path='places', 
  meta=['country abbreviation', 'state abbreviation'])



base_link = "https://api.agify.io/?name="

your_name = "Dana"

complete_link = base_link + your_name

complete_link


### exercise
av_k = "0CtBRPX7XVVxYRapC2eGP6mZ4Z6ZkXWuZCfgJt1E"

av_link = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={av_k}"


av_request = requests.get(av_link)

av_json = av_request.json()

series_data = av_json.get('Time Series (Daily)')

meta_data = av_json['Meta Data']

av_data = pd.DataFrame.from_dict(series_data, orient='index')

av_data['symbol'] = meta_data['2. Symbol']

av_data.reset_index(inplace = True)

av_data = av_data.rename(columns = {'index':'date'})

av_data


## these will always give you a json file
next_gen_data['leaders'][0]
next_gen_data['leaders'][0]['leader']

