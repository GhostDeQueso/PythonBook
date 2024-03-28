def main():

    name = input("Your name: ")
    about = input("Smt about u: ")

    html_content = f"""
    <html>
    <head></head>
    <body>
        <center>
            <h1>{name}</h1>
        </center>
        <hr />{about}<hr />
    </body>
    </html>
    """

    html = open('user.html', 'w')

    write_html = html.write(html_content)

    html.close()

main()