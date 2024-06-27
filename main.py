from app import start_app

app = start_app()

if __name__ == '__main__':
#                ''                    '5058'
    app.run(host='0.0.0.0', port='5050', debug=True) # 0.0.0.0 permite acesso fora do container docker
    