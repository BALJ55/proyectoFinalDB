# -*- coding: utf-8 -*-

import sys
import psycopg2
from random import randint

adresses = ["4 Smith Store St.Danbury, CT 06810", "8932 Boston Street North Royalton, OH 44133",
            "57 Church Ave. Shelton, CT 06484", "9536 Grand St. Peachtree City, GA 30269",
            "9283 Wrangler St. Petersburg, VA 23803", "517 Wall Drive Hopewell Junction, NY 12533",
            "843 Carson Street Jonesborough, TN 37659", "574 Depot Road Cranberry Twp, PA 16066",
            "49 West Wrangler Court Ridgefield, CT 06877", "31 Grandrose Court Maryville, TN 37803",
            "382 Court Drive Hanover Park, IL 60133", "630 Branch St. Amityville, NY 11701",
            "25 Lakewood Dr. Orland Park, IL 60462", "95 North Dunbar Street Bradenton, FL 34203",
            "53C Carpenter Rd. Mc Lean, VA 22101", "5 South Poplar St. Suite 38 ",
            "Collierville, TN 3801715 Lake Forest Court", " Fresno, CA 9370645 Airport Ave. ",
            "Bayonne, NJ 07002299 Amherst Road ", "Fairfax, VA 220307 Pumpkin Hill Drive",
            " Suite 28 Oviedo, FL 32765", "7830 Bridge Ave. Oak Ridge, TN 37830",
            "52 Tunnel Street Vienna, VA 22180", "284 Plymouth Road Southampton, PA 18966",
            "9900 Mill Pond Avenue Olney, MD 20832", "25 S. 10th Dr. Vicksburg, MS 39180",
            "997 East Garfield Avenue Matthews, NC 28104", "9093 West Gartner Ave. Central Islip, NY 11722",
            "9110 West Vernon Road Waldorf, MD 20601", "54 Ann Lane Gastonia, NC 28052",
            "953 White Ave. Stafford, VA 22554", "33 Chapel Road Milledgeville, GA 31061",
            "8136 Edgewood Lane Marcus Hook, PA 19061", "223 Linda Dr. Schaumburg, IL 60193",
            "487 Del Monte St. Omaha, NE 68107", "472 Stonybrook Street Seymour, IN 47274",
            "1 Lincoln Ave. Canyon Country, CA 91387", "8263 Jones Court West Roxbury, MA 02132",
            "79 Bay Meadows St. Kernersville, NC 27284", "34 Chestnut Court Riverview, FL 33569",
            "389 South Redwood St. Lumberton, NC 28358"]
towns = ["St.Danbury", "Bosto", "St. Petersburg", "New York", "Jonesborough", "Cranberry", "Ridgefield", "Maryville",
         "Hanover", "Ametyville", "Lakewood", "Bradento", "Carpenter", "Soyth Poplar", "Collierville", "Fresno",
         "Bayonne", "Fairfax", "Oviedo", "Oak Ridge", "Vienna", "Southampto", "Olney", "Vicksburg", "Matthews",
         "Islip", "Waldorf", "Gastonia", "Safford", "Milledgeville", "Marcus Hook", "Schaumburg", "Omaha", "Seymour",
         "Canyon Country", "Roxbury", "Kernersville", "Riverview", "Lumberto"]
cities = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "I", "KS", "KY", "LA",
          "MA", "MD", "ME", "MI", "M", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
          "OR", "PA", "RI", "SC", "SD", "T", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

conn = psycopg2.connect(database="Chinook",
                        user="postgres",
                        password="pascalito",
                        host="127.0.0.1",
                        port="5432")
cur = conn.cursor()
temp_inline_holder = 0


def main(args):
    exitFlag = False

    while not exitFlag:
        print_menu()
        chosenOption = int(input("Ingrese su opción: "))

        if chosenOption == 1:
            generateData(7)
        if chosenOption == 2:
            generateData(30)
        if chosenOption == 3:
            generateData(60)
        if chosenOption == 4:
            generateData(365)
        if chosenOption == 5:
            exitFlag = true

    conn.close()


def generateData(days):
    cur.execute('SELECT "invoiceId" FROM invoice ORDER BY "invoiceId" DESC LIMIT 1')

    # display the PostgreSQL database server version
    data = cur.fetchone()
    invoiceID = data[0]
    cur.execute('SELECT "invoicelineId" FROM invoiceline ORDER BY "invoicelineId" DESC LIMIT 1')

    # display the PostgreSQL database server version
    data = cur.fetchone()
    inlineID = data[0]
    # generate n invoice lines
    for temp_invoice_id in range(invoiceID+1, invoiceID +1+ days * randint(1, 10)):
        cur.execute(generateRandomInvoice(temp_invoice_id, getClientID()))
        print("generated new invoice_id")
        for temp_inline_id in range(inlineID+1, inlineID + 4):
            cur.execute(generateRandomInvoiceLine(temp_inline_id, temp_invoice_id))
            print("generated new inline")
        inlineID = inlineID + 5

    print("se han generado registros")


def getClientID():
    return randint(1, 59)


def getRandomArrayFromOpts(opts):
    return opts[randint(0, len(opts)-1)]


def getRandomDate():
    return str(randint(2015, 2020)) + "/" + str(randint(1, 12)) + "/" + str(randint(1, 28))


def getRandomTrackID():
    return randint(1, 3503)


def generateRandomInvoice(invoiceId, customerID):
    print('INSERT INTO "invoice" ("invoiceId", "customerId", "invoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry", "BillingPostalCode", "Total") VALUES (' + str(invoiceId) + ', ' + str(customerID) + ', \'' + str(getRandomDate()) + '\', \'' + str(getRandomArrayFromOpts(adresses)) + '\', \'' + str(getRandomArrayFromOpts(towns)) + '\', \'' + str(getRandomArrayFromOpts(cities)) + '\', \'USA\', \'' + str(randint(1010, 9999)) + '\', 0.99);')
    return str('INSERT INTO "invoice" ("invoiceId", "customerId", "invoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry", "BillingPostalCode", "Total") VALUES (' + str(invoiceId) + ', ' + str(customerID) + ', \'' + str(getRandomDate()) + '\', \'' + str(getRandomArrayFromOpts(adresses)) + '\', \'' + str(getRandomArrayFromOpts(towns)) + '\', \'' + str(getRandomArrayFromOpts(cities)) + '\', \'USA\', \'' + str(randint(1010, 9999)) + '\', 0.99);')

def generateRandomInvoiceLine(invoiceLineId, invoiceId):
    print('INSERT INTO "invoiceline" ("invoicelineId", "invoiceId", "trackId", "UnitPrice", "Quantity") VALUES (' + str(invoiceLineId) + ', ' + str(invoiceId) + ', ' + str(getRandomTrackID()) + ', 0.99, 1);')
    return str('INSERT INTO "invoiceline" ("invoicelineId", "invoiceId", "trackId", "UnitPrice", "Quantity") VALUES (' + str(invoiceLineId) + ', ' + str(invoiceId) + ', ' + str(getRandomTrackID()) + ', 0.99, 1);')


def print_menu():
    print("")
    print(" 1) Generar data para una semana")
    print(" 2) Generar data para un mes")
    print(" 3) Generar data para seis meses")
    print(" 4) Generar data para un año")
    print(" 5) Salir")


if __name__ == '__main__':
    main(sys.argv)
