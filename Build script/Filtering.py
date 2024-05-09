import json
import re


# 数据清洗，删除多行注释
def remove_multiline_comments(code):
    # 使用正则表达式匹配多行注释，并将其替换为空字符串
    cleaned_code = re.sub(r'\"\"\".*?\"\"\"|\'\'\'.*?\'\'\'|/\*.*?\*/', '', code, flags=re.DOTALL)
    return cleaned_code



# 1. 打开test.jsonl文件并加载数据
with open('../valid.jsonl', 'r') as file:
    data = [json.loads(line) for line in file]

# 2. 打开或创建target.jsonl文件以写入数据
with open('valid.jsonl', 'w') as target_file:
    # 3. 将数据写入target.jsonl文件
    for entry in data:
        clean_code = remove_multiline_comments(entry['code'])
        lines_of_code = clean_code.splitlines()
        for index, line in enumerate(lines_of_code):
            if '#' in line and not line.strip().startswith('#'):
                parts = line.split('#', 1)
                Code = parts[0].strip()
                comments = parts[1].strip() if len(parts) > 1 else None
                if comments is not None and  "import" not in Code and not Code.strip().endswith(':') and 'pylint' not in comments and not any(char in comments for char in '"\''):
                    # result = {'comments': comments}
                    result = { 'code': Code,'comments': comments, 'lines': index + 1, 'repo': entry['repo'],
                              'path': entry['path'], 'func_name': entry['func_name'],
                              'original_string': entry['original_string'], 'language': entry['language'],
                              'Allcodes': entry['code'], 'code_tokens': entry['code_tokens'],
                              'docstring': entry['docstring'], 'docstring_tokens': entry['docstring_tokens']}
                    print(result)
                    json.dump(result, target_file)
                    target_file.write('\n')
