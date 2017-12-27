class Catelog:
    name = ''
    address = ''
    favicon = ''
    remark = ''

    def __init__(self, name, address, favicon = '', remark = ''):
        self.name = name
        self.address = address
        self.favicon = favicon
        self.remark = remark

class Category:
    title = ''
    catelogs = []
    categories = []

    def __init__(self, title, the_catelogs = None, the_categories = None):
        self.title = title
        self.catelogs = the_catelogs if the_catelogs is not None else []
        self.categories = the_categories if the_categories is not None else []