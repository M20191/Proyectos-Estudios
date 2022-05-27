class html:

	def __init__(self,page_name="") -> str:
		"""
		The visible name of the web
		"""
		self.page_name = page_name

		if page_name:
			page_name = page_name

		else:
			page_name = "NO NAME PAGE"
			
		with open("index.html", "w") as w:
			w.write(
				f'<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n<link rel="stylesheet" href="styles.css">\n<title>{page_name}</title>'
			)

	def linkCss(self, path) -> str:
		"""
		Bind the styles from the css file to your html
		"""
		with open("index.html", "a") as w:
			w.write(f'<link rel="stylesheet" type="text/css" href="{path}">')

	def closeHead(self) -> str:
		"""
		Close the head
		"""
		with open("index.html", "a") as w:
			w.write("\n</head>\n<body>\n\n")

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	def tag(self, content, tag, clas="", idd="", href="", src="") -> str:
		"""
		Create a new html tag
		"""
		self.clas= clas
		self.idd = idd
		self.href = href
		self.src = src

		if clas:
			clas = f' class="{clas}"'
		
		if idd:
			idd = f' id="{idd}"'

		if href:
			href = f' href="{href}"'
		
		if src:
			src = f' src="{src}"'

		with open("index.html", "a") as w:
			w.write(f"<{tag} {clas}{idd}{href}{src}>{content}</{tag}>\n")

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	def specialTagOpen(self, special, clas="", idd="", href="", src="") -> str:
		"""
		Open a new html Special Tag.
		Tags that need a start and an end
		---
		* body
		* head
		* links 
		* [more](https://developer.mozilla.org/es/docs/Web/HTML)
		"""
		
		self.clas= clas	
		self.idd = idd
		self.href = href
		self.src = src

		if clas:
			clas = f' class="{clas}"'
		
		if idd:
			idd = f' id="{idd}"'

		if href:
			href = f' href="{href}"'
		
		if src:
			src = f' src="{src}"'
		
		with open("index.html", "a") as w:
			w.write(f"\n<{special} {clas}{idd}{href}{src}>\n")	

	def specialTagClose(self, special) -> str:
		"""
		Close Special Tag
		"""
		with open("index.html", "a") as w:
			w.write(f"\n</{special}>")	


	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	def listOpen(self, tipe, typo="") -> str:
		"""
		Open a new list (ul,ol,others)
		"""
		self.typo = typo
		
		if typo:    
			typo = f' type="{typo}"'

		with open("index.html", "a") as w:
			w.write(f"\n<{tipe}{typo}>\n")
	
	
	def liElement(self, contentli) -> str:
		"""
		Create a new li element
		"""

		with open("index.html", "a") as w:
			w.write(f"<li>{contentli}</li>\n")


	def listClose(self, tipe) -> str:
		"""
		Close list (need the tipe)
		"""
		with open("index.html", "a") as w:
			w.write(f"</{tipe}>\n")	

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

	def closeBody(self) -> str:
		"""
		Close Body
		"""
		with open("index.html", "a") as w:
			w.write("\n</body>\n</html>")


	def clearPage(self) -> str:
		""""
		Clean page
		"""
		with open("index.html", "w") as w:
			w.write("")
