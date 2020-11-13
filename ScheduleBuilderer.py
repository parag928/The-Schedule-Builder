#start time, end time and name of each class in order
startTime= [7.5,  8.0,  8.0,  10.5, 11.5,  12.0, 13.0, 14.0,  16.0, 17.0]
endTime = [8.5, 10.0,  9.25, 12.5, 12.75, 12.5, 16.0, 14.75, 17.0, 18.0]
description = [
    "Biology 101",
    "Chemistry 102",
    "Computer Science 341",
    "Philosophy 251",
    "American Studies 101",
    "Korean 101",
    "Chemistry 351",
    "Information Systems 247",
    "Computer Science 447",
    "Math 152"
  ]

for i in range(len(endTime)-2):
    for j in range(len(endTime)-2):
        #if the end time of each class in order greater than end time of the next class
        if endTime[j] > endTime[j+1]:
            temp = endTime[j]       #swaps the end times
            endTime[j] = endTime[j+1]
            endTime[j+1] = temp
            temp1 = startTime[j]    #swaps the start times
            startTime[j] = startTime[j + 1]
            startTime[j + 1] = temp1
            temp2 = description[j]  #swaps the name of the class too
            description[j] = description[j + 1]
            description[j + 1] = temp2

#creates a new dictionary and assigns start time and end times as the Class name's value
new_dict = {}
i = 0
for each in description:
    new_dict[each] = []
    new_dict[each].append(startTime[i])
    new_dict[each].append(endTime[i])
    i += 1


for key, value in new_dict.items():
    print(key, ": Start Time", value[0], "End Time", value[1])


#adds the start times and end times of each classes in order
new_list = []
for each in new_dict.values():
    new_list.append(each)


#if the start time of next class is after the the end time of previous class, add the class to the schedule
final_schedule = []
final_schedule.append(new_list[0])
for i in range(len(new_list)):
    if new_list[i][0] >= final_schedule[len(final_schedule)-1][1]:
        final_schedule.append(new_list[i])

#A function that returns Name, Start Time and End Time of the class that has been added to the final schedule
def getKeys(each):
    for key, value in new_dict.items():
        if value == each:
            return key, value

print("\n")
print("Available Classes that doesn't conflict with each other!")
for each in final_schedule:
    print(getKeys(each))