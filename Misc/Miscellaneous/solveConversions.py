__author__ = 'a-aron'
import sys
import os
path = '/home/a-aron/internship/summerInt/Misc/Miscellaneous/'
instructionSet = "Create function:\nCreate base unit: Simply create name to represent a real-world unit\nCreate unit: Create a non-base unit to use in future functions\nAdd name: Add a name to a preexisting unit i.e. (seconds --> second)"


def prepare_for_reimport(path, pyFile):
    """
    Eliminates current import of pyFile
    :param path: location of pyFile
    :param pyFile: filename including the .py extension
    :return: nothing
    """
    try:
        # So python doesn't know I already imported it
        del sys.modules[pyFile[:len(pyFile)-3]]
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

def name_not_taken(filename, var):
    exec("import {} as file_with_var".format(filename[:len(filename)-3]))
    return not var in dir(file_with_var)

def name_is_taken(filename, var):
    return not name_not_taken(filename, var)

def is_base_unit(var):
    if var == eval("cs.{}".format(var))[1]:
        return True
    else:
        return False

def merge_expression(expression):
    units_on_left = []
    units_on_right = []
    num = 1.0
    if not isinstance(expression, list):
        units_on_right.append(expression)
    else:
        num_list = [x for x in expression if isinstance(x, int) or isinstance(x, float)]
        result_list = []
        num = num_list[0]
        result_list.append(num)
        index = expression.index(num)
        units_on_left = []
        units_on_right = []
        for item in expression[:index]:
            multiplier, mult_units, div_units = merge_expression(item)
            # Do the opposite of the name because this is what is to the left of the num
            num = num / multiplier
            units_on_left = units_on_left + mult_units
            units_on_right = units_on_right + div_units
        for item in expression[index+1:]:
            multiplier, mult_units, div_units = merge_expression(item)
            num = num * multiplier
            units_on_left = units_on_left + div_units
            units_on_right = units_on_right + mult_units
    return num, units_on_right, units_on_left

def convert_unit_into_list(item):
        if isinstance(item, int) or isinstance(item, float):
            return item
        elif [] in list(item):
            def replace_empty_array(item):
                if not item:
                    return 1.0
                return item
            return map(replace_empty_array, item)
        elif isinstance(item, str):
            item = eval("cS.{}".format(item))
            return convert_unit_into_list(item)
        else:
            my_other_list = []
            for thing in item:
                my_other_list.append(convert_unit_into_list(thing))
            return my_other_list

def convert_into_base_units(expression):
    my_list = []
    for item in expression:
        my_list.append(convert_unit_into_list(item))
    num, mult_units, div_units = merge_expression(my_list)
    div_units.append(num)
    return div_units + mult_units


def accessible_name(name):
    return isinstance(name, str) and name in dir(cS)


def check_answer():
    return True


if __name__ == "__main__":

    backup_file(path, "conversionSolutions.py")
    backup_file(path, "solveConversions.py")

    user_input = "!exit"
    while user_input != "exit":

        prepare_for_reimport(path, "conversionSolutions.py")
        # Completes the re-import
        import conversionSolutions as cS


        """ TESTING LOCATION JUST BELOW """
        print convert_into_base_units(['hour', 'hour', 12960, 'kg', 'kilometer'])


        user_input = raw_input("Type in help for the help menu, exit to exit, or simply enter your command: ").lower()
        if user_input == "help":
            user_input = raw_input("Would you like to know how to use this application or do you want to see a list of pre-built items?(1,2): ")
            if user_input == "1":
                print instructionSet
            elif user_input == "2":
                # print available functions
                print [x for x in dir(cS) if not x.startswith("__")]

        elif user_input == "create function":
            pass

        elif user_input == "create base unit":
            new_unit = raw_input("Type in your new unit ('unit_name'): ")
            unit_rep = [[], new_unit]
            with open(os.path.join(path, "conversionSolutions.py"), 'a') as f:
                f.write("\n" + new_unit + " = " + str(unit_rep))

        elif user_input == "create unit":
            user_input = raw_input("Type in your unit in terms of a base unit ('name_of_unit # base_unit'): ")
            # splits input at spaces and puts the input out into a list
            user_input = user_input.split()
            new_unit, unit_rep = user_input[0], user_input[1:]
            unit_rep[0] = int(unit_rep[0])
            if name_is_taken("conversionSolutions.py", unit_rep[1]):
                keep_changes = raw_input(new_unit + " = " + str(unit_rep) + "\nKeep Changes?(y/n): ").lower()
                if keep_changes == 'y':
                    # Make permanent changes to file
                    with open(os.path.join(path, "conversionSolutions.py"), 'a') as f:
                        f.write("\n" + new_unit + " = " + str(unit_rep))
            else:
                print "Name {} doesn't exist yet.".format(unit_rep[1])

        elif user_input == "add name":
            user_input = raw_input("Type in your additional name for old unit ('alias' 'unit_name'): ").split()
            new_alias, unit_rep = user_input[0], user_input[1]# eval("cS.{}".format(user_input[1]))
            if name_is_taken("conversionSolutions.py", unit_rep):
                with open(os.path.join(path, "conversionSolutions.py"), 'a') as f:
                    if name_not_taken("conversionSolutions.py", new_alias):
                        f.write("\n" + new_alias + " = " + str(unit_rep))
                    else:
                        print "Name {} already taken.".format(new_alias)
            else:
                print "Name {} doesn't exist yet.".format(unit_rep)
