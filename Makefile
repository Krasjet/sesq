.PHONY: clean

syntax.css: sesq.py
	python -B sesq.py > syntax.css
	# remove background color
	sed -i "/^\.sourceCode  {/d" syntax.css
	echo ".sourceCode .hll { display: block; }" >> syntax.css

clean:
	rm -f syntax.css
