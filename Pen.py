class Pen(object):
    def __init__(self, **kwargs):
        # the amount of ink
        self.ink_container_value = kwargs.get('ink_container_value', 1000)
        # size of the letter (font)
        self.size_letter = kwargs.get('size_letter', 1.0)
        # ink color
        self.color = kwargs.get('color', 'blue')

    def write(self, word):
        if not self.get_color:
            return ''
        size_of_word = len(word) * self.size_letter
        if size_of_word <= self.ink_container_value:
            self.ink_container_value -= size_of_word
            return word
        part_of_word = word[0: self.ink_container_value]
        self.ink_container_value = 0
        return part_of_word

    # ERROR!!! Bug
    def get_color(self):
        return 'blue'

    def check_pen_state(self):
        return self.ink_container_value > 0

    def do_something_else(self):
        print(self.color)


