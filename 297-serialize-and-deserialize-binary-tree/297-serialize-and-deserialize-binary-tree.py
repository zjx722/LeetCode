# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None:
            return ''
        
        queue = deque()
        
        queue.append(root)
        
        nodes = []
        
        while len(queue) > 0:
            
            cur_node = queue.popleft()
            if cur_node is None:
                nodes.append('null')
                continue
            else:
                nodes.append(str(cur_node.val))
                
            queue.append(cur_node.left)
            queue.append(cur_node.right)
            
        return ','.join(nodes)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if len(data) == 0:
            return None
        
        nodes = data.split(',')
        root_node = TreeNode(int(nodes[0]))
        
        
        queue = deque()
        queue.append(root_node)
        
        cur_pos = 1
        
        while len(queue) >0:
            cur = queue.popleft()
            
            if nodes[cur_pos] != 'null':
                cur.left = TreeNode(int(nodes[cur_pos]))
                queue.append(cur.left)
                
            cur_pos +=1
            
            if nodes[cur_pos] != 'null':
                cur.right = TreeNode(int(nodes[cur_pos]))
                
                queue.append(cur.right)
                
            cur_pos +=1
            
        return root_node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))