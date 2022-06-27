num = 123

print(f"[{num}]")

# numの後ろに@を書く、10文字表示
print(f"[{num:@<10}]")

# numの前に0を書く、9文字表示
print(f"[{num:0>9}]")

# numを大で挟む、8文字表示
print(f"[{num:大^8}]")
