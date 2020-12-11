from app import create_app

aplicativo = create_app()

if __name__ == '__main__':
    aplicativo.run(debug = True)
