import os

# "../input/<DATASET>/<SEQUENCE>/annotations/"
path_in = ""

idx = 0
for file in sorted(os.listdir(path_in)):
    os.rename(path_in+file,path_in+str(idx).zfill(6)+".json")
    idx=idx+1