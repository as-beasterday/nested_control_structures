'''
programmer: me
program: double for loop
'''

for i in range(5):
    print(i)
    for j in range(20):
        print(j)

print("Done!")

print("\n")

'''
programmer: me
program: average test score
'''

num_people = int(input("How many people are taking the test?  "))
test_per_person = int(input("How many tests are being averaged?  "))

for i in range(num_people):
    name = input("What is your name?  ")
    sum = 0
    for j in range(test_per_person):
        score = int(input("What is the score on your test?  "))
        sum += score
    average = float(sum) / test_per_person
    print("Average for " + name + ": " + str(round(average, 2)))

'''
programmer: me
program: for loop + while loop
'''