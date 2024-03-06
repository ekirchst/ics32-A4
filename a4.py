# Evan
# ekirchst@uci.edu
# 59946460

from pathlib import Path
import ui as ui
import admin as admin
import user as user
# port = 168.235.86.101


if __name__ == "__main__":
    
    
    if ui.user() == 1:
        admin.start()
    else:
        user.comm_list()
        user.start()