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
git push heroku master

# OR if using a different branch than master:
git push heroku otherBranch:master
```

## Usage

Default API student key: `SUPERSTUD`
