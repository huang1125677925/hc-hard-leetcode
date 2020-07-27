class Solution:
    def widthOfBinaryTree(self, root):
        tobeprint=1
        nextlevel=0
        from collections import deque
        q=deque([root])
        root.val=1
        res=[]
        while q:
            now=q.popleft()
            res.append(str(now.val))
            if now.left:
                q.append(now.left)
                now.left.val=now.val*2
                nextlevel+=1
                
            if now.right:
                q.append(now.left)
                now.left.val = now.val * 2 + 1
                nextlevel+=1
                
            tobeprint-=1
            
            if tobeprint==0:
                tobeprint=nextlevel
                nextlevel=0
                res.append(',')
                
        res=''.join(res).split(',')
        m=1
        for l in res:
            if len(l)>=2:
                m=max(m,int(l[-1])-int(l[0]))
                
        
        return m

    if not root:
        return 0
    que = [[0, root]]  # 起始坐标为0，节点为根节点
    ans = 1
    while que:
        ans = max(ans, que[-1][0] - que[0][0] + 1)
        tmp = []  # 下一轮队列
        for i, q in que:
            if q.left:
                tmp += [[i * 2, q.lexiteft]]  # 坐标节点生成
            if q.right:
                tmp += [[i * 2 + 1, q.right]]
        que = tmp
    return ans


                