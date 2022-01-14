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
