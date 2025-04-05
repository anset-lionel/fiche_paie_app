# app.py

import streamlit as st
from utils import extraire_fiches_par_identifiant

st.set_page_config(page_title="Extraction des fiches de paie", layout="centered")

st.title("🔍 Extraction des fiches de paie par numéro DN (CPS)")

# Upload du fichier PDF
pdf_file = st.file_uploader("📄 Déposez le PDF contenant toutes les fiches de paie :", type=["pdf"])

# Champ pour saisir l'identifiant
identifiant = st.text_input("🔢 Entrez le numéro DN (CPS) à rechercher")

if pdf_file and identifiant:
    if st.button("🚀 Extraire les fiches de paie"):
        with st.spinner("Analyse du document en cours..."):
            pdf_result = extraire_fiches_par_identifiant(pdf_file, identifiant)
            if pdf_result:
                st.success("✅ Extraction terminée ! Téléchargez le fichier ci-dessous.")
                st.download_button(
                    label="📥 Télécharger les fiches extraites",
                    data=pdf_result,
                    file_name=f"fiches_paie_{identifiant}.pdf",
                    mime="application/pdf"
                )
            else:
                st.warning("Aucune fiche de paie trouvée pour cet identifiant.")
else:
    st.info("Veuillez uploader un fichier et entrer un numéro DN pour commencer.")
