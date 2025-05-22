# def double_integer(i):
#     return i*2


# def hoop_count(n):
#     return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

# def get_drink_by_profession(param):
#     match param.lower():
#         case "jabroni":
#             return "Patron Tequila"
#         case "school counselor":
#             return "Anything with Alcohol"
#         case "programmer":
#             return "Hipster Craft Beer"
#         case "bike gang member":
#             return "Moonshine"
#         case "politician":
#             return "Your tax dollars"
#         case "rapper":
#             return "Cristal"
#         case _:
#             return "Beer"


# better solution
# d = {
#     "jabroni": "Patron Tequila",
#     "school counselor": "Anything with Alcohol",
#     "programmer": "Hipster Craft Beer",
#     "bike gang member": "Moonshine",
#     "politician": "Your tax dollars",
#     "rapper": "Cristal"
# }


# def get_drink_by_profession(s):
#     return d.get(s.lower(), "Beer")


###################################################
# 3
# Remove duplicates from list
# def distinct(seq):
#     seen = set()
#     return [x for x in seq if not (x in seen or seen.add(x))]

# print(distinct([1, 2, 1, 1, 3, 2]))

###################################################
# 4

# def multiple_of_index(arr):
#     return [num for index, num in enumerate(arr) if index == 0 and num == 0 or (index != 0 and num % index == 0)]


# # def multiple_of_index(arr):
# #     result = []  # Create an empty list to store the valid numbers

# #     # Loop through the list with index and value
# #     for index, num in enumerate(arr):
# #         if index == 0 and num == 0:  # Special case: Include 0 if it's at index 0
# #             result.append(num)
# #         elif index != 0 and num % index == 0:  # Check if number is a multiple of its index
# #             result.append(num)

# #     return result  # Return the final list of valid numbers


# print(multiple_of_index([22, -6, 32, 82, 9, 25]))

# ###################################################
# # 5

# def dna_to_rna(dna):
#     rna=[]
#     for char in dna:
#         if char=="T":
#             rna.append("U")
#         else:
#             rna.append(char)
#     return ''.join(rna)


# def dna_to_rna(dna):
#     return dna.replace("T", "U")


# print(dna_to_rna("GCAT"))


# ###################################################
# # 5

# def make_negative(n):
#     return -abs(n)

# print(make_negative(3))

# ###################################################
# # 6

# def combine_names(first, last):
#     return f'{first} {last}'

# print(combine_names("Steven", "Lake"))

# ###################################################
# # 7

# def find_difference(a:list,b:list)->int:
#     sum_a = 1
#     sum_b = 1
#     for i,j in zip(a,b):
#         sum_a *= i
#         sum_b *= j
#     return sum_a-sum_b

# def find_difference(a:list, b:list)->int:
#     return abs((a[0]*a[1]*a[2])-(b[0]*b[1]*b[2]))


# print(find_difference([2, 2, 4], [4, 5, 1]))

# ###################################################
# # 8 Jaden Casing Strings

# def to_jaden_case(s:str)->str:
#     arr_str = ' '.join(word.capitalize() for word in s.split())
#     return arr_str

# print(to_jaden_case("Hello my dear friends!"))

# ###################################################
# # 9 Find the middle element

# def gimme(triplet):
#    return triplet.index(sorted(triplet)[1])

# print(gimme([5,10,14]))


# ###################################################
# # 10 Volume of a Cuboid
# def get_volume_of_cuboid(length, width, height):
#     return length * width * height

# ###################################################
# # 11 Sum of angles


# def angle(n):
#     if n < 2:
#         return "Please enter number greater then 1"
#     return (n-2) * 180

# print(angle(3))

# ###################################################
# # 12 Fix string case

# def solve(s):
#     lower_count = sum(1 for char in s if char.islower())
#     return s.lower() if lower_count >= len(s)/2 else s.upper()

# def solve(s):
#     return s.upper() if sum(map(str.isupper,s))*2>len(s)else s.lower()


# print(solve("HellO"))

# ###################################################
# # 13 Sum of Minimums!

# def sum_of_minimums(numbers):
#     return sum(min(row) for row in numbers)

# def sum_of_minimums(matrix):
#     return sum(map(min, matrix))

# two_d_arr = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]
#  ]

# print(sum_of_minimums(two_d_arr))

# ###################################################
# # 14 is_palindrome

# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()

#     s = new_s
#     return s == s[::-1]


# def is_palindrome(s: str) -> bool:
#     filtered_chars = [char.lower() for char in s if char.isalnum()]
#     return filtered_chars == filtered_chars[::-1]


# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True

# ###################################################
# # 15 Surface Area and Volume of a Box

# def get_size(w, h, d):
#     area= 2*(w*h+h*d+d*w)
#     volume=w*h*d
#     return {'area':area, 'volume':volume}

# print(get_size(3,4,5))


# ###################################################
# # 16 Sort array by string length

# def sort_by_length(arr):
#     return sorted(arr, key=len)

# arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]
# print(sort_by_length(arr))

# ###################################################
# # 17 Alternate capitalization

# def capitalize(s: str) -> list[str]:
#     even = "".join([char.upper() if i % 2 == 0 else char.lower()
#                    for i, char in enumerate(s)])
#     odd = "".join([char.upper() if i % 2 != 0 else char.lower()
#                    for i, char in enumerate(s)])
#     return [even, odd]

# print(capitalize("abcdef"))

# ###################################################
# # 18 Sentence Smash

# def smash(words:list[str]) -> str:
#     return " ".join(words)

# words = ['hello', 'world', 'this', 'is', 'great']

# print(smash(words))

# ###################################################
# # 19 Is it even?

# def is_even(n: int) -> bool:
#     return n % 2 == 0

# ###################################################
# # 20 Is this a triangle?

# def is_triangle(a:int, b:int, c:int)->bool:
#     if a<=0 or b<=0 or c<=0:
#         return False

#     return a+b>c and a+c>b and b+c>a

# def is_triangle(a, b, c):
#     return all(x > 0 for x in (a, b, c)) and a+b > c and a+c > b and b+c > a

# print(is_triangle(0,2,3))


# ###################################################
# # 21 Maximum Length Difference

# def mxdiflg(a1: list[str], a2: list[str]) -> int:
#     if not a1 or not a2:
#         return -1
#     return max(
#         len(max(a1, key=len))-len(min(a2, key=len)),
#         len(max(a2, key=len))-len(min(a1, key=len))
#     )


# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
#       "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

# print(mxdiflg(a1, a2))

# ###################################################
# # 22  Formatting decimal places #0

# def two_decimal_places(n):
#     return round(n, 2)
#     # return '{0:.2f}'.format(n)


# print(two_decimal_places(5.234234))

# ###################################################
# # 23 L1: Set Alarm

# def set_alarm(employed:bool, vacation:bool)->bool:
#     return employed and not vacation

# print(set_alarm())

# ###################################################
# # 24 How old will I be in 2099?

# def calculate_age(year_of_birth, current_year):

#    if year_of_birth==current_year:
#       return "You were born this very year!"
#    elif year_of_birth>current_year:
#       return f'You will be born in {year_of_birth-current_year} {"year" if year_of_birth-current_year == 1 else "years" }.'
#    else:
#       return f'You are {current_year-year_of_birth} {"year" if current_year-year_of_birth == 1 else "years" } old.'


# def calculate_age(year_of_birth, current_year):
#     diff = current_year - year_of_birth
#     label = "year" if abs(diff) == 1 else "years"

#     match diff:
#         case 0:
#             return "You were born this very year!"
#         case _ if diff > 0:
#             return f"You are {diff} {label} old."
#         case _:
#             return f"You will be born in {abs(diff)} {label}."


# print(calculate_age(1989, 1990))


# ###################################################
# # 25 Deodorant Evaporator

# def evaporator(_, evap_per_day, threshold):
#     days = 0
#     current = 100
#     while current>threshold:
#         current-=current*(evap_per_day/100)
#         days+1
#     return days

# ###################################################
# # 26 Sorted? yes? no? how?

# def is_sorted_and_how(arr):
#     if arr == sorted(arr):
#         return 'ascending'
#     elif arr == sorted(arr)[::-1]:  # or sorted(arr, reverse=True)
#         return 'descending'
#     else:
#         return 'not sorted'

# ###################################################
# # 27 Sum of a sequence


# def sequence_sum(begin_number, end_number, step):
#     return sum(range(begin_number, end_number+1, step))

# print(sequence_sum(1,5,3))

# ###################################################
# # 28 Find out whether the shape is a cube

# def cube_checker(volume, side):
#     return 0<volume==side **3


# print(cube_checker(27,3))

# ###################################################
# # 29  Fibonacci

# from functools import lru_cache
# import os
# import pickle


# def fibonacci_with_while_and_result(limit):
#     state_file = 'fib_state.pkl'

#     # Try to resume state if exists
#     if os.path.exists(state_file):
#         with open(state_file, 'rb') as file:
#             state = pickle.load(file)
#         print("Resuming calculation with previous state:", state)
#     else:
#         print("Starting new calculation...")
#         state = {'current': 0, 'next': 1, 'results': []}

#     # Continue calculation
#     while state['current'] <= limit:
#         state['results'].append(state['current'])
#         new_value = state['current'] + state['next']
#         state['current'], state['next'] = state['next'], new_value

#     # Save final state
#     with open(state_file, 'wb') as file:
#         pickle.dump(state, file)

#     print("Calculation completed.")
#     print("Final calculation state:", state)

#     # Filter results up to limit
#     results = [num for num in state['results'] if num <= limit]
#     return results[-1] if results else None


# # Test
# print(fibonacci_with_while_and_result(5))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a + b
#     return b


# # Example
# print(fibonacci(5))  # Output: 5


# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# @lru_cache(maxsize=None)
# def fibonacci_memoized(n):
#     if n <= 1:
#         return n
#     return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a+b
#     return b

# ###################################################
# # 30 Sum of Multiples

# def sum_mul(n, m):
#     if n > 0 and m > 0:
#         result = 0
#         for num in range(n, m, n):
#             print(num)
#             result += num
#         return result
#     else:
#         return 'INVALID'


# def sum_mul(n, m):
#     if m > 0 and n > 0:
#         return sum(range(n, m, n))
#     else:
#         return 'INVALID'


# print(sum_mul(2, 2))


# ###################################################
# # 31 Hex to Decimal

# def hex_to_dec(s):
#     return int(s, 16)

# print('34')

# ###################################################
# # 32  Cat years, Dog years


# def human_years_cat_years_dog_years(human_years):
#     if human_years == 1:
#         cat_years = dog_years = 15
#     elif human_years == 2:
#         cat_years = dog_years = 24  # 15 + 9
#     else:
#         cat_years = 24 + (human_years - 2) * 4
#         dog_years = 24 + (human_years - 2) * 5
#     return [human_years, cat_years, dog_years]

# # Example test
# print(human_years_cat_years_dog_years(10))  # [10, 24 + 8*4 = 56, 24 + 8*5 = 64]

# ###################################################
# # 33 Sum of positive
# def positive_sum(arr):
#     return sum(num for num in arr if num>=0)

# print(positive_sum([1,-2,3,4,5]))

# ###################################################
# # 34 Calculate BMI

# def bmi(weight, height):
#     total = weight / (height*height)
#     if total<=18.5:
#         return "Underweight"
#     elif total<=25.0:
#         return "Normal"
#     elif total<=30.0:
#         return "Overweight"
#     else:
#         return "Obese"

# print(bmi(50, 1.80))

# ###################################################
# # 35 Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right


# def remove(st: str, n: int):
#     result = []
#     for char in st:
#         if char == "!" and n > 0:
#             n -= 1
#         result.append(char)
#     return "".join(result)


# def remove_1(s, n):
#     return s.replace("!", "", n)

# ###################################################
# # 36 Shortest Word

# def find_short(s):
#    return min(len(word) for word in s.split())

# print(find_short("bitcoin take over the world maybe who knows perhaps"))

# ###################################################
# # 37 USD => CNY
# def usdcny(usd):
#     return f"{usd*6.75:.2f} Chinese Yuan"

# print(usdcny(10))

# ###################################################
# # 38 Bouncing Balls

# def bouncing_ball(h, bounce, window):
#     # Check the three conditions
#     if h <= 0 or not (0 < bounce < 1) or window >= h:
#         return -1

#     count = 1  # Ball seen once on initial fall
#     height = h * bounce

#     # Count the times it passes the window on the way up and down
#     while height > window:
#         count += 2  # One up, one down
#         height *= bounce

#     return count

# ###################################################
# # 39 Sum of numbers from 0 to N

# def show_sequence(n):
#     if n<0:
#         return f"{n}<0"
#     if n==0:
#         return f"n==0"
    
#     series = "+".join(str(i) for i in range(n+1))
#     total = sum(range(n+1))
#     return f"{series}={total}"

# print(show_sequence(7))

# ###################################################
# # 40 Highest Scoring Word

# def high(x):
#     '''
#     1.first we need to split words into aray
#     2.then we create another function to calculate each word
#     3.we are using sum and iterate using ord()
#     4.return may using inbuilt function
#     '''
#     words=x.split()

#     def word_score(words):
#         return sum(ord(char)-ord('a')+1 for char in words)
    
#     return max(words, key=word_score)

# def high_2(x):
#     return max(x.split(), key=lambda words: sum(ord(char) - 96 for char in words))


# print(high("Hello my dear friends"))

# ###################################################
# # 41 Tortoise Racing

# def race(v1, v2, g):
#    if v1>=v2:
#       return None
   
#    time_in_hours = g/(v2-v1)

#    hours=int(time_in_hours)
#    minutes = int((time_in_hours*60)%60)
#    seconds=int((time_in_hours*3600)%60)
#    return[hours, minutes, seconds]
   
# print(race(720, 850, 70))

# ###################################################
# # 42 Remove First and Last Character Part Two

def array(string: str) -> str:
    parts = string.split(',')
    if len(parts) <= 2:
        return None
    return ' '.join(parts[1:-1])


print(array('1,2,3,4'))

   



