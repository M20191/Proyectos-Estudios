#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytml import *
from os import getcwd
import pyodbc

page = html("TOOLS-M2")
page.linkCss("./styles.css")
# "crossorigin="anonymous"
page.specialTagOpen("script",src="https://kit.fontawesome.com/4aff08c8b5.js")
page.specialTagClose("script")
page.closeHead()

DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
DB_PATH = getcwd() + "./herramientas.accdb"
conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
cursor = conn.cursor()


# HEADER
page.specialTagOpen("header")
page.listOpen("ul")


menu = ["INICIO","TIENDA","SERVICIOS","CONTACTO"]

for menu_display in menu:
	page.specialTagOpen("a",href="#")
	page.liElement(menu_display)
	page.specialTagClose("a")

page.listClose("ul")
page.specialTagClose("header")


# NAV

icons = ["fa-solid fa-toolbox icon",
		"fa-solid fa-trowel icon",
		"fa-solid fa-wrench icon",
		"fa-solid fa-screwdriver icon"]

links = ["#toolbox","#trowel","#wrench"

]

# LINKS ICONS
page.specialTagOpen("nav")
page.listOpen("ul")


for icon in icons:
	page.specialTagOpen("li")
	for link in links:
		page.specialTagOpen("a",href=f"{link}")	

	page.specialTagOpen("i", f"{icon}")

	page.specialTagClose("i")
	page.specialTagClose("a")

page.listClose("ul")
page.specialTagClose("nav")



# MAIN
# Use the other for (up)


page.specialTagOpen("main")

def titles_tools(id_icon,id_name,id_link):
	page.listOpen("ul")
	page.specialTagOpen("li")
	page.specialTagOpen("i",f"{icons[id_icon]}")
	page.specialTagClose("i")
	page.specialTagClose("li")

	id_links = ["toolbox","trowel","wrench"]
	id_names = ["CAJAS","PICOS","LLAVES"]
	
	page.specialTagOpen("li")
	page.tag(f"{id_names[id_name]}","h2",idd=f"{id_links[id_link]}")
	page.specialTagClose("li")

	page.listClose("ul")

# Main classes

# Recorrer cada una de las filas e imprimirlas en pantalla.


def sections(table):
	page.specialTagOpen("div","sec")
	query = cursor.execute(f"SELECT * FROM {table}")
	# Recorrer cada una de las filas e imprimirlas en pantalla.

	for row in query.fetchall():
		page.specialTagOpen("div","herramienta")
		
		# Nombre
		page.tag(f"{row[0]}","h3")
		
		# Link
		page.tag(".","img","img",src=f"{row[2]}")
		
		# Precio
		page.tag(f"$ {row[1]}","h4",clas="herramienta")

		page.specialTagOpen("a",href="#")
		page.specialTagOpen("button")
		page.tag("AGREGAR AL CARRO","h4")
		page.specialTagClose("button")
		page.specialTagClose("a")


		# Close herramientas
		page.specialTagClose("div")

	# Close sec
	page.specialTagClose("div")



titles_tools(0,0,0)
sections("herramientas")

titles_tools(1,1,1)
sections("picos")

titles_tools(2,2,2)
sections("llaves")

page.specialTagClose("main")

cursor.close()

page.closeBody()