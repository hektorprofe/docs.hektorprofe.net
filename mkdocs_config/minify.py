import os
import io
from htmlmin.minify import html_minify
from glob import glob

for x in os.walk("C:\\Users\\hcost\\Documents\\Proyectos\\hektorprofe.net\\site\\"):
    for y in glob(os.path.join(x[0], '*.html')):
        try:
            f = io.open(y, mode="r", encoding="utf-8")
            html = html_minify(f.read())
            f.close()
            f = io.open(y, mode="w", encoding="utf-8")
            f.write(html)
            f.close()
        except:
            print("Error minificando", y)