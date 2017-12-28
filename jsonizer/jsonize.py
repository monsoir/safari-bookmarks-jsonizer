import os
import json
import sys, getopt

from .cleaner import Cleaner
from .extractor import Extractor

SOURCE_FILE = './Safari Bookmarks.html'
TARGET_FILE = './result.json'
TEMPERORY_FILE = './temp.html'

def native_bookmarks_to_json(source_path=None, output_path=None, ignore_folders=None, ignore_items=None, only_extract_folders=None, only_extract_items=None):
    if not source_path or not output_path:
            raise ValueError('source file and output_path are needed')
    cleaner = Cleaner(source_path=source_path, temp_path=TEMPERORY_FILE)
    cleaner.cleanup_source()

    # ignore_folders = ['Favorites', 'Bookmarks Menu', 'Reading List', 'iOS']
    # ignore_items =['腾讯微博']
    # only_extract_items = ['百合网']
    extractor = Extractor(cleaned_file_path=TEMPERORY_FILE, ignore_folders=ignore_folders, ignore_items=ignore_items, only_extract_items=only_extract_items)
    bookmarks = extractor.analyse_bookmarks_file()
    if bookmarks:
        result_json = json.dumps(bookmarks, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
        with open(output_path, 'w+') as f:
            f.write(result_json)
    
    os.remove(TEMPERORY_FILE)

def help():
    common_command1 = 'transform.py -i <input file> -o <output file>'
    common_command2 = 'transform.py -input <input file> -o <output file>'
    common_command = '\n'.join([common_command1, common_command2]) + '\n'

    other_option_prompt = 'other options:'
    other_option1 = '--ignore-folder: an array of folder names which and bookmarks in which will not appear in the result json file'
    other_option2 = '--ignore-items: an array of bookmark names which will not appear in the result json file'
    other_option3 = '--only-extract-folders: an array of folder names, bookmarks in which will be appear in the result json file, but not include the ones in subfolder name of which'
    other_option4 = '--only-extract-items: an array of bookmark names which will appear in the result json file'
    other_option = '\n'.join([other_option1, other_option2, other_option3, other_option4])

    return '\n'.join([common_command, other_option_prompt, other_option]) + '\n'

def main():
    # native_bookmarks_to_json()

    # 原始获取命令行参数
    # print(len(sys.argv))
    # print(str(sys.argv))

    # http://blog.luoyuanhang.com/2016/02/27/编写带命令行参数的-Python-程序/

    input_file = None
    output_file = None
    ignore_folders = None
    ignore_items = None
    only_extract_folders = None
    only_extract_items = None

    argvs = sys.argv[1:] # 第 0 个参数是文件名
    try:
        # 长选项可以单飞
        opts, args = getopt.getopt(argvs, 'hi:o:', ['input=', 'output=', 'ignore-folders=', 'ignore-items=', 'only-extract-folders=', 'only-extract-items='])
    except getopt.GetoptError:
        print('Error, command should be like:\n')
        print(help())
        sys.exit(2) # exit(2) 是什么意思

    if not opts:
        print('Error, command should be like:\n')
        print(help())
        sys.exit(2) # exit(2) 是什么意思
    
    # 没用到的 args 是什么
    for opt, arg in opts:
        if opt == '-h':
            print(help())
            sys.exit()
        elif opt in ('-i', '--input'):
            input_file = arg
        elif opt in ('-o', '--output'):
            output_file = arg
        elif opt == '--ignore-folders':
            ignore_folders = arg
        elif opt == '--ignore-items':
            ignore_items = arg
        elif opt == '--only-extract-folders':
            only_extract_folders = arg
        elif opt == '--only-extract-items':
            only_extract_items = arg

    native_bookmarks_to_json(
        source_path=input_file, 
        output_path=output_file, 
        ignore_folders=ignore_folders,
        ignore_items=ignore_items,
        only_extract_folders=only_extract_folders,
        only_extract_items=only_extract_items,
    )
    
    # print('input file:' + input_file)
    # print('output file:' + output_file)
    # print('ignore folders: ' + str(ignore_folders))
    # print('ignore items: ' + str(ignore_items))
    # print('only extract folders: ' + str(only_extract_folders))
    # print('onlu extract items: ' + str(only_extract_items))

if __name__ == '__main__':
    main()

'''
命令行工具参数解析方法：
1. sys.argv
2. getopt.getopt
3. argparse
'''