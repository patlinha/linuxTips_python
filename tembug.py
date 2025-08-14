def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas"""
    final_word = ""
    for letter in word:
        #import pdb;pdb.set_trace()
        #__import__("pdb").set_trace()
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
        
    return final_word

print(repete_vogal("banana"))