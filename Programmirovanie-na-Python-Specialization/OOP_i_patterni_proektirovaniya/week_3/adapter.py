# class Light:
#     def __init__(self, dim):
#         self.dim = dim
#         self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
#         self.lights = []
#         self.obstacles = []
#
#     def set_dim(self, dim):
#         self.dim = dim
#         self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
#
#     def set_lights(self, lights):
#         self.lights = lights
#         self.generate_lights()
#
#     def set_obstacles(self, obstacles):
#         self.obstacles = obstacles
#         self.generate_lights()
#
#     def generate_lights(self):
#         return self.grid.copy()
#
#
# class System:
#     def __init__(self):
#         self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
#         self.map[5][7] = 1  # Источники света
#         self.map[5][2] = -1  # Стены
#
#     def get_lightening(self, light_mapper):
#         self.lightmap = light_mapper.lighten(self.map)
#

class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def _get_objects_by_grid(self, descriptor, grid):
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == descriptor:
                    result.append((j, i))
        return result

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = self._get_objects_by_grid(1, grid)
        obstacles = self._get_objects_by_grid(-1, grid)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()
#
#
# light_object = Light((5, 5))
# print('grid -', light_object.grid)
# print('generate_lights -', light_object.generate_lights())
# light_object.set_lights([(4, 4)])
# print('generate_lights after set_lights -', light_object.generate_lights())
# print()
# system_object = System()
# print('system map - ', system_object.map)
# adapter = MappingAdapter(light_object)
# system_object.get_lightening(adapter)
# x = [[0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, -1, 0]]
# print((len(x), len(x[0])))
# for _ in range(len(x)):
#     try:
#         print('Один с координатами -', (_, x[_].index(1)))
#         print('Минус один с координатами -', (_, x[_].index(-1)))
#     except ValueError:
#         pass
# print('adapter obstacles -', adapter.adaptee.obstacles)
# print('adapter lights -', adapter.adaptee.lights)
# print('adater map dim -', (len(adapter.adaptee.grid), len(adapter.adaptee.grid[0])))
# print('system map dim -', (len(system_object.map), len(system_object.map[0])))
# print('system lightmap -', system_object.lightmap)
# print('adapte lightmap -', adapter.adaptee.grid)
