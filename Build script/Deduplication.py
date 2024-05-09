import json


def remove_duplicates(input_file, output_file, key_field):
    unique_values = set()

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            json_object = json.loads(line)

            # 检查是否指定了关键字段
            if key_field:
                value = json_object.get(key_field)
            else:
                value = json_object

            # 如果值不在集合中，将其写入新文件，并添加到集合中
            if value not in unique_values:
                json.dump(json_object, outfile)
                outfile.write('\n')
                unique_values.add(value)


# 使用示例
remove_duplicates('valid.jsonl', 'output3.jsonl', key_field='comments')
