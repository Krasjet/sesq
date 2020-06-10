.PHONY: clean

syntax.css: sesq.py
	python -B sesq.py > syntax.css
	# remove background color
	sed -i "/^\.sourceCode  {/d" syntax.css
	# replace italic with medium weight
	sed -i "s/-style: italic/-weight: 500/g" syntax.css
	# strip comments
	sed -i "s/\/\*.*\*\///g" syntax.css
	echo ".sourceCode .hll { display: block; }" >> syntax.css

clean:
	rm -f syntax.css
