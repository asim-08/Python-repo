letter = '''Dear <|Name|>
        Your are selected!
        <|Date|>
'''
print(letter.replace("<|Name|>" , "Asim").replace("<|Date|>" , "25 august 2050"))