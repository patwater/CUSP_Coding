import sys

db = {}
db_frequency = {}
db_agency = {}
''
categories = ['JobID'|'Agency'|'#OfPositions'|'Business Title'|'Civil Service Title'|'Salary Range From'|'Salary Range To'|'SalaryFrequency'|'Work Location'|'Division/Work Unit'|'JobDescription'|'MinimumQualRequirements'|'PreferredSkills'|'AdditionalInformation'|'PostingDate']
# does agency, #of positions, business title, etc, etc
# use find / replace to clean up 
# use to create a dictionary inside the dictionary

#do simalr as db_frequency for a db_agency

def clear():
  # TODO Complete with your code and remove print below.
  print 'clear'    


# Inserts a job offer into the database.
def insert(fieldValues):
  # TODO Complete with your code and remove print below.
  print 'insert ' + str(fieldValues)
  jobid = fieldValues[0]
  jobdetails = fieldValues[1:]

  
  if jobid in db:
    pass
  else:
    frequency = fieldValues[7]
    # agency = fieldValues[1]

    frequency_id = -1
    if frequency in db_frequency:
      frequency_id = db_frequency[frequency]
    else:
      db_frequency[frequency] = len(db_frequency)
      frequency_id = db_frequency[frequency]

    print frequency_id
    db[jobid] = []

    i = 0
    for details in jobdetails:
      db[jobid][i] = details

      if i == 7:
        db[jobid][i] = frequency_id
      i += 1



# Updates all job offers that attend the field_name=old_value pair.
def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    # TODO Complete with your code and remove print below.
    print 'update_all set ' + update_field_name + '=' + update_field_value\
    + ' where ' + query_field_name + '=' + query_field_value

    # Prints number of updated rows in the database.
    updatedRowCount = 0
    print str(updatedRowCount)


# Deletes all job offers that attend the field_name=field_value pair.
def delete_all(params):
  field_name, field_value = params
  
  # TODO Complete with your code and remove print below.
  print 'delete_all where ' + field_name + '=' + field_value


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'find where ' + field_name + '=' + field_value


# Prints how many job offers match the query field_name=field_value.
def count(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'count job offers where ' + field_name + '=' + field_value


# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
  # TODO Complete with your code and remove print below.
  print 'dump'

  #


# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(fieldNames):
  # TODO Complete with your code and remove print below.
  print 'view for fields ' + str(fieldNames)


def executeCommand(commandLine):
  tokens = commandLine.split('|') #assume that this symbol is not part of the data
  command = tokens[0]
  parameters = tokens[1:]

  if command == 'insert':
    insert(parameters)
  elif command == 'delete_all':
    delete_all(parameters)
  elif command == 'update_all':
    update_all(parameters)
  elif command == 'find':
    find(parameters)
  elif command == 'count':
    count(parameters)
  elif command == 'count_unique':
    count_unique(parameters)
  elif command == 'clear':
    clear()
  elif command == 'dump':
    dump(parameters)
  elif command == 'view':
    view(parameters)
  else:
    print 'ERROR: Command %s does not exist' % (command,)
    assert(False)

def executeCommands(commandFileName):
  f = open(commandFileName)
  for line in f:
    executeCommand(line.strip())

if __name__ == '__main__':
  #TODO: You should load the data from the database here
  print 'load'
  #
  executeCommands(sys.argv[1])
  #TODO: You should save the data here
  print 'save'
