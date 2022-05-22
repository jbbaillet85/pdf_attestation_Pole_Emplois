import os


def createDirectory(name_directory: str = "pdf"):
    """_summary_

    Args:
        name_directory (str, optional): _description_. Defaults to "pdf".

    Returns:
        str: the path of the created folder
    """
    directory_current = os.getcwd()
    directory_parent = os.path.dirname(directory_current)
    path_directory_pdf = os.path.join(directory_parent, name_directory)
    if not os.path.exists(path_directory_pdf):
        os.mkdir(path_directory_pdf)
        return path_directory_pdf
    else:
        return path_directory_pdf


if __name__ == "__main__":
    createDirectory("pdf_sortie")
