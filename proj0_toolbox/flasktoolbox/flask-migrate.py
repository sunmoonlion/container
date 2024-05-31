'''
You: 

- 在Flask中，如何使用Flask-Migrate库来管理数据库迁移

ChatGPT: 

- 在Flask中使用Flask-Migrate库来管理数据库迁移非常方便。下面是一些简单的步骤： 

1. **安装Flask-Migrate** ：

```复制代码
pip install Flask-Migrate
```

2. **配置数据库** ：
   在Flask应用程序中配置数据库连接。通常，你会使用SQLAlchemy来连接数据库。确保你的数据库连接字符串已经配置好。 
3. **初始化迁移环境** ：
   在你的Flask应用程序的根目录中，运行以下命令来初始化迁移环境：

```csharp
flask db init
```

4. **创建模型** ：
   使用SQLAlchemy创建你的数据库模型。 
5. **生成迁移脚本** ：
   运行以下命令来生成迁移脚本，它会比较当前数据库模型和迁移历史，然后生成一个适当的迁移脚本：

```arduino
flask db migrate -m "initial migration"
```

6. **应用迁移** ：
   应用迁移脚本到数据库中：

```复制代码
flask db upgrade
```

这些是基本的步骤，你可以根据需要进行修改和扩展。Flask-Migrate提供了丰富的功能来管理数据库迁移，例如回滚迁移、多个迁移路径等。
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://your_username:your_password@localhost/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

if __name__ == '__main__':
    app.run()


#然后依次运行以下命令来初始化和迁移数据库
# flask db init
# flask db migrate -m "Initial migration"
# flask db upgrade
