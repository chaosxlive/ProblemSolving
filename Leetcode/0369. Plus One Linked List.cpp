// https://leetcode.com/problems/plus-one-linked-list/

// Definition for singly-linked list.
// struct ListNode {
//     int val;
//     ListNode* next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode* next) : val(x), next(next) {}
// };

class Solution {
   public:
    ListNode* plusOne(ListNode* head) {
        ListNode *lastNotNine = nullptr, *result = nullptr, *ptr = head;
        while (ptr) {
            if (ptr->val != 9) {
                lastNotNine = ptr;
            }
            ptr = ptr->next;
        }
        if (lastNotNine) {
            result = head;
            lastNotNine->val++;
            ptr = lastNotNine->next;
        } else {
            result = new ListNode(1, head);
            ptr = head;
        }
        while (ptr) {
            ptr->val = 0;
            ptr = ptr->next;
        }
        return result;
    }
};