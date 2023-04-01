# CREATE FOLDER MYUPLOAD FOR YOU IMAGE UPLOAD FILE
from flet import *
import shutil
import os
# NOW FOR COPY YOU FILE FROM SOURCE TO DESTINATION
# USE SHUTIL

def main(page:Page):


	# CHANGE THEME
	page.theme_mode = "light"


	def saveupload(e:FilePickerResultEvent):
		# NOW GET PATH YOU SOURCE IMAGE FOLDER
		for x in e.files:
			print(x.path)
			print(x.name)
			# THIS FOR GET CURRENT LOCATIO NOW
			you_copy = os.path.join(os.getcwd(),"myupload")
			shutil.copy(x.path,you_copy)
			page.update()



	file_picker =  FilePicker(
		# YOU RESULT FUNCTION
		on_result=saveupload
		)

	page.overlay.append(file_picker)

	page.add(
		Column([
			Text("YOU FILE SAVE IN MYUPLOAD",
				size=25,weight="bold"
				),
			ElevatedButton("upload file",
			on_click=lambda e:file_picker.pick_files()
				)
			])
		)

# NOW SET UPLOAD DIR YOU FOLDER NAME
flet.app(target=main,upload_dir="myupload")
