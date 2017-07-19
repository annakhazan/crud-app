import csv

print '-------------------------'
print 'PRODUCTS APPLICATION'
print '-------------------------'

with open('../data/products.csv', 'rU') as f:
    csvreader = csv.reader(f)
    count = 0
    for row in csvreader:
        count += 1

print 'There are {0} products in the database. Please select an operation:'.format(count-1)
print 'Operation | Description'
print '-------------------------'
print 'List      | Display a list of product identifiers and names'
print 'Show      | Show information about a product'
print 'Create    | Add a new product'
print 'Update    | Edit an existing product'
print 'Destroy   | Delete an existing product'


def read_input(operation):
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
    else:
        print "Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'."

def reading_file_contents(path):
    print 'Reading contents of database'
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
        print text

def writing_file_contents(read_path, write_path):
    print 'Writing contents to database'
    with open(write_path, 'w+') as write_file:
        csvwriter = csv.writer(write_file)
        with open(read_path, 'rU') as read_file:
            csvreader = csv.reader(read_file, delimiter = '\t')
            for row in csvreader:
                csvwriter.writerow(row)

def overwriting_file_contents(path):
    print 'Overwriting contents to database'
    data = []
    with open(path, 'rU') as f:
        csvreader = csv.reader(f, delimiter = '\t')
        for row in csvreader:
            data.append(row)
    with open(path, 'w+') as f:
        csvwriter = csv.writer(f)
        for row in data:
            csvwriter.writerow(row)

#Reading from csv file
reading_file_contents('../data/products.csv')

#Writing to another file
writing_file_contents('../data/products.csv', '../data/writing-products.csv')

#Writing to same file
overwriting_file_contents('../data/products.csv')



def list_products():
    print 'listing products'

def show_product():
    print 'showing product'

def create_product():
    print 'creating product'

def update_product():
    print 'updating product'

def destroy_product():
    print 'destroying product'


# read_input(raw_input('Operation: ').title())
