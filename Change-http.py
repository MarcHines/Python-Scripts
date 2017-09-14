import os
# Author: Marcus Hines : Change all http: links in files to //, while ignoring javascript. ie. http://example.com => //example.com


# Open the file, fix mixed content, then overwrite the file with correct text
def fix_mixed_content(filename):
    if not os.path.isdir(filename):
        javascript = False

        with open(filename, 'r+', encoding="utf8") as file:
            string_builder = []
            for line in file:
                if '<script' in line:
                    javascript = True

                if '</script' in line:
                    javascript = False

                if not javascript:
                    string_builder.append(line.replace('http://', '//'))
                else:
                    string_builder.append(line)

            file.seek(0)
            file.truncate()
            new_text = ''.join(string_builder)
            file.write(new_text)


def main():
    # Walk through all files, and directories at all levels after given directory
    for root, dirs, files in os.walk('./MarketingSherpaFiles', topdown=False):
        for name in files:
            fix_mixed_content(os.path.join(root, name))

        for name in dirs:
            fix_mixed_content(os.path.join(root, name))


if __name__ == '__main__':
    main()
