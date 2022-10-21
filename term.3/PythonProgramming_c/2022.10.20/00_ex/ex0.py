import re

# 国名一覧ファイルから、国名（英語）を一覧で取得
with open("country.txt", "r", encoding="UTF-8") as c_file:

    c_list = []
    read_list = c_file.readlines()
    for r in read_list:
        spl = r.split("#")
        c_list.append(spl[0].strip())

# 演習０（前回の復習）
#
# 国名リストから該当する国名の一覧を取得します。（前方一致）
# 指定の正規表現オブジェクトを作成して結果を確認してください。

# 例）指定条件：すべて（２７１個出れば正解）
ptn = re.compile(".*", re.I)

# 演習０－１）
# 指定条件：Aで始まって、Aで終わる（１３個出れば正解）
ptn = re.compile("^A.*A$", re.I)

# 演習０－２）
# 指定条件：どこかにXを含む（２個出れば正解）
ptn = re.compile(".*X.*", re.I)

# 演習０－３）
# 指定条件：「LAND」または「LANDS」で終わる（３１個出れば正解）
ptn = re.compile(".*(LANDS|LAND)$", re.I)
ptn = re.compile(".*LANDS?$", re.I)

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
