# Learning list functions

attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently.")
print("{}".format(potential_attendees))

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("Cc: " + cc_line)
to_line = to_line.split(", ")
print("Split: {}".format(to_line))
