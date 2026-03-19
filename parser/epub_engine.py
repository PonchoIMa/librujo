# Code to extract metadata from epubs
# coded with <3 by @ponchoima - http://ponchoima.dev
from ebooklib import epub
from zipfile import BadZipFile
import os, logging 

# get path
path = '../../bookshelf/'
names = []

# for .epub in path
# TODO: Try for wrong path
for file in os.listdir(path):
    if file.endswith('.epub'):
        try:
            book = epub.read_epub(path + file)
            name = book.get_metadata('DC', 'title')[0][0]
            names.append(name)
        except BadZipFile as e:
            print(f'Error found with {file}: {e}')
        except epub.EpubException as e:
            # TODO: Log error
            print(f'Error found with {file}: {e}')
        except KeyError as e:
            print(f'Error found with {file}: {e}')

for book in names:
    print(book)
