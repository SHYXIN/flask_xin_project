# Flask 社交博客项目

## 项目简介

这是一个使用 Flask 框架构建的 Web 应用程序。本项目提供了，具有社交功能的博客项目。

这个Flask项目具备多个主要功能模块。以下是对这些功能的详细说明：
1. 用户认证功能 (auth)

   - 注册 (Register): 用户可以通过注册页面创建新账户。注册后，通常会发送一封确认邮件以验证用户的电子邮件地址。
   - 登录 (Login): 用户可以通过登录页面输入用户名和密码进行身份验证。如果验证成功，用户将获得访问受限资源的权限。
   - 密码重置 (Password Reset): 如果用户忘记密码，可以通过提供注册时的电子邮件地址来请求重置密码。系统会发送一封带有重置链接的邮件。
   - 电子邮件验证 (Email Confirmation): 注册后，用户需通过点击发送到电子邮件中的确认链接来验证他们的电子邮件地址。
   - 视图和表单: 这一模块包含处理用户输入的表单类 (forms.py) 和处理用户请求的视图函数 (views.py)。

2. API接口 (api)
   - 身份验证 (Authentication): 处理API用户的身份验证请求，使用HTTPBasicAuth认证。
   - 用户管理 (User Management): 提供API端点，允许用户查询、更新、删除用户信息。
   - 帖子管理 (Post Management): 允许用户通过API创建、读取、更新和删除博客帖子。
   - 评论管理 (Comment Management): 类似于帖子管理，允许用户通过API对帖子进行评论，或管理评论。
   - 错误处理 (Error Handling): 定义API错误响应，确保API能够返回清晰的错误信息给客户端。

3. 主应用逻辑 (main)

   - 主页 (Home Page): 主模块通常包含应用的主页视图。在这个项目中，主页显示最新的帖子。
   - 用户资料 (User Profile): 提供用户个人资料查看和编辑功能。用户可以更新自己的信息，如用户名、简介等。
   - 帖子功能 (Post Management): 包括创建新帖子、编辑现有帖子、查看单个帖子的详细信息等功能。
   - 关注者管理 (Followers Management): 提供查看和管理关注者的功能。用户可以查看他们的关注者或他们关注的用户列表。
   - 表单处理 (Form Handling): 处理来自前端的表单提交，如创建或编辑帖子、评论等。

4. 数据库管理 (models.py, migrations/)

   - ORM (Object-Relational Mapping): 使用SQLAlchemy进行对象关系映射，将数据库表映射到Python类中。这些类定义了数据库的结构和关系。
   - 数据迁移 (Database Migrations): 使用Alembic进行数据库迁移管理。migrations/文件夹中的脚本用于在数据库结构变更时自动应用这些变更。

5. 邮件功能 (email.py)

   - 发送邮件: 系统通过Flask-Mail扩展发送电子邮件。例如，当用户注册或请求密码重置时，系统会发送相应的确认邮件或重置链接。
   - 邮件模板: templates/auth/email/中包含了HTML和纯文本格式的邮件模板，用于生成发送给用户的邮件内容。

6. 前端模板 (templates/)

   - Jinja2模板: 使用Jinja2模板引擎渲染动态HTML页面，模板文件如base.html, index.html, user.html等定义了网站的页面布局和内容。
   - Bootstrap集成: 使用Bootstrap前端框架为网站提供响应式设计和现代UI组件。

7. 测试功能 (tests/)

   - 单元测试 (Unit Testing): 项目包含一组测试用例，用于确保各个模块的功能正常工作。
   - API测试: 测试API端点的功能，验证身份验证、数据CRUD操作等是否按预期工作。
   - Selenium测试: 使用Selenium进行端到端测试，模拟用户在浏览器中的操作，验证应用的整体功能。

8. Docker支持
   - 容器化应用: Dockerfile定义了应用的Docker镜像，docker-compose.yml文件用于定义多个容器的运行配置，如Web应用、数据库等。
   - 环境变量管理: .env和.env-mysql文件用于配置敏感信息，如数据库连接字符串、电子邮件服务器配置等。这些文件不应提交到版本控制系统中。

9. 部署脚本 (boot.sh)
   - 自动化部署: boot.sh脚本可能用于自动化部署过程，启动应用服务器、运行数据库迁移并初始化权限表。

10. 分页和Markdown支持 (pagedown)
    - 分页: 使用Flask-Pagedown扩展，为帖子或评论提供分页功能，支持大篇幅文本的分页显示。
    - Markdown编辑: 提供Markdown格式的文本编辑和预览功能，用户可以在编写帖子或评论时使用Markdown语法。

这个项目整合了多个功能模块，提供了一个功能齐全的Web应用框架，涵盖了用户认证、API服务、前后端集成、数据库管理、测试和部署等方面。

## 主要目录结构

```
/project-root
│
├── app/                 # Flask 应用目录
│   ├── decorators.py
│   ├── email.py
│   ├── exceptions.py
│   ├── fake.py          # 生成假数据
│   ├── models.py        # 数据模型
│   └── __init__.py      # 应用初始化
│   │
│   ├── api/             # API实现
│   ├── auth/            # 用户注册登录
│   ├── main/            # 博客分享功能
│   ├── static/          # 静态文件
│   └── templates/       # 模板文件
│
├── migrations/          # 数据库迁移文件
├── requirements/        # python依赖包，不同环境依赖包
├── tests/               # 自动化测试文件
│
├── .env                 # 环境变量，敏感信息文件
├── .env-mysql           # docker部署时的mysql镜像，包括数据库设置、密码等
├── boot.sh              # docker部署时的启动脚本，初始化数据库表结构、初始化角色
├── config.py            # 项目配置文件
├── flasky.py            # 运行项目的主文件
├── docker-compose.yml   # docker部署，容器编排文件（MySql数据库）
├── Dockerfile           # docker部署时，python环境构建文件
```


## 环境设置

### 1. 克隆项目

    首先，克隆项目仓库到你的本地机器：

    GitHub
    ```bash
    git clone https://github.com/SHYXIN/flask_xin_project.git
    cd flask_xin_projec
    ```

    Gitee
    ```bash
    git clone https://gitee.com/theshyxin/flask_xin_project.git
    cd flask_xin_projec
    ```



## 2. 部署项目

部署项目有2种，本地部署和docker部署

### 2.1 本地部署

#### 环境要求

- Python 3.6、Python 3.7
- pip


1. 创建虚拟环境


    使用python3.7版本，建议你在虚拟环境中运行该项目，以便隔离不同项目的依赖。可以使用以下命令创建虚拟环境：

    ```bash
    # 使用 venv 创建虚拟环境
    python -m venv venv

    # 激活虚拟环境
    # 对于 Windows
    venv\Scripts\activate
    # 对于 macOS/Linux
    source venv/bin/activate
    ```

2. 安装依赖

    确保你在虚拟环境中，然后运行以下命令安装项目的所有依赖：

    ```bash
    pip install -r requirements/commont.txt
    ```

3. 配置环境变量

    你需要设置一些环境变量来配置项目运行。在项目根目录下新建或修改 `.env` 文件，写入如下内容：

    ```env
    FLASK_APP=flasky.py
    FLASK_CONFIG=development
    SECRET_KEY=your_strong_secret_key    # 修改
    MAIL_USERNAME=your_email@email.com   # 修改
    MAIL_PASSWORD=your_email_key         # 修改
    ```

4. 数据库迁移

    如果你的项目使用数据库，你需要运行迁移命令来设置数据库：
    因为本项目代码已经包含数据迁移的文件migrations/，可以直接运行代码，进行迁移

    ```bash
    flask db upgrade
    ```

5. 运行项目

    一切设置完毕后，可以使用以下命令启动 Flask 应用：

    ```bash
    flask run
    ```

    应用将会在 `http://127.0.0.1:5000/` 运行，你可以在浏览器中访问这个地址。


6. 添加虚拟文章和用户数据（非必须）

    按`ctrl + c`停止项目运行，通过faker模块生成数据。

    安装faker模块

    ```bash
    pip install faker==0.7.18
    ```

    使用`flask shell`运行app/fake.py文件，
    ```bash
    flask shell

    >>>from app import fake
    >>>fake.users()
    >>>fake.posts()
    ```

    重新启动项目

    ```bash
    flask run
    ```

### 2.2 使用 Docker 部署

#### 环境要求

- Docker
- Docker Compose


1. 配置环境变量

    在项目根目录下新建或修改 `.env` 文件，写入如下内容：

    ```env
    FLASK_APP=flasky.py
    FLASK_CONFIG=docker                  # 注意这里是docker
    SECRET_KEY=your_strong_secret_key    # 修改
    MAIL_USERNAME=your_email@email.com   # 修改
    MAIL_PASSWORD=your_email_key         # 修改
    DATABASE_URL=mysql+pymysql://flasky:xin_password@dbserver/flasky   # 注意xin_password为数据库密码，与.env-mysql保持一致
    ```

    在项目根目录下新建或修改 `.env-mysql` 文件，写入如下内容：

    ```env
    MYSQL_RANDOM_ROOT_PASSWORD=yes
    MYSQL_DATABASE=flasky
    MYSQL_USER=flasky
    MYSQL_PASSWORD=xin_password   # 注意xin_password为数据库密码，与.env保持一致
    ```




2. 启动服务：

   使用以下命令启动服务：

   ```bash
   docker-compose up -d
   ```

3. 访问应用：

   打开浏览器并访问 `http://127.0.0.1:8000`。


4. 添加虚拟文章和用户数据（非必须）

    运行docker ps，查看 flask_xin_project-flasky的容器ID

    ```bash
    $ docker ps

    CONTAINER ID   IMAGE                      COMMAND                   CREATED          STATUS                             PORTS                               NAMES
    3b5fbf050b73   flask_xin_project-flasky   "./boot.sh"               10 seconds ago   Up 7 seconds                       0.0.0.0:8000->5000/tcp              flask_xin_project-flasky-1
    2428e23cf806   mysql/mysql-server:5.7     "/entrypoint.sh mysq…"   10 seconds ago   Up 10 seconds (health: starting)   0.0.0.0:3306->3306/tcp, 33060/tcp   flask_xin_project-mysql-1
    ```

    可以看到是`3b5fbf050b73`，进入该容器

    ```bash
    docker exec -it  3b5fbf050b73 /bin/sh

    source venv/bin/activate
    pip install  faker==0.7.18

    ```


    ```bash
    flask shell

    >>> from app import fake
    >>> fake.users()
    ```


## 其他说明

- **测试**:运行测试的命令如下：

```bash
flask test
```

## 贡献指南

如果你想为本项目贡献代码，请遵循以下步骤：

1. Fork 本仓库
2. 创建你的 Feature 分支 (`git checkout -b feature/your-feature`)
3. 提交更改 (`git commit -am 'Add some feature'`)
4. 推送到分支 (`git push origin feature/your-feature`)
5. 打开一个 Pull Request

## 项目截图

首页

![首页](images/首页.png)

![管理员首页](images/admin_home.png)

![评论界面](images/comment.png)

![个人资料界面](images/profile.png)

## 打赏联系我

<img src="images/wechat1.jpg" width="270" height="300">
<img src="images/wechat2.jpg" width="270" height="300">

## 打个广告

本人编写的《Python Streamlit 从入门到实战——快速构建机器学习和数据可视化Web应用》一书，已由清华大学出版社，于2024年4月出版并发行，

需要的可以支持一下！嘻嘻

书籍链接：https://item.m.jd.com/product/14595352.html

![alt text](images/streamlit_book.png)

## 许可证

此项目遵循 MIT 许可证。详情请参考 `LICENSE` 文件。

