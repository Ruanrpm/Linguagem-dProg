import bakaa

while True:
    text = input('bakaa>>') 
    tokens = bakaa.run(text)
    print(tokens)