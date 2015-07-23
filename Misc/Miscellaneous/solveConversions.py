__author__ = 'a-aron'
import sys
import os
import csv

path = '/home/a-aron/internship/summerInt/Misc/Miscellaneous/'
instructionSet = ""

def prepare_for_reimport(path, pyFile):
    """
    Eliminates current import of pyFile
    :param path: location of pyFile
    :param pyFile: filename including the .py extension
    :return: nothing
    """
    try:
        # So python doesn't know I already imported it
        del sys.modules[pyFile[:]]
        # So python doesn't just reuse the compiled version we have to delete it
        # BE VERY CAREFUL NOT TO TAKE OUT THIS 'c' below, if removed the entire .py will be deleted
        os.remove(os.path.join(path, pyFile + 'c'))
    except KeyError:
        # do nothing because it already works
        pass
    except OSError:
        # do nothing because it already works
        pass

def backup_file(path, filename):
    lines = ""
    with open(os.path.join(path, filename), 'r') as fileToBeBackedUp:
        lines += fileToBeBackedUp.read()
    with open(os.path.join(path, "backupFiles/backup" + filename), 'w') as backup:
        backup.write(lines)


if __name__ == "__main__":

    backup_file(path, "conversionSolutions.py")
    backup_file(path, "solveConversions.py")

    user_input = "!exit"
    while user_input != "exit":

        backup_file(path, "conversionSolutions.py")
        prepare_for_reimport(path, "conversionSolutions.py")
        # Completes the re-import
        import conversionSolutions as cS

        user_input = raw_input("Type in help for the help menu, exit to exit, or simply enter your command.").lower()
        if user_input == "help":
            user_input = raw_input("Would you like to know how to use this application or do you want to see a list of pre-built functions?(1,2)")
            if user_input == "1":
                print instructionSet
            elif user_input == "2":
                # print available functions
                print [x for x in dir(cS) if not x.startswith("__")]

        elif user_input == "create function":
            pass

        elif user_input == "create base unit":
            pass

        elif user_input == "create unit":
            pass
