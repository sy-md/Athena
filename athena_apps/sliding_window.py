def maxSlidingWindow(nums, k):
        output = []
        maxQueue = deque()

        i,j = 0,0
        n = len(nums)

        while(j < n):
            #Remove all elements from deque that are smaller than current element at index j
            while(len(maxQueue) > 0 and nums[j] > maxQueue[-1]): maxQueue.pop()  
                
            #And once removed, then put the j index element in the Queue
            maxQueue.append(nums[j])

            #Check Window size
            if(j - i + 1 < k): j += 1
            #If Window size = k
            else:
                #Put the maximum element in this window in the output
                output.append(maxQueue[0])
                
                #Before sliding the window, check if the element we are not going to include in next window is max element or not
                # It it is the max element, that means we remove it from deQue as well
                if(nums[i] == maxQueue[0]): maxQueue.popleft()
                #Slide the window
                i += 1
                j += 1

        return output

if __name__ == '__main__':
    data = [1,3,-1,-3,5,3,6,7]
    k = 3
    maxSlidingWindow(data,k)




