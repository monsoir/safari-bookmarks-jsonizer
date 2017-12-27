from bs4 import BeautifulSoup as BSS
from .model import Catelog, Category

class Extractor:
    cleaned_file_path = None
    ignore_folders = None # 忽略的文件夹
    ignore_items = None # 忽略的条目
    only_extract_folders = None # 只对这里面的文件夹进行抓取，不包括子文件夹，若值不为 None, 则会忽略 ignore_folders 的赋值
    only_extract_items = None # 只抓取匹配这些条目的书签，不会影响 ignore_folders 和 only_extract_folders 的赋值

    def __init__(self, cleaned_file_path=None, ignore_folders=None, ignore_items=None, only_extract_folders=None, only_extract_items=None):
        if not cleaned_file_path:
            raise ValueError('cleaned file is needed')

        self.cleaned_file_path = cleaned_file_path
        self.only_extract_items = only_extract_items

        if only_extract_folders:
            self.only_extract_folders = only_extract_folders
        else:
            self.ignore_folders = ignore_folders
        
        if only_extract_items:
            self.only_extract_items = only_extract_items
        else:
            self.ignore_items = ignore_items

    def should_add_catelog(self, catelog_name):
        if self.only_extract_items:
            return catelog_name in self.only_extract_items
        if self.ignore_items:
            return not (catelog_name in self.ignore_items)
        return True
    
    def should_add_category(self, category_name):
        if self.only_extract_folders:
            return category_name in self.only_extract_folders
        if self.ignore_folders:
            return not (category_name in self.ignore_folders)
        return True

    # 获取直接的标签
    def get_catelogs_of_node(self, a_node):
        dl = a_node.next_sibling.next_sibling # next.sibling 可能是 `\n`, 需要再 next_sibling
        addresses = dl.find_all('a', recursive=False)
        catelogs = []
        for address in addresses:
            if self.should_add_catelog(address.text):
                catelog = Catelog(address.text, address['href'])
                catelogs.append(catelog)

        return catelogs

    # 获取文件夹中的标签
    def get_categories_of_node(self, a_node):
        dl = a_node.next_sibling.next_sibling
        categories = []
        subH3s = dl.find_all('h3', recursive=False)
        for h3 in subH3s:
            if self.should_add_category(h3.text):
                category = self.bookmarks_of_node(h3)
                categories.append(category)

        return categories

    # 抓取入口
    def bookmarks_of_node(self, a_node):
        # 获取直接标签
        catelogs = self.get_catelogs_of_node(a_node)
        
        # 递归获取嵌套标签
        categories = self.get_categories_of_node(a_node)

        bookmark = Category(a_node.text, catelogs, categories)

        return bookmark

    def analyse_bookmarks_file(self):
        if not self.cleaned_file_path:
            raise ValueError('cleaned file is needed')

        with open(self.cleaned_file_path) as f:
            bsObj = BSS(f.read(), 'html.parser')
            html_node = bsObj.find('html')
            h3 = html_node.find('h3')

            catelogs = self.get_catelogs_of_node(h3)
            categories = self.get_categories_of_node(h3)
            bookmarks = Category(h3.text, catelogs, categories)

            return bookmarks