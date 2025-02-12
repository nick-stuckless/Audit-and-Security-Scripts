import pandas
import ipinfo

# IPInfo auth token
token="843195af81f114"
# CSV path, Create a datafram with pandas to read CSV
csv_file = "C:\\Users\\nicks\\Downloads\\vernlog.csv"  
dataframe = pandas.read_csv(csv_file)

# Collecting country info from IP using IPInfo
def get_country_code(ip):
    try:
        handler = ipinfo.getHandler(token)
        data = handler.getDetails(ip)
        return data.country
    # Error handling
    except:
        return print("Not gunna happen")

# Dataframe key "country" is added and given the value returned by the get_country_code function. Function takes the client address as its argument
dataframe["country"] = dataframe["clientaddr"].apply(get_country_code)

# Converts the output to a JSON list and formats it into records with an indentation as requested
json_list = dataframe.to_json(orient="records", indent=4)

print(json_list)
