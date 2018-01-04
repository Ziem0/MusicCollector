import logging

# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='myprogram.log', level=logging.ERROR)


a = 1 + 2
logging.error(a)


# try:
#     age = int(input("How old are you? "))
# except ValueError as err:
#     logging.exception(err)
