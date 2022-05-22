from constantes import PATH_DIRECTORY_PDF_SOURCE, PATH_DIRECTORY_PDF_OUTPUT
from gestion_dossiers import createDirectory


createDirectory(PATH_DIRECTORY_PDF_SOURCE)
createDirectory(PATH_DIRECTORY_PDF_OUTPUT)
print(
    f"Merci de copier vos pdf dans le dossier {PATH_DIRECTORY_PDF_SOURCE}")
