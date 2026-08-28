class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
            // Building the final product result
            vector<int> productResult(nums.size(), 1);

            // Building the prefix products
            int prefixProducts = 1;
            for (int i = 0; i < nums.size(); i++) {
                productResult[i] = prefixProducts;
                prefixProducts *= nums[i];
            }

            int suffixProducts = 1;
            for (int i = nums.size() - 1; i >= 0; i--) {
                productResult[i] *= suffixProducts;
                suffixProducts *= nums[i];
            }

            return productResult;
    }
};
