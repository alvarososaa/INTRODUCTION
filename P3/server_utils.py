def print_colored(message, color):
    import termcolor
    termcolor.cprint(message , color)
def ping():
     print_colored("Ping command", "green")
