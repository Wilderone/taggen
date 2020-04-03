class HTML:
    """"Create html file in path from argument. Use 'print' or None argument to print result"""""
    def __init__(self, output=None):
        self.output = output
        self.child = []
        self.result_self = '<HTML> \n </HTML>'

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        childs = f'\t'
        if self.output is not None and 'print':
            with open(self.output, 'w') as f:
                if self.child:
                    for row in self.child:
                        childs += row
                    f.write(f'<HTML> \n \t{childs} \n</HTML>')
                else:
                    f.write(self.result_self)

    def __iadd__(self, other):
        self.child.append(str(other))
        return self


class TopLevelTag:
    """Create TopLevelTag, only can be pair-tag, may have STRING of classes in argument, STRING of ID.
    name by default is div
    syntax is TopLevelTag(name='div', class_='class1 class2', id_='id', text='text')
    dont forget _ after class and id"""

    def __init__(self, **kwargs):
        self.child = []  # list of childs for += operations
        self.attr = kwargs

        self.name = ''
        self.class_ = ''
        self.id_ = ''
        self.text = ''
        for key, value in kwargs.items():
            if 'name' in key:
                self.name = value
            if 'class' in key:
                self.class_ = f' class="{value}"'
            if 'id' in key:
                self.id_ = f' id="{value}"'
            if 'text' in key:
                self.text = value


        self.tag_close = f'</{self.name}>'
        self.tag_result = f"\n<{self.name}{self.class_}{self.id_}>\n{self.text} \n{self.tag_close}"



# function for returning tag with or without child, used in __str__ and __exit__
    def check_for_child(self):
        if self.child:
            childs = ''
            for row in self.child:
                childs += row
            return ''.join(f"\n<{self.name}{self.class_}{self.id_}> \n{self.text}\n\n{childs}\n\n\n{self.tag_close}")
        else:
            return self.tag_result

    def __str__(self):
        return self.check_for_child()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return self.check_for_child()


    def __iadd__(self, other):
        self.child.append(str(other))
        return self

    # trying

    # def attrib(self):
    #     attribute_string = ''
    #     for key, value in self.attr.items():
    #         attribute_string.join(f'{key}="{value}"')
    #     return attribute_string


class Tag(TopLevelTag):

    """Low-level tag, same as TopLevelTag, but may have:
     is_single=True/False (True by default) - if you need tag without close-pair (img, br)
     src='text'(empty by default) - for img, script, etc
     Syntax is Tag(name='img', is_single=True, src = './img/1.png', class_='class', id_='id', text='text')
     You can skip any of arguments
     dont forget _ after class and id"""

    def __init__(self, is_single=False, src='', **kwargs):
        super().__init__(**kwargs)

        for arg, value in kwargs.items():
            if 'text' in arg:
                self.text = f'{value}'
            else:
                self.text = ''

        if is_single:
            self.tag_close = ''
        else:
            self.tag_close = f'</{self.name}>'
        if src:
            self.src = f' src="{src}"'
        else:
            self.src = src



    def __str__(self):
        self.tag_result = f"\n<{self.name}{self.src}{self.class_}{self.id_}> {self.text} {self.tag_close}"
        return self.check_for_child()

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #    # self.tag_result = f"\n<{self.name} {self.src} {self.class_} {self.id_}> {self.text} {self.tag_close}"
    #     return self.tag_result










