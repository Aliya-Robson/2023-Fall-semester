print("")
# get the users address
house_number = int(input('enter house number: ' ))
str_name = input('  enter street address: \n' )
print("These are your neighbors' addresses on", str_name)
print("You are at the *\n")

# compute neighboring house numbers
house_across = house_number + 1
# Draw 1st row of housing.. house, house w/star, house
print("  _       _       _")
print(" / \\     / \\     / \\")
print("/   \\   / * \\   /   \\")
print("|___|   |___|   |___|")
print('', house_number-2,'   ',house_number,'   ',house_number+2)
print('')
# Draw 2nd row of housing.. house, house, house
print("  _       _       _")
print(" / \\     / \\     / \\")
print("/   \\   /   \\   /   \\")
print("|___|   |___|   |___|")
print('', house_number-1,'   ',house_number+1,'   ',house_number+3)
print("")





