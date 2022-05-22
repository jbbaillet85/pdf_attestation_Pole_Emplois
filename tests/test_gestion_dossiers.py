import os
from config.gestion_dossiers import createDirectory


name_directory = "pdf_out"
directory_current = os.getcwd()
directory_parent = os.path.dirname(directory_current)
path_directory_pdf = os.path.join(directory_parent, name_directory)


def test_createDirectory():
    assert createDirectory(name_directory) == path_directory_pdf
