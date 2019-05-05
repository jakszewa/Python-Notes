#What is the meaning of 'if __name__ == '__main__':

#let see what is __name__ by default
print('This is first module ' + __name__)
#Other way of writing
print("First Module's Name: {}".format(__name__))

'''
OUTPUT: __main__

what is happening over here?
When python run any code it sets a few special variables
__name__ is one of those special variables
When python runs a python file directly(not imported through another file)
it sets this __name__ variable equal to __main__ 
thats what we are doing, we are running this code from the file itself not 
through some other file(s)
We can also import this file then the __name__ variable will be set to file name
    Example:
    first_module.py
        print('This is first module ' + __name__)
    second_module.py
        import first_module

    RUN: python3 second_module.py
    OUTPUT: first_module
This is happening because the file is not run directly but its imported by some other file.
'''

def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == "__main__":  # we are checking if this file is directly run by python or imported via some other file
    main()

'''
if you want to run main() from first_module.py in second_module.py do below
    import first_module
    first_module.main()

'''
