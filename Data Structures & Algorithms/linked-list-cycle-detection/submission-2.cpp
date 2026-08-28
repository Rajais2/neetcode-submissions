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
    bool hasCycle(ListNode* head) {
        // Creating our slow and fast pointers
        ListNode* slow = head;
        ListNode* fast = head;

        // Begin the fast and slow pointer process
        while (fast && fast->next) {
            // Move the slow pointer up by one
            slow = slow->next;

            // Move the fast pointer up by two
            fast = fast->next->next;

            // If our pointers collide, there is a cycle
            if (fast == slow) {
                return true;
            }
        }

        // Otherwise, no cycle is detected
        return false;
    }
};
