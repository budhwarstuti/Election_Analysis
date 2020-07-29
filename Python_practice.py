print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
if "El Paso" in counties:
    print("El PAso is present in counties!")
else:
    print("El PAso is not present in counties!")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso are in the list of counties")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso are in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)


temperature = int(input("What is the temperature today?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

x = 5
y = 5
if x == 3 or y == 5:
    print("True")
else:
    print("False")

x = 0
while x <=5:
    print (x)
    x = x + 1

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.values():
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key, value)

for county in counties_dict.items():
    print(county)

for county, voters in counties_dict.items():
    print(county, voters)

for countyValue, votersNum in counties_dict.items():
    print(countyValue + " county has "+ str(votersNum) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} regostered voters.")

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)


for counties_dict in voting_data:
    print(counties_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

    
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
msg_to_display = print(
    f" You received {my_votes:,} number of votes in the election."
    f" Total number of votes were {total_votes:,}."
    f" You received {my_votes / total_votes * 100:.2f} % of votes." 
)
print(msg_to_display)

