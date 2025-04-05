# 📤 Application d'extraction de fiches de paie par numéro DN (CPS)

Cette application Streamlit permet d'extraire automatiquement les fiches de paie d'un employé à partir d'un PDF global contenant toutes les fiches de l'entreprise.

## 🧠 Fonctionnement

- Le fichier PDF source contient **toutes les fiches de paie de tous les employés**.
- Chaque fiche contient un identifiant personnel : le **numéro DN de la CPS**.
- L'utilisateur **uploade le fichier** et **renseigne l'identifiant**.
- L'application retrouve toutes les pages contenant cet identifiant et génère un **PDF individuel** avec uniquement les pages correspondantes.

## 🚀 Lancer l'application en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/tonutilisateur/fiche_paie_app.git
cd fiche_paie_app
