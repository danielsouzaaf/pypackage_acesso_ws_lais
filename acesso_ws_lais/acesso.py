import requests
from collections import namedtuple

def _url(path):
    return 'http://integra.telessaude.ufrn.br/api/'
    #return 'http://127.0.0.1:8000/api' + path

########################################################################################################################
############################################METODOS DA UF###############################################################
########################################################################################################################
class acesso_barramento():

    def __init__(self, token):
       if len(token.split(' ')) == 2:
           self.token = token.split(' ')[1]
       else:
           self.token = token
       self.headers = {

            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Token %s' % self.token
        }

    def get_municipios_por_uf(self, uf, json=False):

        response = requests.get(_url('/uf/%s/municipios' %uf), headers=self.headers)
        data = response.json()
        UF = namedtuple('UF', data.keys())
        if (json == False):
            data = UF(**data)
        return data

    def get_uf(self, json=False):

        response = requests.get(_url('/uf/'), headers=self.headers)
        data = response.json()
        UF = namedtuple('UF', data.keys())
        if (json == False):
            data = UF(**data)
        return data

####################################################################################################################
###########################################METODOS DOS TIPOS#######################################################
####################################################################################################################
    def get_tipoestabelecimento(self, json=False):
        response = requests.get(_url('tipos/tipoestabelecimento/'), headers=self.headers)
        data = response.json()
        tipoestabelecimento = namedtuple('TipoEstabelecimento', data.keys())
        if (json == False):
            data = tipoestabelecimento(**data)
        return data

    def get_subtipoestabelecimento(self, json=False):
        response = requests.get(_url('tipos/subtipoestabelecimento/'), headers=self.headers)
        data = response.json()
        subtipoestabelecimento = namedtuple('SubTipoEstabelecimento', data.keys())
        if (json == False):
            data = subtipoestabelecimento(**data)
        return data

    def get_tipogestao(self, json=False):
        response = requests.get(_url('tipos/tipogestao/'), headers=self.headers)
        data = response.json()
        tipogestao = namedtuple('TipoGestao', data.keys())
        if (json == False):
            data = tipogestao(**data)
        return data

    def get_cbo(self, json=False):
        response = requests.get(_url('tipos/cbo/'), headers=self.headers)
        data = response.json()
        tipocbo = namedtuple('TipoCBO', data.keys())
        if (json == False):
            data = tipocbo(**data)
        return data

    def get_tipotelefone(self, json=False):
        response = requests.get(_url('tipos/tipotelefone/'), headers=self.headers)
        data = response.json()
        tipotelefone = namedtuple('TipoTelefone', data.keys())
        if (json == False):
            data = tipotelefone(**data)
        return data

    def get_tipoequipe(self, json=False):
        response = requests.get(_url('tipos/tipoequipe/'), headers=self.headers)
        data = response.json()
        tipoequipe = namedtuple('TipoEquipe', data.keys())
        if (json == False):
            data = tipoequipe(**data)
        return data

    def get_esferaadministrativa(self, json=False):
        response = requests.get(_url('tipos/esferaadministrativa/'), headers=self.headers)
        data = response.json()
        esferaadministrativa = namedtuple('EsferaAdministrativa', data.keys())
        if (json == False):
            data = esferaadministrativa(**data)
        return data

    def get_naturezaorganizacao(self, json=False):
        response = requests.get(_url('tipos/naturezaorganizacao/'), headers=self.headers)
        data = response.json()
        naturezaorganizacao = namedtuple('NaturezaOrganizacao', data.keys())
        if (json == False):
            data = naturezaorganizacao(**data)
        return data

    def get_vinculoempregaticio(self, json=False):
        response = requests.get(_url('tipos/vinculoempregaticio/'), headers=self.headers)
        data = response.json()
        vinculoempregaticio = namedtuple('VinculoEmpregaticio', data.keys())
        if (json == False):
            data = vinculoempregaticio(**data)
        return data

    def get_tipovinculoempregaticio(self, json=False):
        response = requests.get(_url('tipos/tipovinculoempregaticio/'), headers=self.headers)
        data = response.json()
        tipovinculoempregaticio = namedtuple('TipoVinculoEmpregaticio', data.keys())
        if (json == False):
            data = tipovinculoempregaticio(**data)
        return data

    def get_subtipovinculoempregaticio(self, json=False):
        response = requests.get(_url('tipos/subtipovinculoempregaticio/'), headers=self.headers)
        data = response.json()
        subtipovinculoempregaticio = namedtuple('SubTipoVinculoEmpregaticio', data.keys())
        if (json == False):
            data = subtipovinculoempregaticio(**data)
        return data

    def get_tipoinscricaoprofissional(self, json=False):
        response = requests.get(_url('tipos/tipoinscricaoprofissional/'), headers=self.headers)
        data = response.json()
        tipoinscricaoprofissional = namedtuple('TipoInscricaoProfissional', data.keys())
        if (json == False):
            data = tipoinscricaoprofissional(**data)
        return data

    def get_tipoespecialidade(self, json=False):
        response = requests.get(_url('tipos/tipoespecialidade/'), headers=self.headers)
        data = response.json()
        tipoespecialidade = namedtuple('TipoEspecialidade', data.keys())
        if (json == False):
            data = tipoespecialidade(**data)
        return data

    def get_tipoinscricao(self, json=False):
        response = requests.get(_url('tipos/tipoinscricao/'), headers=self.headers)
        data = response.json()
        tipoinscricao = namedtuple('TipoInscricao', data.keys())
        if (json == False):
            data = tipoinscricao(**data)
        return data

    def get_especialidadeambulatorial(self, json=False):
        response = requests.get(_url('tipos/especialidadeambulatorial/'), headers=self.headers)
        data = response.json()
        especialidadeambulatorial = namedtuple('TipoEspecialidadeAmbulatorial', data.keys())
        if (json == False):
            data = especialidadeambulatorial(**data)
        return data

    def get_fonteinformacao(self, json=False):
        response = requests.get(_url('tipos/fonteinformacao/'), headers=self.headers)
        data = response.json()
        fonteinformacao = namedtuple('TipoFonteInformacao', data.keys())
        if (json == False):
            data = fonteinformacao(**data)
        return data

    def get_tipoequipamento(self, json=False):
        response = requests.get(_url('tipos/tipoequipamento/'), headers=self.headers)
        data = response.json()
        tipoequipamento = namedtuple('TipoEquipamento', data.keys())
        if (json == False):
            data = tipoequipamento(**data)
        return data

    def get_especialidade(self, json=False):
        response = requests.get(_url('tipos/especialidade/'), headers=self.headers)
        data = response.json()
        tipoespecialidade = namedtuple('TipoEspecialidade', data.keys())
        if (json == False):
            data = tipoespecialidade(**data)
        return data

####################################################################################################################
############################################METODOS DA REGIAO DE SAUDE##############################################
####################################################################################################################
    def get_regiaosaude(self, json=False):
        response = requests.get(_url('/regiaosaude/'), headers=self.headers)
        data = response.json()
        regiaosaude = namedtuple('RegiaoSaude', data.keys())
        if (json == False):
            data = regiaosaude(**data)
        return data

########################################################################################################################
################################################METODOS DA REGIAO GEOGRAFICA############################################
########################################################################################################################
    def get_regiaogeografica(self, json=False):
        response = requests.get(_url('/regiaogeografica/'), headers=self.headers)
        data = response.json()
        regiaogeografica = namedtuple('RegiaoGeografica', data.keys())
        if (json == False):
            data = regiaogeografica(**data)
        return data

########################################################################################################################
############################################METODOS DO PROFISSIONAL#####################################################
########################################################################################################################



