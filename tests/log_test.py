import os.path
from click.testing import CliRunner
from app.cli import create_log_folder

clf = CliRunner()


def log_directory_test():
    response = clf.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True


#def log_file_test():
 #   assert os.path.exists(clf.log_file) == True


