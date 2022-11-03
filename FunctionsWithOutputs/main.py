# Functions with Outputs
def format_name(f_name, l_name):
    """ Take a first and last name and format it to return the
    title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

first_name = input("Enter you first name: \n")
last_name = input("Enter your last name : \n")
x = format_name(first_name, last_name)
print(x)

