Are you interested to have your own Lego Art? Do you have a face picture?

![Lego art](Lego-Art.png)

This tool helps you to do so. Let's see a sample. This is the original image thatis going to become and Lego Art.

<img src="MarilynMonroe.jpg" alt="Sample original pic" width="300"/>

using the tool (browse the jpg file, set image size to 64 and the number of colours to 8), the previous image changes to:

![Converted version with 8 colours 64x64](MarilynMonroe_64_8.jpg)

The details for buying the legos will be reported, as a sample see here:

[detailed report for buying legos](MarilynMonroe_64_8_Lego_details.rpt)


One real sample:

<img src="Ghazal1.jpg" alt="input, RealSample" width="300"/>

<img src="Ghazal1_128_4.jpg" alt="output, RealSample"/>


# How to use the tool

<img src="img2lego.jpg" alt="img2lego"/>

1- Run the exe file (dist/img2lego.exe)
2- browse a jpg file
3- choose the right number of colors and image size
4- press start and see the saved file beside your input image

# run the code

	# Python 3.7 is tested
	pip3 install pillow matplotlib sklearn tornado scikit-learn  
	python3 img2logo.py

# How to generate the exe file

You can use one of these two commands (with/without cmd window):
	
no cmd console for IO:

	pyinstaller --onefile -w --icon=lego.ico  ./img2logo.py --hidden-import sklearn.neighbors.typedefs

with cmd console for IO:

	pyinstaller --onefile --icon=lego.ico  ./img2logo.py --hidden-import sklearn.neighbors.typedefs 

Due to the issue with ''sklearn'' library, we need to modify the ''img2lego.spec'' according to (https://stackoverflow.com/questions/49558126/pyinstaller-and-sklearn-ensemble-modulenotfounderror-no-module-named-sklearn). 

1- add these two lines to the spec file:

	from PyInstaller.utils.hooks import collect_submodules
	hidden_imports = collect_submodules('sklearn')

2- change the hiddenimports from:

	hiddenimports=['sklearn.neighbors.typedefs'],

to:

	-hiddenimports=hidden_imports,

Then regenerate the exe:

	pyinstaller img2lego.spec
