import os
import requests
from time import sleep

# --- 1️⃣ Création du dossier ---
os.makedirs("images", exist_ok=True)

logos = {
    "javascript_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/500px-JavaScript-logo.png",
    "nodejs_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Node.js_logo.svg/1200px-Node.js_logo.svg.png",
    "vuejs_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/330px-Vue.js_Logo_2.svg.png",
    "tailwind_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/2560px-Tailwind_CSS_Logo.svg.png",
    "bootstrap_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/1200px-Bootstrap_logo.svg.png",
    "html_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/2048px-HTML5_logo_and_wordmark.svg.png",
    "css_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1452px-CSS3_logo_and_wordmark.svg.png",
    "java_logo.png": "https://assets.axopen.com/assets/uploads/226777_738cec596d.png",
    "swing_logo.png": "https://examples.javacodegeeks.com/wp-content/uploads/2012/12/java-duke-logo.jpg",
    "spring_logo.png": "https://cdn.worldvectorlogo.com/logos/spring-3.svg",
    "hibernate_logo.png": "https://cdn.freebiesupply.com/logos/large/2x/hibernate-logo-png-transparent.png",
    "python_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png",
    "flask_logo.png": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmD38KsMgEwahtWc_Nfs5ZVktP9dBc36MUZA&s",
    "sqlite_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Sqlite-square-icon.svg/1024px-Sqlite-square-icon.svg.png",
    "c_logo.png": "https://upload.wikimedia.org/wikipedia/commons/1/19/C_Logo.png",
    "linux_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1012px-Tux.svg.png",
    "git_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Git_icon.svg/1200px-Git_icon.svg.png",
    "github_logo.png": "https://cdn-icons-png.flaticon.com/256/25/25231.png",
    "gitlab_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/GitLab_icon.svg/1200px-GitLab_icon.svg.png",
    "rest_logo.png": "https://www.opc-router.de/wp-content/uploads/2020/05/REST_socialmedia.jpg",
    "oracle_logo.png": "https://www.progress.com/images/default-source/products/datadirect/dci-logos/oracle-database-logo.png?sfvrsn=b3bdff65_2",
}

# --- 3️⃣ En-tête pour éviter le blocage ---
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

# --- 4️⃣ Téléchargement avec gestion des erreurs ---
for filename, url in logos.items():
    path = os.path.join("images", filename)
    print(f"⏬ Téléchargement de {filename}...")
    try:
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        print(f"✅ {filename} téléchargé.")
    except Exception as e:
        print(f"❌ Erreur pour {filename} : {e}")
    sleep(1)  # petite pause entre les requêtes

print("\n🎉 Téléchargement terminé ! Vérifie le dossier 'images/'.")
