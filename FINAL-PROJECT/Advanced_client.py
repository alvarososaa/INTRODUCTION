import http.client
import termcolor
import Advanced_utils as au
PORT = 8080
IP = "localhost"
print(f"Connection to the server: {IP}: {PORT}")
try:
    termcolor.cprint("CONNECTION TO THE SPECIES LIST", "yellow")
    connection = http.client.HTTPConnection(IP, PORT)
    path = "/listSpecies?limit=2&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)

    termcolor.cprint("CONNECTION TO THE SPECIES LIST WITH NO LIMIT", "yellow")
    path = "/listSpecies?limit=&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)
    termcolor.cprint("CONNECTION TO THE SPECIES LIST WITH an INVALID LIMIT", "yellow")
    path = "/listSpecies?limit=ABAB&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)

    termcolor.cprint("CONNECTION TO THE KARYOTYPE", "yellow")
    path = "/Karyotype?specie=mouse&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)
    termcolor.cprint("CONNECTION TO THE KARYOTYPE WITH A NOT VALID SPECIE", "yellow")
    path = "/Karyotype?specie=PROGRAMMING&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)

    termcolor.cprint("CONNECTION TO THE CHROMOSOME LENGTH", "yellow")
    path = "/chromosomeLength?specie=mouse&chromo=10&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)
    termcolor.cprint("CONNECTION TO THE CHROMOSOME LENGTH WITH AN INVALID CHROMO NAME", "yellow")
    path = "/chromosomeLength?specie=mouse&chromo=100&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)



    termcolor.cprint("CONNECTION TO THE GENE SEQUENCE", "yellow")
    path = "/geneSeq?gene=FRAT1&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)

    termcolor.cprint("CONNECTION TO THE GENE INFO", "yellow")
    path = "/geneInfo?gene=FRAT1&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json(contents)

    termcolor.cprint("CONNECTION TO THE GENE CALCULATIONS", "yellow")
    path = "/geneCalc?gene=FRAT1&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json_calculations(contents)
    termcolor.cprint("CONNECTION TO THE GENE CALCULATIONS WITH A NOT STORED GENE", "yellow")
    path = "/geneCalc?gene=INVALID_GENE&json=1"
    contents = au.requesting_connection(path, connection)
    au.print_json_calculations(contents)

except ConnectionRefusedError:
    print("Sorry there was a connection error")
    exit()

