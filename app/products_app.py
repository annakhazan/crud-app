import csv

print '-------------------------'
print 'PRODUCTS APPLICATION'
print '-------------------------'

with open('../data/products.csv', 'rU') as f:
    csvreader = csv.reader(f)
    count = 0
    for row in csvreader:
        count += 1

#Checkpoints 1.1 and 2.1.4 Print a menu with number of products
print 'There are {0} products in the database. Please select an operation:'.format(count-1)
print 'Operation | Description'
print '-------------------------'
print 'List      | Display a list of product identifiers and names'
print 'Show      | Show information about a product'
print 'Create    | Add a new product'
print 'Update    | Edit an existing product'
print 'Destroy   | Delete an existing product'


def read_input(operation):
    #Checkpoint 1.2 Prompt user to choose operation, and print it
    if operation in ['List', 'Show', 'Create', 'Update', 'Destroy']:
        print "Operation '{0}' selected".format(operation)
    #Checkpoint 1.4 error handling for invalid operation
    else:
        print "Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'."
    #Checkpoint 1.3 Implement handler function
    if operation == 'List':
        list_products()
    elif operation == 'Show':
        show_product()
    elif operation == 'Create':
        create_product()
    elif operation == 'Update':
        update_product()
    elif operation == 'Destroy':
        destroy_product()

#Checkpoint 3.1
def list_products():
    print 'Listing products'

#Checkpoint 3.2
def show_product():
    print 'Showing product'

#Checkpoint 3.3
def create_product():
    print 'Creating product'

def update_product():
    print 'Updating product'

def destroy_product():
    print 'Destroying product'

#Checkpoint 1 User Inputs
read_input(raw_input('Operation: ').title())



#Checkpoint 2 - Reading and Writing to CSV file
#Checkpoints 2.1.1 and 2.1.2 Print entire contents of inventory CSV file
def reading_file_contents(path):
    print 'Reading contents of file'
    count = 0
    text = ''
    with open(path, 'rU') as f:
        csvreader = csv.reader(f, delimiter='\t')
        for row in csvreader:
            if count == 0:
                keys = row
            else:
                values = row
                text += '+ ' + str(dict(zip(keys, values))) + '\n'
            count += 1
        #Checkoint 2.1.3 Print number of products
        print 'There are {0} products in database'.format(count-1)
        print text
reading_file_contents('../data/products.csv')

#Checkpoint 2.2.1 Write some random content to data/writing-stuff.csv
def writing_file_contents(write_path, data):
    print 'Writing contents to file'
    with open(write_path, 'w+') as write_file:
        csvwriter = csv.writer(write_file)
        for row in data:
            csvwriter.writerow(row)
sample_data = [
    ['Field 1', 'Field 2', 'Field 3'],
    ['Datapoint 1', 'Datapoint 2', 'Datapoint 3']
]
writing_file_contents('../data/writing-stuff.csv', sample_data)

#Checkpoint 2.2.2 Read existing inventory from products.csv and write it to data/writing-products.csv
def reading_and_writing_contents(read_path, write_path):
    print 'Reading and writing contents to file'
    with open(write_path, 'w+') as write_file:
        with open(read_path, 'rU') as read_file:
            csvreader = csv.reader(read_file, delimiter='\t')
            csvwriter = csv.writer(write_file, delimiter='\t')
            for row in csvreader:
                csvwriter.writerow(row)
reading_and_writing_contents('../data/products.csv', '../data/writing-products.csv')

#Checkpoint 2.2.3 Reading and writing to same file
def overwriting_contents(path):
    print 'Overwriting file contents'
    with open(path, 'rU') as read_file:
        csvreader = csv.reader(read_file, delimiter='\t')
        data = []
        for row in csvreader:
            data.append(row)
    with open(path, 'w+') as write_file:
        csvwriter = csv.writer(write_file, delimiter='\t')
        for row in data:
            csvwriter.writerow(row)
overwriting_contents('../data/products.csv')



# def writing_file_contents(read_path, write_path):
#     print 'Writing contents to file'
#     with open(write_path, 'w+') as write_file:
#         csvwriter = csv.writer(write_file)
#         with open(read_path, 'rU') as read_file:
#             csvreader = csv.reader(read_file, delimiter = '\t')
#             for row in csvreader:
#                 csvwriter.writerow(row)
#
# def writing_file_contents(read_path, write_path):
#     print 'Writing contents to database'
#     with open(write_path, 'w+') as write_file:
#         csvwriter = csv.writer(write_file)
#         with open(read_path, 'rU') as read_file:
#             csvreader = csv.reader(read_file, delimiter = '\t')
#             for row in csvreader:
#                 csvwriter.writerow(row)
#
# def overwriting_file_contents(path):
#     print 'Overwriting contents to database'
#     data = []
#     with open(path, 'rU') as f:
#         csvreader = csv.reader(f, delimiter = '\t')
#         for row in csvreader:
#             data.append(row)
#     with open(path, 'w+') as f:
#         csvwriter = csv.writer(f)
#         for row in data:
#             csvwriter.writerow(row)
#
# # #Reading from csv file
# # reading_file_contents('../data/products.csv')
# #
# # #Writing to another file
# # writing_file_contents('../data/products.csv', '../data/writing-products.csv')
# #
# # #Writing to same file
# # overwriting_file_contents('../data/products.csv')
#
#
#

#
#
