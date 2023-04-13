import requests

site = "demo.bima-mo.com"

url = "https://{}/token".format(site)

payload = 'username=?&password=?'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

token_response = requests.request("POST", url, headers=headers, data=payload)

token_data = token_response.json()
access_token = token_data["access_token"]

print(access_token)

headers = {'Authorization': 'Bearer {}'.format(access_token)}
payload = {}

# Product Tests
benefit_id = 340
product_url = "https://{}/product/{}".format(site, benefit_id)
product_response = requests.request("GET", product_url, headers=headers, data=payload)
product_data = product_response.json()
print(product_data["description"])

# Policy Type Tests
policy_id = 1120
policy_type_url = "https://{}/policy/type/{}".format(site, policy_id)
policy_type_response = requests.request("GET", policy_type_url, headers=headers, data=payload)
policy_type_data = policy_type_response.json()
print(policy_type_data["policyTypeDescription"])

# Codeset Tests
codeset = "Benefit Type"
codeset_url = "https://{}/codesets/{}".format(site, codeset)
codeset_response = requests.request("GET", codeset_url, headers=headers, data=payload)
codeset_data = codeset_response.json()
print("number of codeset values:{}".format(codeset_data["noOfCodeSetValues"]))

print("--------------------------------------------")

list_of_entities = [117472, 117565, 117488, 1371993, 1371996, 12598, 13206, 13207, 123456]

for entity in list_of_entities:

    policy_url = "https://{}/policy/{}?getBenefits=true&getDependants=false&getBusinessSource=false".format(site, entity)
    entity_url = "https://{}/entity/{}".format(site, entity)
    claims_url = "https://{}/claims/{}".format(site, entity)

    # Entity Tests
    entity_response = requests.request("GET", entity_url, headers=headers, data=payload)
    entity_data = entity_response.json()
    print("{}".format(entity_data["name"]))

    # Policy Tests
    policy_response = requests.request("GET", policy_url, headers=headers, data=payload)
    policy_data = policy_response.json()

    if not policy_data["benefits"] is None:
        for benefit in policy_data["benefits"]:
            print("-{}".format(benefit["benefitName"]))

    # Claims Tests
    claims_response = requests.request("GET", claims_url, headers=headers, data=payload)
    claims_data = claims_response.json()
    print("-{}".format("number of claims:{}".format(claims_data["noOfClaims"])))









