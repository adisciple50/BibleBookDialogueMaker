# coded with the help of angels
import os
import re
import num2words


class Book:
    def __init__(self, name: str):
        self.name = name

    def _strip_amount_of_chapters(self,name :str):
        regex = ' [(].*[)]' # grab everything between paranthisees for name
        result = re.search(regex, name) # run the pattern search
        # replace the pattern search result with empty sting
        # effectively deleting the result from name
        print(result.group())
        return name.replace(result.group(), '')

    def _convert_numbers_to_alpha(self,name: str):
        regex = r'^\d'
        print(name)
        try:
            result = re.match(regex, name).group()[0]
        except AttributeError:
            result = ''
        if result is '':
            return name
        elif result is not '':
            return name.replace(result, num2words.num2words(int(result)))



    def _create_dialogue_file(self):
        contents = []
        if self.name == 'The Song of Solomon': # code smell - hard coding
            # add Song of songs to dialogue file
            contents.append('Song of Songs')
        contents.append(self.name)
        open('./dialogues/' + self.name + '.dialog', 'w').writelines(contents)


    def create_book(self):
        self.name = self._strip_amount_of_chapters(self.name)
        self.name = self._convert_numbers_to_alpha(self.name)
        self._create_dialogue_file()
        pass


class Bible:

    def __init__(self, book_list):
        self.book_list = book_list

    def create_all_dialogue_files(self):
        for line in self.book_list:
            line = line.rstrip()
            book = Book(str(line))
            print(line)
            book.create_book()
        pass


if __name__ == '__main__':
    os.mkdir('./dialogues')
    list = open('./books.list', 'r').readlines()
    bible = Bible(list)
    bible.create_all_dialogue_files()