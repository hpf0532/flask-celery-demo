# flask-celery-demo
这是一个使用celery结合flask的demo程序，基于python3.6
### 安装
#### 创建虚拟环境
```
cd flask-celery-demo/
virtualenv --python=/usr/bin/python3 venv
source venv3/bin/activate
```
#### 安装依赖
```
pip install -r requirments.txt
```
#### 修改配置

```
配置文件为test_api/settings.py
```

#### 启动celery
```
celery worker -A manage:celery -l debug
```
#### 启动flask
```
flask initdb  # 初始化数据库
flask run
```
#### 测试
```
curl http://127.0.0.1:5000/api/v1/
```

