''' Takes a csv file as input and scans it for "real" state ranks.
    Add the list of schools and subjects you're interested in
    to the relevant lists
'''

schools_of_interest = [
    "James Ruse",
    "Sydney Boys", "Sydney Girls",  # includes NSB and NSG
    "Hurlstone", "Fort Street",
    "Baulkham Hills", "Hornsby Girls",
    "Normanhurst Boys"
]

subjects_of_interest = [
    "Mathematics,",  # Use a comma in the name to exclude Mathematics General
    "Mathemstics Extension"  # Includes extension 1 and 2
    "Chemistry",
    "Physics",
    "Biology",
    # "English (Advanced)"
]
names_of_interest = schools_of_interest + subjects_of_interest


def interested(line):
    return any(s in line for s in names_of_interest)

input_file = open("top-achievers-in-course-2019.csv", "r")
output_file = open("state_ranks.csv", "a")

for line in input_file:
    if interested(line):
        output_file.write(line)
output_file.close()
