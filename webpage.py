import webbrowser
from pathlib import *

def create_webpage():
    f = open("new.html", 'w')
    page = '''
    <html>
    <head></head>
    <script>
        function myFunction() {
            var x = document.getElementById("myDIV");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }
    </script>
    <body>
    <button onclick="myFunction()">Click Me</button>
    <div id="myDIV">
        This is my DIV element.
    </div>
    </body>
    </html>
    '''

    f.write(page)
    f.close()

    p = Path("new.html")
    webbrowser.open("file:///" + str(p.absolute()))


if __name__ == "__main__":
    create_webpage()