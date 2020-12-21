import os
import time


cmd = """schemacrawler --server=sqlite --database=/home/cireng/Projects/pyist/models/istcore.sqlite\
         --command=schema --info-level=standard  --output-format=png --output-file=design.png	"""
cmd2 = """ristretto /home/cireng/Projects/pyist/design.png"""

os.system(cmd)
# time.sleep()
os.system(cmd2)