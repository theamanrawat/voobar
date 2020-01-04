import requests
from tabulate import tabulate


def VooCode(url,out):
	try:
		x = requests.get(url)
		code = str(x.status_code)
		# print(tabulate([[data[1], code]],tablefmt='fancy_grid',floatfmt=".4f"))
		col_width = 40
		print("+"+"-"*col_width+"+"+"-"*col_width+"+")
		print("|"+str(code).center(col_width)+"|"+url.center(col_width)+"|")
		print("+"+"-"*col_width+"+"+"-"*col_width+"+")
		if out != None:
			o = open(out,'a')
			o.write(url+'\n')
			o.close()
		else:
			pass
	except:
		pass


