import pytest

@pytest.fixture
def image():
    return [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def test_floodFill_dfs(image):
    sol = Solution()
    assert sol.floodFill(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

def test_floodFill_dfs_same_color(image):
    sol = Solution()
    assert sol.floodFill(image, 1, 1, 1) == image

def test_floodFill_bfs(image):
    sol = Solution()
    assert sol.floodFill(image, 1, 1, 2) == sol.floodFill_bfs(image, 1, 1, 2)