document = "The quick brown fox jumps over the lazy dog. The quick brown fox is quite fast and the dog jumps again."
punctuations = '?.!<>/@#$%^&*()-+=;:|'
def distance_between_mid_points(document:str, word1:str , word2:str) -> float:
    document = ' ' + document.lower() + ' '
    
    for punctuation in punctuations:
        if punctuation in document:
            document = document.replace(punctuation,' ')

    word1 = word1.lower()
    word2 = word2.lower()

    loc1_idx = []
    loc2_idx = []
    for idx,val in enumerate(document):
        if document[idx:idx+len(word1)+2]==' '+ word1 +' ':
            loc1_idx.append(idx+len(word1)/2)
        if document[idx:idx+len(word2)+2]==' '+ word2 +' ':
            loc2_idx.append(idx+len(word2)/2)

    if not loc1_idx:
        return f'{word1} not found'

    if not loc2_idx:
        return f'{word2} not found'

    shortest_dist = len(document)
    for x in loc1_idx:
        for y in loc2_idx:
            if abs(x-y)<shortest_dist:
                shortest_dist = abs(x-y)
    return shortest_dist

test_cases = [
    ('quick' , 'brown'),
    ('the' , 'over'),
    ('jumps' , 'again'),
    ('fox' , 'dog'),
    ('lazy' , 'quite'),
    ('lazy' , 'dog'),
]

for test in test_cases:
    print(distance_between_mid_points(document, test[0] , test[1]))