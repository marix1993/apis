import requests
import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(pokemon_req.content)

# print(post_codes_req)

# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(post_codes_req.json())
# print(type(post_codes_req.content))
# print(type(post_codes_req.json()))

# post (post requests are very api dependant)

# json.dumps()(converts) -> method to turn python object (collection, variable,boolean, done) into a JSON string
# json_body = json.dumps(
#     {"postcodes": ["PR8 0SG",
#                    "m45 6GN",
#                    "EX165BL"]})
#
# # json.dump()(writes into the file)-> writes to a JSON file
#
# headers = {"Content-Type": "application/json"}
#
# post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)
#
# print(post_multi_req.json())


