import argparse
import re

def modify_file(filename):
    # SQL Serverの主要なキーワード
    keywords = [
        'select', 'from', 'where', 'insert', 'update', 'delete', 'join',
        'inner', 'left', 'right', 'full', 'outer', 'group', 'by', 'order',
        'having', 'distinct', 'top', 'union', 'create', 'alter', 'drop',
        'table', 'index', 'view', 'procedure', 'trigger', 'key', 'primary',
        'foreign', 'use', 'exec', 'execute', 'like', 'between', 'values',
        'case', 'when', 'then', 'else', 'end', 'and', 'or', 'not', 'null',
        'in', 'exists', 'all', 'any', 'some', 'set', 'as', 'with', 'into',
        'database', 'schema', 'default', 'constraint', 'on', 'off', 'cursor',
        'declare', 'transaction', 'try', 'catch', 'merge', 'output', 'rowcount'
    ]

    # キーワードパターンのコンパイル（単語境界を明示的にチェック）
    keyword_pattern = re.compile(
        r'\b(' + '|'.join(re.escape(word) for word in keywords) + r')\b',
        re.IGNORECASE
    )

    try:
        with open(filename, 'r+') as file:
            content = file.read()

            # キーワードを大文字に置換
            content = keyword_pattern.sub(lambda match: match.group().upper(), content)

            file.seek(0)
            file.write(content)
            file.truncate()
        print(f"File '{filename}' has been modified.")
    except IOError:
        print(f"Error: Could not open the file '{filename}'.")

def main():
    parser = argparse.ArgumentParser(description="Convert SQL keywords to uppercase in an SQL file.")
    parser.add_argument("filename", help="The path to the SQL file to modify.")
    parser.add_argument("-m", "--modify", action="store_true", help="Modify the file directly (must be specified to make changes).")
    args = parser.parse_args()

    if args.modify:
        modify_file(args.filename)
    else:
        print("Please specify the '-m' option to modify the file.")

if __name__ == "__main__":
    main()
