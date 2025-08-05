<img src="website/static/logo.png" width=35px align=right>

# Django-Vercel-Neon

## Description

This is a template repository that helps you to set up your Django+Vecel+Neon project.

## Usage
1. Create a new GitHub repo with using this repo as a template
2. Create project on [Vercel](https://vercel.app), link it to your GitHub repo
3. Add Neon DB as a Storage in your Vercel project
4. Clone your project & `nano .env`
5. Copy-paste Neon environmental variables from your Vercel project Settings into `.env` file
6. Cut `SECRET_KEY` from your own Django project's `settings.py` and paste it in `.env` for `SECRET_KEY`
7. Additionally, set up admin account with `ADMIN_LOGIN`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`. Otherwise, use default values:
    
    - Login: `admin`
    - Password: `securepassword123`

8. ```bash
   python3 manage.py migrate
   ```
Make sure `.env` is added to `.gitignore` and will not leak into production.

## License
This project is licensed under MIT License. Feel free to use this template. See [LICENSE](license) to learn more.
