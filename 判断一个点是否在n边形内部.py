from matplotlib import path
p = path.Path([(0, 0), (1, 0), (1, 1)])
p.contains_points([(0.1, 0.1)])
