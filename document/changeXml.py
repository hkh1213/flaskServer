import glob
import os.path


def change():
    files = glob.glob("*.xml")
    for x in files:
        if not os.path.isdir(x):
            filename = os.path.splitext(x)
            try:
                os.rename(x, filename[0] + '.html')
            except:
                pass

change()
