from abbyy import CloudOCR

import argparse
import os
from pathlib import Path


def ocr(input):
	with open(input, 'rb') as input_file:
		post_file = {input_file.name: input_file}
		result = ocr_engine.process_and_download(post_file, **parameters)
		for format, content in result.items():
			output_filename = '{name}.{extension}'.format(name='.'.join(input_file.name.split('.')[:-1]), extension=format)
			with open(output_filename, 'wb') as output_file:
				output_file.write(content.read())
				output_file.close()


if __name__=="__main__":
	parser = argparse.ArgumentParser(description='ABBYY Cloud OCR SDK')
	parser.add_argument('--application_id', '-appid', help='Application ID')
	parser.add_argument('--password', '-pwd', help='Application password')
	parser.add_argument('--language', '-l', help='Specifies recognition language of the document.')
	parser.add_argument('--textType', '-t', help='Specifies the type of the text on a page.')
	parser.add_argument('--exportFormat', '-e', default='txt', help='Specifies the export format.')
	parser.add_argument('--pdfPassword', '-pdfpwd', help='Contains a password for accessing password-protected images in PDF format.')
	parser.add_argument('--writeFormatting', '-xwf', const='true', action='store_const', help='Specifies whether to write XML formatting.')
	parser.add_argument('--writeRecognitionVariants', '-xwrv', const='true', action='store_const', help='Specifies whether to write XML recognition variants.')
	parser.add_argument('--inputFilename', '-i', help='', required=True)

	args = parser.parse_args()

	if 'ABBYY_APPLICATION_ID' in list(os.environ.keys()):
		application_id = os.environ['ABBYY_APPLICATION_ID']
	else:
		application_id = args.application_id

	if 'ABBYY_PASSWORD' in list(os.environ.keys()):
		password = os.environ['ABBYY_PASSWORD']
	else:
		password = args.password
	
	ocr_engine = CloudOCR(application_id, password)

	api_parameters = ['language', 'textType', 'exportFormat', 'pdfPassword', 'writeFormatting', 'writeRecognitionVariants']

	parameters = dict([x for x in args._get_kwargs() if x[0] in api_parameters and x[1] is not None])

	if "xml" not in parameters["exportFormat"]:
		parameters.pop("writeFormatting", None)
		parameters.pop("writeRecognitionVariants", None)

	if "writeFormatting" in parameters:
		parameters["xml:writeFormatting"] = parameters.pop("writeFormatting")
	if "writeRecognitionVariants" in parameters:
		parameters["xml:writeRecognitionVariants"] = parameters.pop("writeRecognitionVariants")

	if len(parameters["exportFormat"].split(",")) > 3:
		raise ValueError("ABBYY Cloud OCR SDK doesn't accept more than 3 export formats.")
	
	input = Path(args.inputFilename)

	if input.is_file():
		print("Processing: {0}".format(input))
		ocr(input)

	elif input.is_dir():
		for file in input.iterdir():
			if file.is_file():
				print("Processing: {0}".format(file))
				ocr(file)
