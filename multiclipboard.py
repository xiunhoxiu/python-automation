import sys  # = "system" to pass cmds like save, test etc. to the terminal 
import clipboard
import json

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)
    if command == "save":
        print("save")
    elif command == "list":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("please pass exactly one command.")

