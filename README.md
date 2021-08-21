<h3 align="center">TRACKJOB SCRAPER</h3>
<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4kYAmTOCJhGnekVbO6ZitVjrA7DwfHcKe5wQq47u_T3TdjrSDtdfl1_uTpf3l4Ze7j8k&usqp=CAU" alt="Project logo"></a>
</p>


<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Lenguage](https://img.shields.io/badge/python-3.8.5-orange.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Manipulador e extrator de dados de 'adm.trackjob.com.br' feito em python
    <br> 
</p>

## 📝 Conteúdo

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Tips](#tips)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Pacote desenvolvido para obter relatórios e informações do trackojob de forma simples e rápida  

### Ambient <a name = "getting_started"></a>

 - Create a file .env with your authentication info:
 ```
 trackjob_username=<YOUR_USERNAME_HERE>
 trackjob_password=<YOUR_PASSWORD_HERE>
 ```

### Installing


- Using github

```
pip install git+https://github.com/Emanuel-AlmeidaDev/trackjob_scraper.git
```



## 🏁 Getting Started <a name = "getting_started"></a>
 - Using trackjob_scraper to get a report of passenger boarding between dates:

```
from trackjob_scraper import Trackjob
from decouple import config

username = config('trackjob_username')
password = config('trackjob_password')
trackjob = Trackjob(username, password)

relatorio = trackjob.get_report_passenger_boarding('10/08/2021', '11/08/2021')

```


## 🎈 Usage <a name="usage"></a>

Em desenvolvimento!


## 💡 Tips <a name="tips"></a>

### Save a report using:
```
    open('relatorio.xlsx', 'wb').write(relatorio)
```


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@Emanuel-AlmeidaDev](https://github.com/Emanuel-AlmeidaDev) - Idea & Initial work
