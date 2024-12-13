# Flood fill Algorithm

def dfs(self, image, i, j, c0, c1):
    if (i < 0 or j < 0 or i >= len(image) or j >= len(image[0])
            or image[i][j] != c0 or image[i][j] == c1):
        return

    image[i][j] = c1

    self.dfs(image, i, j - 1, c0, c1)
    self.dfs(image, i, j + 1, c0, c1)
    self.dfs(image, i - 1, j, c0, c1)
    self.dfs(image, i + 1, j, c0, c1)

def floodFill(self, image, sr, sc, newColor):
    self.dfs(image, sr, sc, image[sr][sc], newColor)
    return image