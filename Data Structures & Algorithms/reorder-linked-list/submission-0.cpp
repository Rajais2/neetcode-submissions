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
    void reorderList(ListNode* head) {
        // Slow and fast pointer
        ListNode* slow = head, *fast = head;

        // Traverse the linked list
        while (fast && fast->next) {
            // Move the slow pointer once
            slow = slow->next;

            // Move the fast pointer twice
            fast = fast->next->next;
        }
        
        // After the loop, slow is now in the middle, meaning we make a new head and sever the link
        ListNode* secondHead = slow->next;
        slow->next = nullptr;

        // Begin to set up for list reversal
        ListNode* secondPrev = nullptr;
        ListNode* secondCurrent = secondHead;

        // Do the whole reversing process
        while (secondCurrent != nullptr) {
            ListNode* secondTemp = secondCurrent->next;

            secondCurrent->next = secondPrev;

            secondPrev = secondCurrent;
            secondCurrent = secondTemp;
        }

        // Rewiring the second head to point at the correct node
        secondHead = secondPrev;

        // Setting up two pointers to begin the merging process
        ListNode* p1 = head, *p2 = secondHead;

        // Traverse through both nodes simultaneously
        while (p1 != nullptr && p2 != nullptr) {
            // Store the next nodes in sequence for both lists
            ListNode* next1 = p1->next;
            ListNode* next2 = p2->next;

            // Rewire the next pointers
            p1->next = p2;
            p2->next = next1;
            
            // And move forward
            p1 = next1;
            p2 = next2;
        }
    }
};