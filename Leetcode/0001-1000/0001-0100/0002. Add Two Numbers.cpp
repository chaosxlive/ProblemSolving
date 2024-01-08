// https://leetcode.com/problems/add-two-numbers/

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

static auto fast_io = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
   public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode();
        int carry = 0;
        ListNode *it1 = l1, *it2 = l2, *it = head;
        while (it1 != nullptr && it2 != nullptr) {
            ListNode* temp = new ListNode((it1->val + it2->val + carry) % 10);
            carry = (it1->val + it2->val + carry) / 10;
            it->next = temp;
            it = it->next;
            it1 = it1->next;
            it2 = it2->next;
        }
        while (it1 != nullptr) {
            ListNode* temp = new ListNode((it1->val + carry) % 10);
            carry = (it1->val + carry) / 10;
            it->next = temp;
            it = it->next;
            it1 = it1->next;
        }
        while (it2 != nullptr) {
            ListNode* temp = new ListNode((it2->val + carry) % 10);
            carry = (it2->val + carry) / 10;
            it->next = temp;
            it = it->next;
            it2 = it2->next;
        }
        if (carry > 0) {
            it->next = new ListNode(carry);
        }
        return head->next;
    }
};