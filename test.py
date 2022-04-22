
import csv


path = "credentials.csv"
file = open(path, "a", newline="")
writer = csv.writer(file)
credentialsTuple = ("Instagram", "Moses", 123)
csv.writer(file)
writer.writerow(credentialsTuple)