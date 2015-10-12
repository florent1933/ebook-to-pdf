This project take ebooks from http://chimera.labs.oreilly.com and transform it into PDF to be printable!

It's in Python2

# Installation

```
virtualenv env
. env/bin/activate
pip install -R requirements.txt
```


# Launch

```
cd oreilly/
scrapy crawl oreilly
```


# Results

Observe all the .txt in the project (a .txt is a book). Enjoy it! :+1:

# Transform it into PDF

To transforme, you can use texoffice.atilla.org. TexOffice can transform the html in a PDF file thanks to LaTeX & Pandoc
