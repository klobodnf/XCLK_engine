class File:
	def __int__(self, filename = None, filesize = None):
		self.filename = filename
		self.filesize = filesize

tmp_file = File()
tmp_file.filename = "filename"
tmp_file.filesize = 15

print tmp_file.filename 

		
