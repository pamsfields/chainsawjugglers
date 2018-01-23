#Pam Fields
#ITEC 2905-01
#Lab 3: SQLite

import SQLite3

db = sqlite.connect('chainsawjugglerrecord.db') #Create a db for the data

cur = db.cursor() # Need a cursor object to perform operations

# Create a table
cur.execute('create table if not exists jugglers (name str, country str, catches int)')

#Add current jugglers, countries, and catches
cur.execute('insert into jugglers values (Ian Stewart, Canada, 94)')
cur.execute('insert into jugglers values (Aaron Gregg, Cananda, 88)')
cur.execute('insert into jugglers values (Chad Taylor, USA, 78)')


def handle_choice(choice):
    while True:

        if choice == "1":
            show_list()

        if choice == "2":
            update_juggler()

        if choice == "3":
            get_new_juggler()
            add_to_db()

        if choice == "4":
            delete_juggler()

        if choice == "5":
            ask_for_juggler_name()

        if choice == "q":
            break


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show list of jugglers
        2. Update juggler
        3. Add juggler
        4. Delete juggler
        5. Search for juggler
        q. Quit
    ''')
    choice = input('Enter your selection: ')

    return choice


def show_list(jugglers):
    ''' Format and display a list of book objects'''
    cur.execute('select * from jugglers')

    # Execute a query. Results are contained in cursor object
    for row in cur:
        print(row) #pretty printing

def get_new_juggler():
    name = input('Enter juggler name: ')
    country = input('Enter juggler country: ')
    catches = int(input('Enter number of catches (as an integer): '))

def add_to_db(name, country, catches):
    with sqlite.connect(db):
        cur = db.cursor()
        cur.execute('insert into jugglers values (?, ?, ?)', (name, country, catches))
        cur.commit()

#Add search option for database
def ask_for_juggler_name():
    while True:
        try:
            name = input('Enter juggler name')
            if name != name in jugglers:
                print('Please enter a name in the database')
            else:
                cur.execute('select * from jugglers where name = ?', (name))
                for row in cur:
                    print(row)



#Add ability to update a juggler's information
def update_juggler():
    ask_for_juggler_name()
    country = input('Enter juggler country: ')
    catches = input('Enter number of catches (as an integer): ')
    cur.execute("update jugglers set country = ? and catches = ?  where name = ?", (country, catches, name))
    cur.commit()


#Add ability to delete a juggler and his attached information

def delete_juggler():
    ask_for_juggler_name()
    cur.execute('delete from jugglers where name = ?', (name)
    cur.commit()


if __name__ == '__main__':
    main()
