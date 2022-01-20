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
    pass
#split it into a list
