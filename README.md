# back

1. `cd back`
2. Install python > 3.10
3. Install poetry `pip install poetry`
4. `cp .env.example .env` and edit db configuration
5. `poetry install`
6. `poetry shell`
7. `python manage.py migrate`
8. `python manage.py collectstatic`
9. `python manage.py createsuperuser` if need to login admin panel
10. `python manage.py runserver`

# front

```
cd front
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).