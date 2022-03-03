class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2){
        int size1 = nums1.size();
        int size2 = nums2.size();
        int total = size1 + size2;
        
        int i = 0;
        int j = 0;
        int k = 0; 
        double median = 0.0;
        int median_index = 0;
        
        int f[total];
        
        auto array1 = nums1;
        auto array2 = nums2;
        
        while(i < size1 && j < size2){
            if(array1[i] <= array2[j]){
                f[k] = array1[i];
                i++;
            }
            else{
                f[k] = array2[j];
                j++;
            }
            k++;
        }
        
         while(i < size1){
            f[k] = array1[i];
            i++;
            k++;
         }
        
        while(j < size2){
            f[k] = array2[j];
            j++;
            k++;
        }
        
        if(total%2 == 0){
            median_index = (total/2)-1;
            int temp_index = median_index + 1;
            median = (f[median_index] + f[temp_index])/2.0;
        }
        else{
            median_index = (total)/2;
            median = f[median_index];
        }
        
        return median;
    }
    
};