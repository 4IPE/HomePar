1.Создаем окружение либо через Conda или через python
Вводим в консоль:
Python - python -m your name venv (windows)
         python3 -m your name venv (windows)

Conda - conda create --name your name venv 
        conda activate your name venv (Для активации)
        conda deactivate (Для деактивации)

2.После того ,как установили окружение прописываем в консоле pip install -r requirements.txt
3.Если вы используете ПО на UNIX перейдите в result.html и cian.py и поменяться расположение (с такого формата homeparapp\\static\\homeparapp\\parsfile\\infocian.txt на homeparapp//static//homeparapp//parsfile//infocian.txt)




*Доп Информация 

template-папка с документами html
static - папка с динамически изменяемыми фалйами 
migrations - папка со всеми миграциями (миграции требуются при создании моделей(бд))
pars - это папка с парсером cian и avito