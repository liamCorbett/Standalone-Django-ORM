import csv, os
import manage
from dbpush.models import Person


def save_new_person_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        row = 0
        for person in reader:
            if row==0:
                headers = person
                row += 1
                print(headers)
            else:
                # create a dictionary of person details
                new_person_details = {}
                for i in range(len(headers)):
                    new_person_details[headers[i]] = person[i]

                # create an instance of person model
                new_person = Person()
                new_person.__dict__.update(new_person_details)
                new_person.save()
                row += 1

    os.rename(file_path, file_path + 'done')

if __name__ == "__main__":
    save_new_person_from_csv('people.csv') 