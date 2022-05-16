# <center> Проект: Анализ вакансий на hh.ru

<a id='Content'></a>
## Содержание
[1. Описание проекта](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Project-description)

[2. Данные](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Data)

[3. Цели](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Personal-goals)

[4. Описание методов](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Method-description)

[5. Результаты](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Results)

[6. Выводы](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Conclusions)

[7. Воспроизводимость кода](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Code-reproducibility)

<a id='Project-description'></a>
## 1. Описание проекта
Анализ заявок соискатетелей на работу из базы HeadHunter.ru за период с 2017 по 2019 года (выборочно) и выявление зависимостей между определёнными признаками указанными в резюме. Это работа сделана в рамках прохождения курса Data Science от компании Skill Factory. 

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)

<a id='Data'></a>
## 2. Данные
Данные представляют собой csv файл, выгруженный с обучающей платформы Skill Factory. Скачать файл можно [здесь](https://www.dropbox.com/s/pesgqxvl55010er/dst-3.0_16_1_hh_database.csv?dl=0).  
Каждая строка - резюме кандидата со следующими признаками:

* Пол и возраст кандидата
* Желаемая заработная плата
* На какую должность ищет работу кандидат
* Город соискателя, готов ли он к переезду и командировкам
* Занятость (полная, частичная и т. д.)
* График работы
* Опыт работы
* Последнее/нынешнее место работы
* Последняя/нынешняя должность
* Образование и ВУЗ
* Когда было обновлено резюме
* Наличие автомобиля

Всего в базе 44744 записи.  
Использовался также [csv файл](https://github.com/igorbakharev/skill_factory/blob/main/SF_project_1/data/ExchangeRates.csv) с курсами валют на даты соотвествующие датам указанным в резюме. Источник - также платформа Skill Factory.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)

<a id='Personal-goals'></a>
## 3. Цели

Цель проекта - улучшить свои навыки в программировании на Python и в анализе статистических данных из большого датасета, именно:

* Научиться обрабатывать и преобразовывать данные в дата фреймах
* Чистить данные
* Выявлять зависимости между признаками в данных
* Научиться пользоваться графическими инструментами Python для демонстрации зависимостей между данными и поиска закономерностей
* Научиться правильно и понятно оформлять свои выводы, сам проект и используемый код.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)

<a id='Method-description'></a>
## 4. Описание методов
В проекте использовальсь следующие библиотеки Python:

* *pandas*
* *numpy*
* *matplotlib*
* *seaborn*

Код пиcался в Jupiter Notebook в Visual Studio. Все задачи и ответы к ним содержатся [в самом ноутбуке](https://github.com/igorbakharev/skill_factory/blob/main/SF_project_1/Skill%20Factory%20Project%201.ipynb).

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)

<a id='Results'></a>
## 5. Результаты
В ходе выполнения проекта были выявлены определенные закономерности между признаками, которые подробно описаны и проиллюстрированы [в ноутбуке](https://github.com/igorbakharev/skill_factory/blob/main/SF_project_1/Skill%20Factory%20Project%201.ipynb). Исходные данные содержали пропуски и выбросы в некоторых столбцах, которые были исключены или заменены.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)

<a id='Conclusions'></a>
## 6. Выводы
Python обладает богатыми и удобными возможностями для работы с данными. Визуализация результатов может быть представлена с помощью нескольких графических библиотек с гибко настраиваемыми функциями.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)

<a id='Code-reproducibility'></a>
## 7. Воспроизводимость кода
Чтобы быть уверенным, что код можно воспроизвести в любое время, версии библиотек были сохранены в файле [requirements.txt](https://github.com/igorbakharev/skill_factory/blob/main/SF_project_1.requirements.txt). Чтобы перенести эти версии на свой компьютер, используйте команду **pip install -r requirements.txt**.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/SF_project_1/README.md#Content)