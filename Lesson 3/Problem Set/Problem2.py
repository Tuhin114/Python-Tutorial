letter = ''' Dear <|Name|>,
             You are selected!
             <|Date|> '''

print(letter.replace("<|Name|>", "Tuhin Poddar").replace("<|Date|>", "01-01-2023")) #chaining of replace