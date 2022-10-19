
# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.



def migratoryBirds(arr):
    max = 0
    id = 0
    for i in range(1,6):
        print(arr.count(i))
        total = arr.count(i)
        if total > max:
            max = total
            id = i
    return id



print(migratoryBirds([1,4,4,5,3,3]))
print(migratoryBirds([3,1,3,3,4,5])) 
print(migratoryBirds([2,2,2,6,6]))