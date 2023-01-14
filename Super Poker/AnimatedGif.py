""" AnimatedGIF - a class to show an animated gif without blocking the tkinter mainloop()

Copyright (c) 2016 Ole Jakob Skjelten <olesk@pvv.org>
Released under the terms of the MIT license (https://opensource.org/licenses/MIT) as described in LICENSE.md

Modified for super poker by supercaca 2022
"""
import random
import sys
import time
try:
	import Tkinter as tk  # for Python2
except ImportError:
	import tkinter as tk  # for Python3


class AnimatedGif(tk.Label):
	"""
	Class to show animated GIF file in a label
	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, original, gif_file, delay, enddelay):
		"""
		:param root: tk.parent
		:param gif_file: filename (and path) of animated gif
		:param delay: delay between frames in the gif animation (float)
		"""
		tk.Label.__init__(self, root)
		self.root = root
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04 (depends on the gif in question)
		self.enddelay = enddelay
		self.stop = False  # Thread exit request flag
		self.done = False
		self._num = 0
		self.original = original 

	def start(self):
		""" Starts non-threaded version that we need to manually update() """
		self.start_time = time.time()  # Starting timer
		self._animate()

	def stop(self):
		""" This stops the after loop that runs the animation, if we are using the after() approach """
		self.stop = True

	def _animate(self):
		try:
			self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
			if self.done:
				self.configure(image=self.original)
				self.stop_thread()
			else:
				self.configure(image=self.gif)
			self._num += 1
		except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
			self._num = 0
			self.done = True
			self.delay = self.enddelay
		if not self.stop:    # If the stop flag is set, we don't repeat
			
			self.root.after(int(self.delay*1000), self._animate)

	def start_thread(self):
		""" This starts the thread that runs the animation, if we are using a threaded approach """
		from threading import Thread  # We only import the module if we need it
		self._animation_thread = Thread()
		self._animation_thread = Thread(target=self._animate_thread).start()  # Forks a thread for the animation


	def start_angus(self):
		""" This starts the thread that runs the animation, if we are using a threaded approach """
		from threading import Thread  # We only import the module if we need it
		self.a_animation_thread = Thread()
		self.a_animation_thread = Thread(target=self.animateangus).start()

	def stop_thread(self):
		""" This stops the thread that runs the animation, if we are using a threaded approach """
		self.stop = True

	def _animate_thread(self):
		
		""" Updates animation, if it is running as a separate thread """
		self._num= len(self.gif_file)
		while self.stop is False:

			  # Normally this would block mainloop(), but not here, as this runs in separate thread
			try:
			   time.sleep(self.delay)
			   self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames

			   self.configure(image=self.gif)
			   self._num += 1
			except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
				self.blink = random.randint(0, 10000)
				if self.blink <50:            
					self._num = 0
				else:
					try:
						self.configure(image=self.original)

					except:
						sys.exit() 
			except:
				sys.exit()
	def animateangus(self):				
		""" Updates animation, if it is running as a separate thread """
		print("101")
		self._num= len(self.gif_file)
		while self.stop is False:
			  # Normally this would block mainloop(), but not here, as this runs in separate thread

			try:
				
				time.sleep(self.delay)
				self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
				self.configure(image=self.gif)
				self._num += 1

			except tk.TclError:
			     # When we try a frame that doesn't exist, we know we have to start over from zero
			    self._num = 0
				
			except RuntimeError:
				print("115")
				sys.exit()
			




