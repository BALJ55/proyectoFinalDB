# -*- coding: utf-8 -*-

import sys
import psycopg2

exitFlag = False
chosenOption = 0


def main(args):
    conn = psycopg2.connect(database="testdb" if not args[0] else args[0],
                            user="postgres" if not args[1] else args[1],
                            password="pass123" if not args[2] else args[2],
                            host="127.0.0.1" if not args[3] else args[3],
                            port="5432" if not args[4] else args[4])

    while not exitFlag:
        print_menu()


def print_menu():
    print(" 1) Generar data para una semana")
    print(" 2) Generar data para un mes")
    print(" 3) Generar data para seis meses")
    print(" 4) Generar data para un año")
    print(" 5) Salir")
    chosenOption = input("Ingrese su opción: ")


def connect_to_db(args):


    if __name__ == '__main__':
        main(sys.argv)
