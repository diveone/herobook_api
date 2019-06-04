# Hero Book API
> Version: 1.0

Features:
- Hero stats API (read-only)

Please view the wiki for documentation about the endpoints.

### Local Development

```
git clone
cd herobookapi
pipenv install
createdb herobook_api
python3 manage.py migrate

python3 manage.py tests herobook_api/apps
```

Run server: `python3 manage.py runserver`

## Deployment to Heroku

```
git tag -a v1.1.0 -m "Introducing Auth"
git push heroku v1.1.0:master

# OR if using a different branch than master:
git push heroku otherBranch:master
```

To make manual changes on server use `heroku run` or use Heroku dashboard.

## Usage

Default API student key: `SUPERSTUDY`

Admin user: instructormaster
Admin password: iamtheone
