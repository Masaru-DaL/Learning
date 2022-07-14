from color import ColorPalette

color_list = ["red","orange","blue","pink","black","green","purple","gold","brown"]
pal = ColorPalette(color_list)

col_gene = pal.get_colors()
print(col_gene)
print(type(col_gene))

# print(next(col_gene))

for all_color in col_gene:
  print(all_color)
