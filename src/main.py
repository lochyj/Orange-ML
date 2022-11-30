import Orange

data = Orange.data.Table("lenses");

for d in data[:3]:
    print(d);