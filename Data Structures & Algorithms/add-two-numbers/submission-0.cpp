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
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;

        int carry = 0, sum = 0, digit = 0, l1Val = 0, l2Val = 0;
        
        while (l1 || l2 || carry != 0) {
            if (l1 != nullptr) {
                l1Val = l1->val;
            } else {
                l1Val = 0;
            }

            if (l2 != nullptr) {
                l2Val = l2->val;
            } else {
                l2Val = 0;
            }

            sum = l1Val + l2Val + carry;
            
            digit = sum % 10;
            carry = sum / 10;

            ListNode* newNode = new ListNode(digit);

            tail->next = newNode;
            tail = tail->next;

            if (l1 != nullptr) {
                l1 = l1->next;
            }             

            if (l2 != nullptr) {
                l2 = l2->next;
            }
        }

        return dummy->next;
    }
};
