# coded with the help of angels
import re
import num2words


class Book:
    def __init__(self, name: str):
        self.name = name

    def _strip_amount_of_chapters(self,name :str):
        reg = '[(].*[)]'
        return re.search(reg, name)

    def _convert_numbers_to_alpha(self,name: str):
        regex = r'^\d'
        result = int(re.match(regex, name).group()[0])
        return name.replace(str(result), num2words.num2words(result))



    def _create_dialogue_file(self):
        contents = []
        if self.name is 'The Song of Solomon':
            # add Song of songs to dialogue file
            contents.append('Song of Songs')
        contents.append(self.name)
        open('./dialogues/' + self.name + '.dialog').writelines(contents)


    def create_book(self):
        self.name = self._strip_amount_of_chapters(self.name)
        self.name = self._convert_numbers_to_alpha(self.name)
        self._create_dialogue_file(self)
        pass


class Bible:

    def __init__(self, book_list):
        self.book_list = book_list

    def create_all_dialogue_files(self):
        for line in self.book_list:
            book = Book(line)
            book.create_book()
        pass


if __name__ == '__main__':
    list = open('./books.list', 'r').read()
    bible = Bible(list)
    bible.create_all_dialogue_files()