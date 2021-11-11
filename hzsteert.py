def get_cities(raw=False):
     response = requests.get(
         'https://hystreet.com/api/locations/',
         headers={'X-API-Token': "yajD4s3C6ebBpHjmtKirwDhS", #'ysm3dZnmKtE97cgTwT2sSbL9',
                  "Content-Type" : "application/vnd.hystreet.v1"},
     )
     data = response.json()
     for city in data:
         city["today_count"] = city["statistics"]["today_count"]
         del city["statistics"]
     if raw:
         return data
     else:
       return pd.DataFrame(data).rename(columns={"id":"ID"})
