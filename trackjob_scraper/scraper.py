import requests
from bs4 import BeautifulSoup



class Trackjob:


    def __init__(self, username, password):
        self.url = "https://adm.trackjob.com.br"
        self.session = None

        if username and password:
            self.login(username, password)

    #not implemented
    def check_authenticated(self, username, password):
        '''Check if the user is logged in an active session'''
        print('method "check_authenticated" not implemented!')
        return False


    def login(self, username, password):
        '''initialize a session in trackjob'''

        self.session = requests.Session()
        login_url = '%s/site/login' % self.url

        request = self.session.get(login_url)
        html = BeautifulSoup(request.text, 'html.parser')

        data = {
            "_csrf-backend": html.input['value'],
            "LoginForm[username]": username,
            "LoginForm[password]": password,
            "LoginForm[rememberMe]": 0,
            'login-button': None,
        }

        response = self.session.post(login_url, data=data)
        print('Login realizado!')
    

    def get_report_passenger_boarding(self, date_start, date_end):
        '''return a report passenger boarding between dates'''

        req = self.session.get('%s/relatorio/listagem-embarques?filtroData=%s - %s' % (self.url, date_start, date_end))
        html = BeautifulSoup(req.text, 'html.parser')
        csrf_backend = html.find('meta', {'name': 'csrf-token'}).get('content')

        data = {
            "_csrf-backend": csrf_backend,
            'export_type': 'Xlsx',
            'exportFull_w1': '1',
            'export_columns': '' ,
            'column_selector_enabled': 0
        }

        post = self.session.post('%s/relatorio/listagem-embarques?filtroData=20/08/2021 - 20/08/2021' % self.url, data=data)

        return post.content



