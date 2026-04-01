# heictojpg

Free, private, browser-based HEIC to JPG converter. Conversion happens 100% client-side using WebAssembly — photos never leave the user's device.

## Deploy on Railway

### One-click deploy

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) and create a new project
3. Select **Deploy from GitHub repo** and choose this repository
4. Railway auto-detects the Nixpacks builder and `Procfile`
5. Set a custom domain: `heictojpg.pics`

### Manual CLI deploy

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Create project and deploy
railway init
railway up

# Set custom domain in Railway dashboard
# Project → Settings → Domains → Add heictojpg.pics
```

### Environment variables

No required environment variables. Railway auto-injects `PORT`.

Optional:
- `FLASK_ENV=production` (set automatically by gunicorn)

## Local development

```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

## Project structure

```
├── app.py              Flask app (serves pages only, zero file processing)
├── requirements.txt    flask, gunicorn
├── Procfile            gunicorn start command
├── railway.json        Railway Nixpacks config
├── sitemap.xml         SEO sitemap
├── robots.txt          Points crawlers to sitemap
└── templates/
    ├── index.html      Main converter (all logic inline, vanilla JS)
    ├── privacy.html
    ├── about.html
    ├── dmca.html
    └── contact.html
```

## Before going live

1. Replace `<!-- ADD SEARCH CONSOLE VERIFICATION TAG HERE -->` in `index.html`
2. Replace `<!-- ADD CONTACT EMAIL HERE -->` in all supporting pages
3. Add your AdSense publisher ID to the three ad slot comments:
   - `<!-- REPLACE WITH ADSENSE: leaderboard-top -->`
   - `<!-- REPLACE WITH ADSENSE: rectangle-post-convert -->`
   - `<!-- REPLACE WITH ADSENSE: mobile-sticky -->`
4. Add OG image at `https://heictojpg.pics/og-image.png` (1200×630)

## Stack

- **Frontend**: Single HTML file, vanilla JS, no frameworks
- **HEIC decoder**: [libheif-js](https://github.com/strukturag/libheif-js) via CDN (WebAssembly)
- **ZIP**: [JSZip](https://stuk.github.io/jszip/) via CDN
- **Backend**: Flask (serves HTML only)
- **Hosting**: Railway
