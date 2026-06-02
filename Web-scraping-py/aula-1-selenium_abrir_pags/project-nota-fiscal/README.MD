# Sistema de Emissão de Notas Fiscais Automatizado

## 📌 Sobre o Projeto

Este projeto tem como objetivo automatizar o preenchimento e a emissão de notas fiscais utilizando Python, Selenium e Pandas.

Os dados dos clientes são armazenados em uma planilha Excel e o sistema realiza automaticamente:

* Leitura dos dados da planilha;
* Login no sistema web;
* Preenchimento dos campos do formulário;
* Emissão da nota fiscal;
* Download do arquivo XML gerado;
* Repetição do processo para todos os registros da planilha.

O projeto foi desenvolvido com fins educacionais para praticar automação de processos (RPA), manipulação de dados e testes de aplicações web.

---

## 🚀 Tecnologias Utilizadas

* Python
* Pandas
* Selenium WebDriver
* WebDriver Manager
* Excel (.xlsx)
* HTML
* CSS
* JavaScript

---

## 📂 Estrutura do Projeto

```text
📁 projeto-nota-fiscal
│
├── login.html
├── index.html
├── js/
│   └── script.js
├── css/
│   ├── style.css
│   └── login.css
├── NotasEmitir.xlsx
└── automacao.py
```

---

## ⚙️ Funcionalidades

### Sistema Web

* Tela de login
* Formulário de emissão de nota fiscal
* Geração automática de XML
* Download do arquivo da nota

### Automação Python

* Leitura de dados via Excel
* Login automático
* Preenchimento dos campos do formulário
* Emissão automática das notas
* Processamento em lote

---

## 📊 Conceitos Aplicados

Durante o desenvolvimento foram utilizados conceitos de:

* Automação Web
* RPA (Robotic Process Automation)
* Manipulação de dados com Pandas
* Leitura de planilhas Excel
* Interação com elementos HTML
* XPath
* Localização de elementos por Name, Class e ID
* Loops e Estruturas de Repetição
* Integração entre Front-end e Back-end

---

## 🎯 Objetivo

Demonstrar conhecimentos em automação de processos utilizando Python e Selenium, simulando um cenário real de emissão de notas fiscais em massa.

---

## 📸 Exemplo de Fluxo

1. Ler planilha Excel
2. Abrir navegador
3. Realizar login
4. Preencher formulário
5. Emitir nota fiscal
6. Baixar XML
7. Repetir para todos os clientes

---

## 👨‍💻 Autor

João Victor

Estudante de Análise e Desenvolvimento de Sistemas com foco em Python, Automação de Processos, Desenvolvimento Web e Análise de Dados.
