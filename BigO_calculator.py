from bigO import BigO
from bigO import algorithm

lib = BigO()

words = ["liver", "dog", "hello", "desserts", "evil", "test", "god", "stressed", "racecar", "palindromes", "semordnilap", "abcd", "live"]

def semordnilap(words):
    sorted_words = []
    index_pairs  = []
    result =[]
    for i in range (len(words)):
        sorted_word = (sorted(words[i]))
        if sorted_word in sorted_words:
            first_index = (sorted_words.index(sorted_word))
            index_pairs.append([first_index,i])
            sorted_words.append(sorted_word)
        else:
            sorted_words.append(sorted_word)
    for indx_list in index_pairs:
        pair = []
        for i in range(len(indx_list)):
            pair.append(words[indx_list[i]])
        result.append(pair)
    
    return result

lib.test_all(semordnilap(words))

