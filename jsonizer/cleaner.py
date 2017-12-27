class Cleaner:
    source_path = None
    temp_filepath = './.temp.html'

    def __init__(self, source_path=None, temp_path=None):
        if not source_path:
            raise ValueError('source file is needed')

        assert (temp_path != None), 'temp file is needed'

        self.source_path = source_path
        self.temp_filepath = temp_path

    def trim_DT(self, a_string):
        temp = a_string.replace(r'<DT><H3', '<H3')
        return temp.replace(r'<DT><A', '<A')

    def trim_p_after_DL(self, a_string):
        temp = a_string.replace(r'<DL><p>', '<DL>')
        return temp.replace(r'</DL><p>', '</DL>')

    # 删除无关行，且清除 <DT> <p>
    def cleanup_source(self):
        if not self.source_path:
            raise ValueError('source file is needed')

        assert (self.temp_filepath != None), 'temp file is needed'

        input = open(self.source_path) # 输入文件
        output = open(self.temp_filepath, 'w+') # 输出文件

        prefix = \
r'''<HTML>
  <H3 FOLDER>目录</H3>
  <DL>
'''
        output.write(prefix + '\n') # 添加一个顶级标签，便于递归
        for index, line in enumerate(input):
            if index in [0, 1, 2, 3, 4]:
                continue
            elif line == r'</HTML>':
                suffix = r'''
                    </DL>
                </HTML>
                '''
                output.write(suffix)
            else:
                line = self.trim_DT(line)
                line = self.trim_p_after_DL(line)
                output.write(line)

        input.close()
        output.close()
