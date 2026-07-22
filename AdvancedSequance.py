# indexing  
# a,b,c = 0,1,2
# 0 = a 
# 1 = b  
# 2 = c

alphabet = 'abcdefjiklmnopqrstuvwxyz'
print(alphabet[0])

#slicing

text_string = "learing python from satr " #23
list_a = [1,1,1,2,3,4,5]
tuple_a = (1,1,2,2,3,4,5)
text1 = "    A8OW   "

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# l e a r i n g - p y  t  h  o  n  -  f  r  o  m  -  s  a  t  r

print(text_string[8:14]) # From To 
print(text_string[:14]) # The End
print(text_string[8:]) # from To End


print('----Find python Index----')   # Index Function
print(text_string.index('python'))

print('----How Many----')  # Length Function 
print(len(text_string))        
print(len(list_a)) 
print(len(tuple_a))     

print("----Count----")   # Count Function
print(text_string.count('o'))
print(list_a.count(1))
print(tuple_a.count(2))

print("----checking----")   # in Opearator
print('learing' in text_string)
print('satr' not in text_string) 
print('Satr'  in text_string) # S s <-- sensitive case
print(1 in list_a)
print(7 in tuple_a)


print("------checking the string ---------")   # in Opearator

print(text1.isalnum()) ## isalnum - checking if there any spaces or any symbol  return true/false
print(text1.isdigit()) ## isdigit - all numbers or not
print(text1.isalpha()) ## isalpha - all letters
print(text1.isidentifier()) ## isidentfier checking 1 - start with letter or( _ ) 2 - only nums or letters  

print("---- strip the string ----")
print(text1.strip())  ## strip() removes the spaces from the string ---> (       python       ) ---> (python)
print(text1.rstrip())

print("---- replace ----")
numbers = '1\n2\n3\n4\n5\n6'
print(numbers.replace('\n', ' , ')) ## from \n  to , but it does't change the real value 
print(numbers)


## lower change the string to small letter's --> text1.lower() 
## upper change the string to big letter's --> text1.upper()
## swapcase chenges the upper letters to lower letters and lower to upper --> text1.swapcase()
## title changes every first letter to an upper letter -->text1.title()



      ##             filter function
  
ages = [12,32,54,14,28,26,17,18] # two ways to remove under 18 years old
adults = [] # needed for the first way 

# basic way ( long way )
def filterd_teen1(ages):     # input a array
    for age in ages:       # genrate a vairble for the loop
     if age  >= 18 :
        adults.append(age) #input the genrate value into the new array
    return adults

print(filterd_teen1(ages))  # did't need to use a filter or a list 

# better way 
def filterd_teen2(age):
   return age >=18

print(list(filter(filterd_teen2 , ages))) # you should use filter and list function 

##                     map function similar to filter function


numbers = [1,10,2,3,4,5,6,7,8,9]

## basic way ( longer way )
def square1(numbers):
   sq_numbers = [] ## new array to put the squared nums in it

   for num in numbers: # for each value in the input array
      sq_numbers.append(num**2) # will squared 

   return sq_numbers  ## return our new array 
print(square1(numbers))

## better way using the map function
def square2(num):
   return num**2

print(list(map(square2 , numbers))) 

## third way 

sq_numbers = [num**2 for num in numbers if num >= 0 and num % 2 == 0 ]  ## we call it list comprehension
sq_numbers.sort()
print(sq_numbers)

# sort function  -->number.sort()
# --
# reverse function --> number.reverse() 


