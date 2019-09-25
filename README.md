#Setup

Create a virtual enviroment and install the dependencies in it with the following commands:

Linux:

* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt

Windows: 

* python -m venv venv
* \venv\Scripts\activate.bat
* pip install -r requirements.txt

or install the dependencies globally on your system-wide Python installation.


#Running

Run the following commands while still inside the virtual enviroment:

Supply the Application ID and password either through setting enviroment variables:

Linux:

* export ABBYY_APPID=YourApplicationId
* export ABBYY_PWD=YourPassword

Windows:

* set ABBYY_APPID=YourApplicationId
* set ABBYY_PWD=YourPassword

or supply them when calling the script (see the example below). 


```
python ocr.py [-h] [--application_id APPLICATION_ID] [--password PASSWORD]
                [--language LANGUAGE] [--textType TEXTTYPE]
                [--exportFormat EXPORTFORMAT] [--pdfPassword PDFPASSWORD]
                [--writeFormatting] [--writeRecognitionVariants] --inputFilename
                INPUTFILENAME
```

```
optional arguments:
  -h, --help            show this help message and exit
  --application_id APPLICATION_ID, -appid APPLICATION_ID
                        Application ID
  --password PASSWORD, -pwd PASSWORD
                        Application password
  --language LANGUAGE, -l LANGUAGE
                        Specifies recognition language of the document.
  --textType TEXTTYPE, -t TEXTTYPE
                        Specifies the type of the text on a page.
  --exportFormat EXPORTFORMAT, -e EXPORTFORMAT
                        Specifies the export format.
  --pdfPassword PDFPASSWORD, -pdfpwd PDFPASSWORD
                        Contains a password for accessing password-protected
                        images in PDF format.
  --writeFormatting, -xwf
                        Specifies whether to write XML formatting.
  --writeRecognitionVariants, -xwrv
                        Specifies whether to write XML recognition variants.
  --inputFilename INPUTFILENAME, -i INPUTFILENAME
```

#Examples 

#### Process a single file
```
python ocr.py -i foo.png -l Romanian -e txt,xml,pdfSearchable -xwf 
```

#### Process a single file and directly supplying credentials
```
python ocr.py -appid <APPID> -pwd <PWD> -i foo.png -l Romanian -e txt,xml,pdfSearchable -xwf 
```

#### Process all files in a directory
```
python ocr.py -i ./foo/ -l Romanian -e txt,xml,pdfSearchable -xwf 
```


#Links

* [List of available recognition languages](https://www.ocrsdk.com/documentation/specifications/recognition-languages/)
* [List of available export formats](https://www.ocrsdk.com/documentation/specifications/export-formats/)





