all: gui run

gui:
	pyuic4 gui.ui > gui.py
	pyuic4 Command.ui > Command.py
	pyuic4 DisplayMode.ui > DisplayMode.py

run:
	python3 RTGraph.py

clean:
	rm -r *.pyc
	rm -r *.log*
	rm -r __pycache__
