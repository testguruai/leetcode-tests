import pytest
import collections

class TestSolution:
    
    def test_network_delay_time_dfs(self):
        sol = Solution()
        times = [[2,1,1],[2,3,1],[3,4,1]]
        N = 4
        K = 2
        
        assert sol.networkDelayTime(times, N, K) == 2
        
    def test_network_delay_time_dijkstra(self):
        sol = Solution()
        times = [[2,1,1],[2,3,1],[3,4,1]]
        N = 4
        K = 2
        
        assert sol.networkDelayTime(times, N, K) == 2
        
    def test_network_delay_time_invalid_input(self):
        sol = Solution()
        times = [[2,1,1],[2,3],[3,4,2]]
        N = 4
        K = 2
        
        assert sol.networkDelayTime(times, N, K) == -1
        
    def test_network_delay_time_large_input(self):
        sol = Solution()
        times = [[i,i+1,1] for i in range(1, 10001)]
        times.append([1,10000,10000])
        N = 10000
        K = 1
        
        assert sol.networkDelayTime(times, N, K) == 10000


# to run the tests: pytest -q file_name.py