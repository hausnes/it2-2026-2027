# Initial distance between the two people in kilometers
initial_distance = 10

# Speeds of the two people in kilometers per hour
speed_person1 = 5
speed_person2 = 3

# Calculate the relative speed
relative_speed = speed_person1 + speed_person2

# Calculate the time it takes for them to meet
time_to_meet = initial_distance / relative_speed

# Extract hours and minutes
hours = int(time_to_meet)
minutes = (time_to_meet - hours) * 60

# Print the result
print(f"It takes {hours} hours and {int(minutes)} minutes for the two people to meet.")