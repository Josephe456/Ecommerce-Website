from Website import create_app

app = create_app()

#Prevents running of the webserver when imported
if __name__ == '__main__':
    app.run(debug=True)

