class Solution:
    def fib(self, n: int) -> int:
#
        dp=[-1]*(n+1)
        return self.fibo(n,dp)
    def fibo(self,n,dp):
        if n==0 or n==1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fibo(n-1,dp)+self.fibo(n-2,dp)
        return dp[n]
