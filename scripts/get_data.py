import requests
from text_procesing import get_text

# url = 'https://api.openalex.org/works/W2741809807'

url = 'https://api.openalex.org/works?sample=20'
response = requests.get(url)

print(response.status_code == 200)

if response.status_code == 200:
    # Request was successful
    data = response.json()  # If the response is in JSON format
    for key, value in data.items():
            
            if key == 'results':
                 print(value)
                 for result in value:

                        abstract = result["abstract_inverted_index"]

                        if abstract != None:
                            print(abstract)
                            print(get_text(abstract))

else:
    # Request failed
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes

