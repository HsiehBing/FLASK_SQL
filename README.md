### 說明:此repo是練習如何在FLASK中操作MySQL
## Linux MySQL安裝
1. 安裝 mysql mysql-server
```
yum install mysql mysql-server
```
2. 啟動
```
systemctl start mysqld
#可以透過netstat -tulnp | grep 'mysql'看有沒有啟動
```
3.設置密碼
預設並無設置密碼
可以直接啟動
```
mysql -u root
```
並由
```
exit
```
離開

設置密碼
```
mysqladmin -u root password 'password'
# 其中'password'為密碼
```
設置密碼後改以以下方式登入
```
mysql -u root -p
```
## MySQL簡易操作
可直接參考下方參考資料

## 其他
### 更新日誌
* 2023/4/6 第一次上傳

### 參考資料
* 鳥哥伺服器篇20.2.5
https://linux.vbird.org/linux_server/centos6/0360apache.php

* MySQL基本操作(含小範例)
https://ithelp.ithome.com.tw/articles/10216290

* MySQL語法彙整
http://note.drx.tw/2012/12/mysql-syntax.html

* Python Web Flask — Flask-Login登入系統實作
https://medium.com/seaniap/python-web-flask-flask-login%E7%99%BB%E5%85%A5%E7%B3%BB%E7%B5%B1%E5%AF%A6%E4%BD%9C-51c5ffda7924

* [Flask教學] Flask-SQLAlchemy 資料庫操作-ORM篇(二)
https://www.maxlist.xyz/2019/10/30/flask-sqlalchemy/

* Python Web Flask — 使用SQLAlchemy資料庫
https://medium.com/seaniap/python-web-flask-%E4%BD%BF%E7%94%A8sqlalchemy%E8%B3%87%E6%96%99%E5%BA%AB-8fc49c584ddb
