from subprocess import call

call(["find", ".", "-name", "'*.pyc'", "-delete"])
