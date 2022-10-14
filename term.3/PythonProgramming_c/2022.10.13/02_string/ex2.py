# 演習２
# matchで完全一致で国名を取り出します。
# 指定の正規表現を作ってください。
import re

# 国名一覧ファイルから、国名（英語）を一覧で取得
with open("country.txt", "r", encoding="UTF-8") as c_file:
    
    c_list = []
    read_list = c_file.readlines()
    for r in read_list:
        spl = r.split('#')
        c_list.append(spl[0].strip())
    # --------------------------------------------
    # 正規表現オブジェクトを作成
    
    # 正規表現指定
    # 演習２－１）
    # 指定条件：「M」で始まって、「S」で終わる（４個出れば正解）
    ptn = None

    # 演習２－２）
    # 指定条件：任意の５文字（２７個出れば正解）


    # 演習２－３）
    # 指定条件：母音(a,i,u,e,o)が３つ繋がった部分がある（２個出れば正解）



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
