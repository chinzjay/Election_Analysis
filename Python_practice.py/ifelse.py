#what is the score?
#score=int(input("What is the test score?"))
#Determine the grade
#if score>=90:
#    print("Your grade is A")
#elif score>=80:
#    print("Your grade is B")
#elif score>=70:
#     print("Your grade is C")
#elif score>=60:
#     print("Your grade is D")
#else:
#     print("Your grade is F")


counties=["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in county list")
else:
    print("El Paso is not in county list")

if "El Paso" in counties or "Arapahoe" in counties:
    print("A or E are in county list")
else:
    print("A and E not in county list")

for county in counties:
    print(county)

numbers=[0,1,2,3,4]
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_dict={"Arapahoe": 422829, "Denver": 463353, "Jefferson":432438}
for county in counties_dict.values():
    print(county)
for county in counties_dict:
    print(counties_dict[county])
for voters in counties_dict:
        print(voters)
for county,voters in counties_dict.items():
    print(county,voters)
for county, voters in counties_dict.items():
    print(county +" county has "+ str(voters) + " registered voters.")


voting_data=[{"county" : "Arapahoe", "registered voters": 422829},{"county": "Denver", "registered voters" : 463353}, {"county": "Jefferson", "registered voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
