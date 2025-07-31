names = [
    "Bruno", 
    "Joao", 
    "Bernardo", 
    "Barbara", 
    "Brian",
    ]

# TODO: usar lambdas

def starts_with_b(text):
    #return text[0].lower() == "b"
    return text[0].startswith(("b","B"))

print(*list(filter(starts_with_b, names)))





"""
for name in names:
    if name.lower().startswith("b"):
        print(name)
"""