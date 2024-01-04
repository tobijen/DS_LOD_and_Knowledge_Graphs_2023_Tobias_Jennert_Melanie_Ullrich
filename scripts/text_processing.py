from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter


def get_text(data: dict):
    '''
    The abstract text is packed in a dictionary and constists of the words as keys and the indexlist where the word occurs as the values.
    Example: 
    abstract_inverted_index: {
            "Abstract": [
                0
            ],
            "Thematic": [
                1
            ],
            "analysis": [
                2,
                39,
                110,
                128
            ],
            "is": [
                3
            ],
            "a": [
                4,
                81,
                112
            ]
        }

    The abstract text must be put together from that list. This is the purpose of this function.
    '''
    # get highest list value
    # loop over dict to get values in right order
    # get the length of the abstract needed for extract the right order of the text
    highest_values = []
    for words, index in data.items():
        highest_index = max(index)
        highest_values.append(highest_index)
    
    abstract_length = max(highest_values)

    # search in the list values for the right oder and add word if the order fits
    abstract_text = []
    for i in range(abstract_length + 1):
        for word, indexlist in data.items():
            if i in indexlist:
                abstract_text.append(word)
    
    return ' '.join(abstract_text)



def text_to_file(file_path, text, encoding='utf-8'):
    with open(file_path, 'a', encoding=encoding) as file:
        # Write content to the file
        file.write(text)



def split_text(file_path):
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
    )
    with open(file_path, encoding='utf-8') as f:
        text = f.read()
        text_splitted = text_splitter.split_text(text)
        print(text_splitted[:10])

