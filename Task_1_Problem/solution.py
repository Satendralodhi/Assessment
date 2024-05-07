# Task 1: Problem 
# You are given a list of strings where each string represents a word. Write a Python function 
# group_anagrams(words) that eƯiciently groups the anagrams together and returns a list of lists where each 
# inner list contains words that are anagrams of each other. The order of inner lists doesn't matter, but the order 
# of words within each inner list should remain the same as they appear in the original list. 
# An anagram is a word or phrase formed by rearranging the letters of a diƯerent word or phrase, typically using 
# all the original letters exactly once. 
# Example: 
# >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] 
# Note: 
#  Consider edge cases such as an empty list or a list with no anagrams. 
# Submission: 
#  Implement the group_anagrams(words) function. 
#  Test your function with diƯerent inputs to ensure correctness and eƯiciency.



# **********************************************Solution******************************************


def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
            
        else:
            anagrams[sorted_word] = [word]
            
    return list(anagrams.values())

# Test the function
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# new test
print(group_anagrams(["eat", "tea", "tan", "ate", "tas", "sat","tes","set","yart","cart"]))