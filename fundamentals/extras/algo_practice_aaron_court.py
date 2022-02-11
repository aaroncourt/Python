from cgitb import strong


def count_positives(lst):
    pos_count = 0
    for x in lst:
        if x > 0:
            pos_count += 1
    lst[-1] = pos_count
    print(lst)

test = {
    
}
count_positives([-1,2,3,4]) #[-1,2,3,3]
count_positives([-1,-2,3,4]) #[-1,-2,3,2]


# define a function, it takes in a list and returns a new list.  If the number is even, replace that number with the sum of that number and the number befor it.



#using a function, take in a list of movies and return all the movies between 1990 and 2000
movie_info= [ 
    {
        'title':"ET",
        'year':1982,
        'genre':"Family"
    },
    {
        'title':"Princess Bride",
        'year':1986,
        'genre':"Adventure"
    },
    {
        'title':"Smoke Signals",
        'year':1998,
        'genre':"Comedy"
    },
    {
        'title':"Legends of the Fall",
        'year':1994,
        'genre':"Drama"
    },
    {
        'title':"A River Runs Through It",
        'year':1992,
        'genre':"Drama"
    },
    {
        'title':"Seven Years in Tibet",
        'year':1997,
        'genre':"Drama"
    }
]

def old_movies(lst):
    late_90s = []
    for i in lst:
        if movie_info[i]['year'] >= 1990 and movie_info[i]['year'] <= 2000:
            late_90s.append(movie_info[i]['title'])
    print(late_90s)

old_movies(movie_info)

# If given a large string (like a multi-line string or a .txt file) take that string and return a dictionary that has the words as the key, and the value is a count of how many times that word was used.  There is no difference in a word that is capital or lowercase.  It still counts for the same word. 
#  For example if given: , your function should return 
# {
#   this: 1,
#   is: 2,
#   a: 1,
#   test: 1
#   string: 1
#   it: 1,
#   not: 1,
#   very: 1,
#   long: 1
# }

test_string = "This is a test string.  It is not very long."

def word_count(data):
    count = {}

    punctuation = ["!", ".", "?", ",", "-", "\n"]
    for c in punctuation:
        if c in data:
            data = data.replace(c, " ")
    data = data.replace("  ", " ")
    print(data)

    for word in data.split(" "):
        if word != "" or word != " ":
            word = word.lower()
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    all_values = count.values()
    max_count = max(all_values)
    results = []
    for key in count:
        if count[key] == max_count:
            results.append(key)
    if len(results) == 0:
        return "No common word found"
    elif len(results) == 1:
        return results[0]

    else:
        answer = "These are the most common words: \n"
        for w in results:
            answer += f"{w}\n"

        return answer



# Find two numbers from the list that add to 2020 and return their product.

data = [1721,
        979,
        366,
        299,
        675,
        1456]

def two_nums(lst):
    ind1 = 0
    for i in lst:
        ind2 = 1
        while ind2 < len(lst):
            if lst[ind1] + lst[ind2] == 2020:
                product = lst[ind1] * lst[ind2]
                return print(f'The product is {product}')
            else:
                ind2 += 1
        if ind1 == (len(lst)-1):
            return print('No result!')
        else:
            ind1 += 1

two_nums(data)


#password checker. Can't be a weak password (ie password, opeansesame, LetMe!n, bill_for_president). Must contain a uppercase and lowercase letter, a number, and a special character (!@#$%^&*)

def strong_password(input):
    p_word = str(input)
    special = '!@#$%^&*'
    weak = ['password','opanseasame','LeMe!n','bill_for_president']
    if len(p_word) < 8:
        print ('The password is too short')
        return False
    if p_word.isalnum() == True:
        print('The password requires a special character')
        return False
    while x == True:
        for char in p_word:
            if char.isupper() == True:
                x = True
                continue
            if char.islower() == True:
                x = True
                continue
            if char.isnumeric() == True:
                x = True
                continue
            if special.find(char) != -1:
                x = True
                continue
            else:
                x = False
            

strong_password('password')