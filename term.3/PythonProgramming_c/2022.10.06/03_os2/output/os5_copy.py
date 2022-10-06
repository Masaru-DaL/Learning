import shutil

# ファイルをコピーする（すでに存在する時は上書きされる）
shutil.copyfile("os5.py", "./output/os5_copy.py")

# 指定フォルダに、同名でファイルをコピーする
# ※フォルダがない場合はファイルが作られる
shutil.copy("os5.py", "./output/")
