print("""MENU
List of commands corresponding with each possible option:
CALCULATE: Takes accelerated time values and returns the normal time equivalent.
REGISTRY: Displays a list of past calculations, along with the time when they were performed.
CREDITS: Prints the list of super awesome members of the dev team.
QUIT: Closes the program.""")

def calculator():
    try:
        quick_time_hours = int(input("Please insert the amount of hours: "))
    except:
        print("Don't make fun of me Mr. Noycinho!")
        sleep(5)
        return
    quick_time_minutes = int(input("Please insert the amount of minutes: "))
    quick_time_seconds = int(input("Please insert the amount of seconds: "))
    total_quick_time = (quick_time_hours * 3600) + (quick_time_minutes * 60) + (quick_time_seconds)
    real_time_seconds = (total_quick_time / 3) * 4
    shown_time_hours = int(real_time_seconds / 3600)
    shown_time_minutes = int(real_time_seconds % 3600) / 60
    shown_time_minutes = int(shown_time_minutes)
    shown_time_seconds = int((real_time_seconds % 3600) % 60)
    The_time = (shown_time_hours, shown_time_minutes, shown_time_seconds)
    print(The_time)
    date = ctime()
    regalia = {The_time : date}
    record = list()
    record.append(regalia)
    print(record)
    while True:
        calculator()
def reg_show():
    print()


def main():
    menu = str(input("Please type the function you wish to use: "))
    if menu.upper() == "CALCULATE":
        calculator()
    else :
        sys.exit(12)
main()