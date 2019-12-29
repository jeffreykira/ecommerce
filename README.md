# ecommerce-server

## Demo on Heroku
- swagger api doc
    https://live-ecommerce-server.herokuapp.com/api/v1/
- database admin interface
    https://live-ecommerce-server.herokuapp.com/admin/category/

## Server environment dependency
1. python3
2. pip install -r requirements.txt
3. docker
4. PostgreSQL


## Deploy to Heroku
可將 repo 裡指定目錄個別 deploy 到 Heroku

1. set remote
```
heroku git:remote -a {your_heroku_app_name}
```

2. push folder
```
git subtree push --prefix {your_folder} heroku master
```

- if subtree up-to-date but can't push
```
git push heroku `git subtree split --prefix {your_folder} master`:master --force

# then use step2
```
