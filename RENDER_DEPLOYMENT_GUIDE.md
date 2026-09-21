# AccuTrack Deployment Guide for Render

This guide outlines how to deploy the **Accutrack** Django project to **Render** to obtain a live demo link.

---

## Pre-Deployment Checklist (Already Completed)

- [x] Fixed `STATIC_ROOT` and configured WhiteNoise in `accutrack_project/settings.py`.
- [x] Configured staticfiles collection (`python manage.py collectstatic --noinput`).
- [x] Configured media file serving via `re_path(r'^media/(?P<path>.*)$', ...)` in `accutrack_project/urls.py` so images load properly even with `DEBUG=False`.
- [x] Configured dynamic `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for `https://*.onrender.com`.
- [x] Enhanced WhatsApp contact form message pre-filling with name, email, and message.
- [x] Added `build.sh` build script.
- [x] Created `render.yaml` Blueprint.
- [x] Automated test suite verified (10/10 tests passed).

---

## Method 1: Deploy with Render Blueprint (Recommended)

1. Push this repository to **GitHub** or **GitLab**.
2. Log in to [Render Dashboard](https://dashboard.render.com/).
3. Click **New +** in the top right, then select **Blueprint**.
4. Connect your Accutrack repository.
5. Render will automatically detect `render.yaml` and configure:
   - **Service Name**: `accutrack-web`
   - **Runtime**: `Python`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn accutrack_project.wsgi:application`
   - **Environment Variables**: Automatically loaded.
6. Click **Apply**.
7. Render will build and deploy your project, giving you a live URL like:
   `https://accutrack-web.onrender.com`

---

## Method 2: Manual Web Service Setup on Render

If you prefer configuring the Web Service manually:

1. In the [Render Dashboard](https://dashboard.render.com/), click **New +** -> **Web Service**.
2. Select your Accutrack Git repository.
3. Configure the following fields:
   - **Name**: `accutrack-web`
   - **Language**: `Python 3`
   - **Branch**: `main` (or your active branch)
   - **Region**: Choose closest to your target audience (e.g. `Singapore` or `Frankfurt`).
   - **Build Command**: `./build.sh` (or `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`)
   - **Start Command**: `gunicorn accutrack_project.wsgi:application`
4. Expand **Advanced** -> **Environment Variables** and add:

| Key | Recommended Value | Notes |
|---|---|---|
| `PYTHON_VERSION` | `3.11.9` | Render standard stable Python runtime |
| `DEBUG` | `False` | Production mode |
| `SECRET_KEY` | *(Generate random string)* | Render can auto-generate |
| `ALLOWED_HOSTS` | `*` | Or your Render URL `accutrack-web.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://*.onrender.com` | Required for admin and form security |

5. Click **Create Web Service**.

---

## Database & Admin Access on Render

### Using SQLite for Demo (Zero Setup)
The SQLite database `db.sqlite3` is committed to the repository with initial data (slides, gallery images, contact info, and admin user).
- **Existing Admin Username**: `admin@accutrack`
- To reset or set a known admin password on Render:
  1. Go to your Render Web Service dashboard.
  2. Click the **Shell** tab on the left.
  3. Run:
     ```bash
     python manage.py createsuperuser
     ```
     or
     ```bash
     python manage.py changepassword admin@accutrack
     ```

### Upgrading to Render PostgreSQL (Optional)
If you require persistent data across redeploys:
1. In Render, click **New +** -> **PostgreSQL**.
2. Copy the **Internal Database URL**.
3. In your `accutrack-web` service settings, add the environment variable:
   `DATABASE_URL` = `<Render Internal PostgreSQL URL>`.
4. Render will automatically connect to PostgreSQL via `dj_database_url`.
