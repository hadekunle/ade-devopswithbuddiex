def distance_between_mid_points(document: str, word1: str, word2: str):
    input_file=document.split(" ")
    shortest= float('inf')
    # word_difference=0

    length1=0
    length2=0
    updated_word_count_length=0
    for word in input_file:
        if word == word1.lower() :#checks if the first word in the input is same as the input word 1  for first iteration
            length1=updated_word_count_length +len(word1)/2

        elif  word ==word2.lower() :
            length2=updated_word_count_length +len(word2)/2
            
        if length1 !=0 and length2 !=0:
            word_difference =abs(length1-length2)
            if word_difference < shortest:
                shortest=word_difference 
            
        
        updated_word_count_length =updated_word_count_length+ len(word)+1

    return shortest if  shortest != float('inf') else None


def main():
    document = "The quick brown fox jumps over the lazy dog. The quick brown fox is quite fast and the dog jumps again."


    # Test Case 1:
    print(distance_between_mid_points(document, 'Quick', 'fox') )
    # Expected Output: 6.0
 
    # Test Case 2:
    print(distance_between_mid_points(document, 'the', 'over'))
    # Expected Output: 26.5

    # Test Case 3:
    print(distance_between_mid_points(document, 'jumps', 'again'))
    # Expected Output: 41.0

    # Test Case 4:
    print(distance_between_mid_points(document, 'fox', 'dog'))
    # Expected Output: 37.5

    # Test Case 5:
    print(distance_between_mid_points(document, 'lazy', 'quite'))
    # Expected Output: 65.0
 
if __name__ =='__main__':
     main()