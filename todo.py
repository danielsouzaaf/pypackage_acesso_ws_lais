import requests

def _url(path):
    #return 'http://integra.telessaude.ufrn.br/api/'
    return 'http://127.0.0.1:8000/api' + path

########################################################################################################################
############################################METODOS DA UF###############################################################
########################################################################################################################
class acesso_barramento():

    def __init__(self, token):
       if len(token.split(' ')) == 2:
           self.token = token.split(' ')[1]
       else:
           self.token = token
       headers = {

            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Token %s' % self.token
        }

    @staticmethod
    def get_municipios_por_uf(self, uf):

        response = requests.get(_url('/uf/%s/municipios' %uf), headers=self.headers)
        data = response.json()
        print data
        return data

    @staticmethod
    def get_uf(self):

        response = requests.get(_url('/uf/'), headers=self.headers)
        data = response.json()
        print data
        return data

    ####################################################################################################################
    ############################################METODOS DOS TIPOS#######################################################
    ####################################################################################################################
    @staticmethod
    def get_tipoestabelecimento(self):
        response = requests.get(_url('tipos/tipoestabelecimento/'), headers=self.headers)
        data = response.json()
        print data
        return data

    @staticmethod
    def get_subtipoestabelecimento(self):
        response = requests.get(_url('tipos/subtipoestabelecimento/'), headers=self.headers)
        data = response.json()
        print data
        return data

    @staticmethod
    def get_tipogestao(self):
        response = requests.get(_url('tipos/tipogestao/'), headers=self.headers)
        data = response.json()
        print data
        return data

    @staticmethod
    def get_cbo(self):
        response = requests.get(_url('tipos/cbo/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipotelefone(self):
        response = requests.get(_url('tipos/tipotelefone/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipoequipe(self):
        response = requests.get(_url('tipos/tipoequipe/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_esferaadministrativa(self):
        response = requests.get(_url('tipos/esferaadministrativa/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_naturezaorganizacao(self):
        response = requests.get(_url('tipos/naturezaorganizacao/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_vinculoempregaticio(self):
        response = requests.get(_url('tipos/vinculoempregaticio/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipovinculoempregaticio(self):
        response = requests.get(_url('tipos/tipovinculoempregaticio/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_subtipovinculoempregaticio(self):
        response = requests.get(_url('tipos/subtipovinculoempregaticio/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipoinscricaoprofissional(self):
        response = requests.get(_url('tipos/tipoinscricaoprofissional/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipoespecialidade(self):
        response = requests.get(_url('tipos/tipoespecialidade/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipoinscricao(self):
        response = requests.get(_url('tipos/tipoinscricao/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_especialidadeambulatorial(self):
        response = requests.get(_url('tipos/especialidadeambulatorial/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_fonteinformacao(self):
        response = requests.get(_url('tipos/fonteinformacao/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_tipoequipamento(self):
        response = requests.get(_url('tipos/tipoequipamento/'), headers=self.headers)
        data = response.json()
        print data
        return data
        pass

    @staticmethod
    def get_especialidade(self):
        response = requests.get(_url('tipos/especialidade/'), headers=self.headers)
        data = response.json()
        print data
        return data

    ####################################################################################################################
    ############################################METODOS DA REGIAO DE SAUDE##############################################
    ####################################################################################################################
    @staticmethod
    def get_regiaosaude(self):
        response = requests.get(_url('/regiaosaude/'), headers=self.headers)
        data = response.json()
        print data
        return data

    ####################################################################################################################
    ############################################METODOS DA REGIAO GEOGRAFICA############################################
    ####################################################################################################################
    @staticmethod
    def get_regiaogeografica(self):
        response = requests.get(_url('/regiaogeografica/'), headers=self.headers)
        data = response.json()
        print data
        return data

    ####################################################################################################################
    ############################################METODOS DO PROFISSIONAL#################################################
    ####################################################################################################################
