![Header](/img/EbwInvest.png "Ebw Invest")

# Gerador Automático de Carteira de investimento

Este projeto desenvolvido em python tem a finalidade de aplicar modelos de análise fundamentalista de grandes nomes do mercdado para composição de carteiras de investimentos de forma automatizada.

![Gerador](img/gerador_de_carteriras.gif)

## 🚀 Funcionalidade

Utilizando tecnicas de WebScraping e tratamento de dados, ranquea os ativos que melhor se enquadram nas regras de negógio dos modelos fundamentalistas aplicados.
Após a visualização das carteiras na tela do programa podemos salvar as informações em um arquivo pdf estilizado utilizando o botão <b>Salvar</b>.

### 📋 Pré-requisitos

Neste estágio passamos a utilizar o beautiful soup para buscar os dados na pagina [Fundamentus](https://www.fundamentus.com.br/resultado.php#), um dos mais famosos sites do genero.
Usamos um modelo de cabeçalho de pesquisa para o navegador FireFox e por tanto recomendamos a instalação do mesmo.
A demais, caso nescessário, deve-se fazer a instalação do pacote de bibliotécas listado no arquivo requirements.txt.
A instalação das bibliotecas pode ser feita com facilidade utilizando o comando:

```
pip install requirements
```
Geramos um arquivo executável [main](dist/main) que pode ser encotrado no diretório ./dist dete repositório para facilitar os testes.
Basta fazer as instalações necessárias executar o arquivo. 


### 🔧 Instalação

Como o Projeto está em faze inicial, ainda não possui um instalador. Faça um clone do repositório em sua máquina para copilalo através do módulo main.py. Ou executá-lo através do arquivo [main](dist/main) no diretório <i>/dist</i> deste repositório.

Após clonar o repositório em sua máquina execute os seguintes comandos no terminal:

```
pip install requirements
. magicform/bin/activate
python main.py
```
Uma interface simples será apresentada ao usuário, precione o botão gerar e defina o diretório onde será salvo o documento. 

## 📦 Implantação

Foi tomado o cuidado de produzir o projeto em módulos, de forma que possa ser fragmentado, adaptado e reaproveitado para novos projetos.

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Python](https://www.python.org/) - A linguagem que possibilitou tudo
* [Selenium](https://www.selenium.dev/) - Utilizado para conseguir os dados
* [Pandas](https://pandas.pydata.org/) - Usado para tratar os dados
* [FPDF](https://py-pdf.github.io/fpdf2/index.html) - usado para produzir o relatório final
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - utilizado para criar a interface gráfica

## ✒️ Autores

Idealizado e produzido por:

[Jhone Antonio](https://github.com/EbonyWizard4)

* **Problemática** - *Identificar e Processar*
* **Pesquisa** - *Extruturação*
* **Documentação** - *Elaboração e Viabilização*
* **Desenvolvimento** - *Criação e revisão*
* **Manutenção** - *Ampliação e escalabilidade*

Este projeto teve início ao aplicar os conhecimentos adquiridos em um evento promovido por [Breno Sulivan](https://www.youtube.com/@varos-programacao). Deixo aqui minha sinsera gratidão.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊

Editado por [Jhone Antonio](https://github.com/EbonyWizard4)