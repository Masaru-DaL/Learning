import re

# 国名一覧ファイルから、国名（英語）を一覧で取得
with open("country.txt", "r", encoding="UTF-8") as c_file:
    
    c_list = []
    read_list = c_file.readlines()
    for r in read_list:
        spl = r.split('#')
        c_list.append(spl[0].strip())
# --------------------------------------------
# （詳細はこちら）
# https://docs.python.org/ja/3/library/re.html
# （分かりやすいかもしれないサイト）
# https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3

# 正規表現オブジェクトを作成
# 「re.I」をフラグとして２つ目の引数に指定すると、
# 大文字小文字の差を無視する

# 正規表現指定
ptn = re.compile(".*", re.I)
#ptn = re.compile("japan", re.I)
#ptn = re.compile("pa", re.I)
#ptn = re.compile(".*j.*", re.I)
#ptn = re.compile(".+j.+", re.I)
#ptn = re.compile("^j.*", re.I)
#ptn = re.compile(".*n$", re.I)
#ptn = re.compile("^[jqz].*", re.I)
#ptn = re.compile("^(j|q|z).*", re.I)
#ptn = re.compile("^[jap]{3}.*", re.I)

# --------------------------------------------
# 正規表現の条件に一致した国名を表示
# オブジェクト.group()で文字列として取得できる
m_list = []
for c in c_list:
    res = ptn.match(c)
    if res != None:
        m_list.append(c)
print(f"matchで一致した数：{len(m_list)}")
print(m_list)

m_list = []
for c in c_list:
    res = ptn.search(c)
    if res != None:
        m_list.append(c)
print(f"searchで一致した数：{len(m_list)}")
print(m_list)
