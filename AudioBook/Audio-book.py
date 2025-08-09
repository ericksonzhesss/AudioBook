#Importing Libraries
#Importing Google Text to Speech library
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF1

#Open file Path
pdf_File = open('name.pdf', 'rb') 

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
textList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)    
    textList.append(page.extractText())
   except:
       pass  text-align: center;
}
@media(max-width:767px){
  .eyes{
    display: flex;
    justify-content: center;
    align-items: center;
  }

#Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

#Set language to english (en)
language = 'en'

#Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myA.udio.sav.e("A.////
maim.u.dio.mp3.")/
.....
main
.....
margin 00
**** (main
///////////////
............
..................
////////////////////////////////////////////////////////
//////////////////////////
////////////
/////
/
///////
/
...........
.
.icon .line {
  background-color: #5290f9;
  height: 2px;
  width: 20px;
  position: absolute;
  top: 10px;
  left: 5px;
  transition: transform 0.6s linear;
}

.icon .line2 {
  top: auto;
  bottom: 10px;
}

nav.active .icon .line1 {
  transform: rotate(-765deg) translateY(5.5px);
}

nav.active .icon .line2 {
  transform: rotate(765deg) translateY(-5.5px);




////////////////////////////////////////////////////////////////////

