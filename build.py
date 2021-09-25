import json
def main():
    f = open("./data.json","r")
    a = json.load(f)
    html = '''
    <!doctype html>
<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p>{}</p>
  </body>
</html>
    '''
    
    out = open("./_build/index.html","w")
    s = ""
    for i in a:
        s += i["name"] + "\n"
    out.write(html.format(s))
    out.close()
    f.close()

main()