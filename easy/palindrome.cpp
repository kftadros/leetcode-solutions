class Solution {
public:
    bool isPalindrome(int x) {
        //Edge Cases
        if ( x < 0 ){return 0;}
        if (x != 0 && x % 10 == 0) return 0;
        if (x < 10) return 1;

        // find the size
        int divisor = 1;
        while (x / divisor >=10){
            divisor *=10;
        }

        while ( x > 0 ){
            int left = x / divisor;   // left  digit
            int right = x % 10;       // right digit

            if ( left != right ) {return 0;}

            // removes left and right digit
            x = ( x % divisor ) / 10;

            // since we removed 2 digits (left and right)
            divisor /= 100;

            //repeat
        }
        return 1;
    }
};