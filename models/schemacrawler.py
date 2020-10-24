import os

os.system("schemacrawler --server sqlite --database $HOME/Projects/pyist/models/istcore.sqlite --log-level=CONFIG --info-level=maximum --password= --command schema -o $HOME/Projects/pyist/models/diagram.png")

os.system("gwenview $HOME/Projects/pyist/models/diagram.png")
