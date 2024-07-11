def line(katz):
    if len(katz) ==0:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently:"
        for index, name in enumerate(katz, start=1):
            current_line += f" {index}. {name}"
        print(current_line)

def take_a_number(katz, name):
    katz.append(name)
    position = len(katz)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz):
    if len(katz) ==0:
        print("There is nobody waiting to be served!")
    else:
        serving = katz.pop(0)
        print(f"Currently serving {serving}.")

