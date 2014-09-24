import sys
from collections import defaultdict
import os.path

job_db = defaultdict(dict)
job_id_list = []
dump_list = []
write_list = []

# 'JobID',
categories = ['Agency','# Of Positions','Business Title','Civil Service Title','Salary Range From','Salary Range To','Salary Frequency','Work Location','Division/Work Unit','Job Description','Minimum Qual Requirements','Preferred Skills','Additional Information','Posting Date']

def clear():
  # TODO Complete with your code and remove print below.
  
  global job_db 
  job_db = defaultdict(dict)
  global job_id_list 
  job_id_list = []
  global dump_list
  dump_list = []
  global write_list
  write_list = []

# Inserts a job offer into the database.
def insert(fieldValues):
  # TODO Complete with your code and remove print below.
  
  job_id = fieldValues[0]
  job_data = fieldValues[1:]

  if job_id not in job_db:
    job_id_list.append(job_id)

    for i in xrange(len(job_data)):
        job_db[job_id][categories[i]]=job_data[i]
  
  job_id_list.sort()

# Updates all job offers that attend the field_name=old_value pair.
def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    updatedRowCount = 0
    if query_field_name == 'Job ID':
      job_db[query_field_value][update_field_name] = update_field_value
      updatedRowCount += 1

    else:
      for i in job_id_list:
        if job_db[i][query_field_name] == query_field_value:
          job_db[i][update_field_name] = update_field_value
          updatedRowCount += 1

    # TODO Complete with your code and remove print below.
    
    
    print str(updatedRowCount)


# Deletes all job offers that attend the field_name=field_value pair.
def delete_all(params):
  field_name, field_value = params
  
  if field_name == 'Job ID':
    del job_db[field_value]
    job_id_list.remove(field_value)
  else: 
    for i in job_id_list:
      if job_db[i][field_name] == field_value:
        del job_db[i][field_name]
        job_id_list.remove(i)

  


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  

  find_line = []
  if field_name == 'Job ID':
    for job_id in job_db:
      if job_id == field_value:

        find_line = [field_value]

        for c in categories:
          find_line.append("|"+job_db[field_value][c])

        write_list.append("".join(find_line)+"\n")

  else:
    for job_id in job_id_list:
      find_line = []
      if job_db[job_id][field_name] == field_value:

        find_line = [job_id]

        for c in categories:
          find_line.append("|"+job_db[job_id][c])

        write_list.append("".join(find_line)+"\n")


# Prints how many job offers match the query field_name=field_value.
def count(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'count job offers where ' + field_name + '=' + field_value


# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
  # TODO Complete with your code and remove print below.

  for job_id in job_id_list:
    print_line = [job_id]
    for c in categories:
      print_line.append("|"+job_db[job_id][c])
    dump_list.append("".join(print_line))
    write_list.append("".join(print_line)+"\n")

  for i in dump_list:
    print i


# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(fieldNames):
  # TODO Complete with your code and remove print below.
  
  for job_id in job_id_list:
    view_line = []
    for view in fieldNames:
      if view == 'Job ID':
        view_line.append(job_id+"|")
      else:
        view_line.append(job_db[job_id][view]+"|")
    write_list.append("".join(view_line)+"\n")

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
  
  if os.path.isfile('database.txt'):
    with open('database.txt','r+') as raw_database:
      data = []
      for line in raw_database:
        data.append(line.split("|"))
    
    for line in data:
      insert(line)

  executeCommands(sys.argv[1])
  #TODO: You should save the data here
  
  db = open('database.txt','w')
  for i in write_list:
    db.write(i)