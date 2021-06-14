# (sphinx-teste) | autodocmentação + hospedagem no readthedocs
teste de documentação automatica (veja como ficou o exemplo desse rep <https://sphinx-teste.readthedocs.io/pt/latest/>)

1. Parta de um repositório no github. Clone-o na sua máquina pessoal !
2. Se você já não tiver um ambiente para esse projeto, recomendo que o crie.
3. instale o sphinx e,opcionalmente , os temas rtd, caso queira:
```
conda install -c conda-forge sphinx
```
```
conda install -c conda-forge sphinx_rtd_theme
```
4. Entre no repositório e crie uma pasta docs:
```
mkdir docs
```
5. Abra-a no terminal, e execute o comando "sphinx-quickstart":
```
sphinx-quickstart
# Preencha da forma que lhe for mais convieniente, é possível apagar a pasta docs e recomeçar do início.
```
6. Algumas pastas e arquivos foram criadas. Encontre os arquivos conf.py e index.rst:
- No arquivo conf.py certifique-se/mude dos/os seguintes detalhes dentro do arquivo:
```
# Que o trecho semelhante a este abaixo (com os import) está descomentado
# que o os.path está apontando para o root do repositório (neste exemplo adaptado, geralmente já está apontando)
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Que no extensions, está ativada a auto-documentação
extensions = ['sphinx.ext.autodoc']

# que o tema html da documentação é o da sua preferencia
# https://www.sphinx-doc.org/en/master/usage/theming.html
html_theme = 'classic'

```
- No arquivo index.rst, abra-o e inclua o direcionamento para seu arquivo .py e altere a parte escrita como preferir:
```
.. example documentation master file, created by
sphinx-quickstart on Sun Aug  2 18:21:27 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Bem vindo a Documentacao (voce pode customizar isso)
====================================================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

.. automodule:: pets
 :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

```
7. Gere a documentação em html:
```
# rode o comando a partir da pasta "docs"
make html
```
8. Indo em build/html e abrindo o index.html, já é possível ver a documentação. Agora commite a documentação para o github:
```
# execute a partir da raiz do repositório
git add docs/
git commit -m "commit da documentação"
git push
```
## Hospedagem no readthedocs
9. Acesse <https://readthedocs.org/dashboard/>. Crie uma conta, caso não possua, anexe com o github (use o mesmo email)!
10. Selecione "importar um projeto". Importe seu projeto do GitHub (Nesta estapa, é necessário que o repositório estava público).
11. Preencha todas as informações e siga os passos. Ao final, seu repositório já estará disponivel.

Notas e próximos tutoriais.: Pode-se tornar o repositório privado logo em seguida? como adicionar módulos de um script principal ?
Estas anotações tiveram como base os seguintes tutoriais:
```
https://github.com/jhonatheberson/doc-sphinx
https://github.com/davidmorosini/python-sphinx-example
https://www.python.org/dev/peps/pep-0257/
https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
```

