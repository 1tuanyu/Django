# Django
Django官方文档码一码

2.0中在settings里添加app之后，写好models数据库连接代码，用“python manage.py makemigrations books"创建tables,然后“python manage.py sqlmigrate books 0001”进行数据库连接。#“python manage.py migrate”暂时不明作用。

在python2中models使用“__Unicode__”，python3使用“__str__”，将project对象可视化。
