import requests

from text_processing import get_text, text_to_file, split_text

# url = 'https://api.openalex.org/works/W2741809807'

path = './data/abstract_input/abstracts.txt'
windoof_path = '.\\data\\abstract_input\\abstracts.txt'

url = 'https://api.openalex.org/works?filter=language:en,abstract.search:Transcription%20factors%20in%20E.%20coli' 

response = requests.get(url)

if response.status_code == 200:
    # Request was successful
    data = response.json()  # If the response is in JSON format
    print(len(data['results']))
    for key, value in data.items():
            
            if key == 'results':
                 for result in value:

                        abstract = result["abstract_inverted_index"]

                        if abstract != None:
                            text = get_text(abstract) + "\n"
                            text_to_file(path, text)

else:
    # Request failed
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes
