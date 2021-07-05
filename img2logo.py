import tkinter as tk
from tkinter import filedialog
from PIL import Image
#import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

class Img2lego:

	def __init__(self):
		self.filename = ""
		self.num_colours = 8
		self.imgsize = 32

	def set_filename(self, filename):
		self.filename = filename
		print("file name %s is set" % self.filename)

	def set_numberofcolours(self, num):
		self.num_colours = num
		print("Number of colours is set to %s" % self.num_colours)

	def set_imgsize(self, num):
		self.imgsize = num
		print("The image size is %dx%d" % (self.imgsize, self.imgsize))

	def creat(self):
		name_string = self.filename[:-4] + '_' + str(self.imgsize) + '_' + str(self.num_colours)
		
		im = Image.open(self.filename)
		print('original image size: ', im.size)
		im = im.resize( (self.imgsize, self.imgsize) )
		print('resized image size: ', im.size)

		arr = np.array(im)
		arr_h, arr_w, arr_c = arr.shape[0], arr.shape[1], arr.shape[2] 
		print(arr_h, arr_w, arr_c)
		
		cs = []
		for h in range(arr_h):
			for w in range(arr_w):
				cs.append ([arr[h][w][0], arr[h][w][1], arr[h][w][2]])

		kmeans = KMeans(n_clusters=self.num_colours, random_state=0).fit(cs)
		print(kmeans.labels_)
		print(kmeans.cluster_centers_)

		for h in range(arr_h):
			for w in range(arr_w):
				arr[h][w] = kmeans.cluster_centers_[kmeans.labels_[h*self.imgsize + w]]

		im = Image.fromarray(arr)
		im.save(name_string + '.jpg')


		from collections import Counter
		temp_dict = dict(Counter(kmeans.labels_))


		# reporting
		report_file = open(name_string + "_Lego_details.rpt", "w") 
		report_file.write('# Colours: \n')
		
		for i in range(self.num_colours):
			cc = kmeans.cluster_centers_[i]
			report_file.write('RGB-' + str(i) + ': [')
			for cc_i in cc:
				report_file.write(str(int(cc_i)) + ', ')
			report_file.write('] --> ' + str(temp_dict[i]) + '\n')

		report_file.write('\n\n# Map: \n')
		for h in range(arr_h):
			for w in range(arr_w):
				report_file.write(str(kmeans.labels_[h*self.imgsize + w]) + ', ') 
			report_file.write('\n')

		report_file.close() 


class App():
	def show_entry_fields(self):
		print("First Name: %s\nLast Name: %s" % (self.e1.get(), self.e2.get()))


	def browsefunc(self):
		filename = filedialog.askopenfilename(title = "Select file", filetypes=[("jpeg files","*.jpg")]) 
		self.img2lego.set_filename(filename)
		self.Filename_variable.set(filename)

	def startfunc(self):
		self.img2lego.set_numberofcolours(int (self.e1.get()))
		self.img2lego.set_imgsize(int(self.e2.get()))
		self.img2lego.creat()

	def __init__(self):

		self.img2lego = Img2lego()

		master = tk.Tk()
		master.title("Img2Lego")
		self.t1 = tk.Label(master, text="# of colours:")
		self.t1.grid(row=0, column=0)
		self.e1 = tk.Entry(master)
		self.e1.grid(row=0, column=1)
		self.e1.insert(0, "8")

		self.t2 = tk.Label(master, text="# of rows/columns")
		self.t2.grid(row=1, column=0)
		self.e2 = tk.Entry(master)
		self.e2.grid(row=1, column=1)
		self.e2.insert(0, "32")

		self.Filename_variable = tk.StringVar()
		self.Filename_variable.set("File")
		self.t3 = tk.Label(master, textvariable=self.Filename_variable)
		self.t3.grid(row=2, column=0)
		self.b1 = tk.Button(master,text="Browse",command=self.browsefunc)
		self.b1.grid(row=2, column=1)

		self.b2 = tk.Button(master, text='Start', command=self.startfunc)
		self.b2.grid(row=3, column=0)
		self.b3 = tk.Button(master, text='Quit', command=master.quit)
		self.b3.grid(row=3, column=1)

		tk.mainloop()

app = App()
