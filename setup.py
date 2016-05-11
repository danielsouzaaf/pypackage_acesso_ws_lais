from distutils.core import setup
install_requires = [
    'requests>=2.2.1',
    ]
setup(
    name = 'acesso_ws_lais',
    packages = ['acesso_ws_lais'], # this must be the same as the name above
    version = '0.1',

    description = 'Biblioteca para facilitar o acesso ao ws do LAIS.',
    author = 'Daniel Souza Affonso Ferreira',
    author_email = 'daniel.souza.af@gmail.com',
    url = 'https://github.com/danielsouzaaf/pypackage_acesso_ws_lais', # use the URL to the github repo
    download_url = 'https://github.com/danielsouzaaf/pypackage_acesso_ws_lais/tarball/0.1', # I'll explain this in a second
    keywords = ['lais', 'webservice', 'barramento'], # arbitrary keywords
    classifiers = [],
)