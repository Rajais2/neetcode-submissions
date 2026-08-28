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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Creating a dummy node and tail to create another list
        ListNode* dummyNode = new ListNode();
        ListNode* tail = dummyNode;

        // Begin traversing both lists
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                tail->next = list1;
                tail = tail->next;
                list1 = list1->next;
            } else {
                tail->next = list2;
                tail = tail->next;
                list2 = list2->next;
            }
        }

        if (list2 == nullptr && list1 != nullptr) {
            tail->next = list1;
            tail = tail->next;
        } else if (list1 == nullptr && list2 != nullptr) {
            tail->next = list2;
            tail = tail->next;
        }

        return dummyNode->next;
    }
};
