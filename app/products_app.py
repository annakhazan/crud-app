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
    if operation.title() == 'List':
        list_products()
    elif operation.title() == 'Show':
        show_products()
    elif operation.title() == 'Create':
        create_products()
    elif operation.title() == 'Update':
        update_products()
    elif operation.title() == 'Destroy':
        destroy_products()
    else:
        print "Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'."

# Reading and writing to csv file
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
    with open(write_path, 'w+') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['this is a row'])

reading_file_contents('../data/products.csv')

writing_file_contents('../data/products.csv', '../data/writing-stuff.csv')

def list_products():
    print 'listing products'

def show_products():
    print 'showing products'

def create_products():
    print 'creating products'

def update_products():
    print 'updating products'

def destroy_products():
    print 'destroying products'


# read_input(raw_input('Operation: '))
