
# Парсер авито
Скрипт находит бесплатные обьявления на авито  по ключевым словам, сохраняет результат в виде JSON в файл
***

## Стек
Python3, selenium, fake_useragent
***

## Как запустить парсер
* В корне проекта создаем файл .env в файле создаем константу URL и туда добавляем ссылку на авито с выбранной категорией
    
    ### пример
	`
	URL = https://www.avito.ru/arzamas/bytovaya_elektronika?cd=1&q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE
	`

* В  конце файла parser.py добавляем ключевые слова

    `
    AvitoParse(url=url, count_page=3, items=['<ключевое слово>', '<ключевое слово>']).parse()
    `

* Устанавливаем драйвер Google Chrome в папку chromedriver

https://chromedriver.storage.googleapis.com/index.html?path=110.0.5481.77/


* Клонируем репозиторий к себе на пк

    `
    git clone git@github.com:EgorFedotov/parser_avito.git
    `


* Устанавливаем и активируем виртуальное окружение  

	`
    py -3.10 -m venv venv
    `
    `
    source venv/Scripts/activate
    `
   
   
* Устанавливаем зависимости из файла req.txt
 
	`
    pip install -r req.txt
    `
 


* запускаем парсер, переходим в директорию chromedriver

    `
    cd chromedriver
	python parser.py
    `
***
