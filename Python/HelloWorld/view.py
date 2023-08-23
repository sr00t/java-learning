from os import walk
_, _, filenames = next(walk('img'))

print(filenames)
html = """
<html>
   <head>
   <title></title>
   <style>
   img {
   width: 500px;
   height: 150px;
   object-fit: cover;
   }
   </style>
   </head>
   <body>
   """
for f in filenames:
    html += '<img src="img/' + f + '">'

html += """
   <h1>Gallery for my photos</h1>
   <img src="https://cdn.pixabay.com/photo/2023/08/08/15/01/flower-8177578_960_720.jpg">  
   </body>
</html>
"""

print(html)

# write html string to file.html
with open("index.html", "w") as file:
    file.write(html)