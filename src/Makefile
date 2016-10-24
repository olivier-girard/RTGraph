all: gui run

gui:
	pyuic4 LiveWindow.ui > LiveWindow.py
	pyuic4 CommandWindow.ui > CommandWindow.py
	pyuic4 SavedWindow.ui > SavedWindow.py
	pyuic4 PosterWindow.ui > PosterWindow.py
	pyuic4 AutoWindow.ui > AutoWindow.py

run:
	python3 RTGraph.py

clean:
	rm -r *.pyc
	rm -r *.log*
	rm -r __pycache__
