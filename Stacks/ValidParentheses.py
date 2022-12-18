def isvalid(s):
    our_stack = [];
    # hashmap to check
    closed_to_open = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in closed_to_open and not our_stack:
            print(our_stack)
            return False
        if ch not in closed_to_open:
            our_stack.append(ch)
            continue
        # if in hashmap then check if corresponding value is present at top of the stack
        if closed_to_open[ch] != our_stack[-1]:
            # return false if corr. val isnt present
            print(our_stack)
            return False
        # if corr.val is present pop corr. val from stack(probably the last val or topmost)
        our_stack.pop()
    # after looping through all ch in string if the stack isnt empty return false else true
    print(our_stack)
    return False if our_stack else True


ans = isvalid("(]")
print(ans)
