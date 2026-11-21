class Solution {
public:
    bool isPalindrome(std::string s) {
        std::string::iterator forward = s.begin();
        std::string::iterator backward = s.end();

        while (forward < backward) {
            if (!std::isalnum(*forward)) {
                forward++;
                continue;
            }

            if (!std::isalnum(*backward)) {
                backward--;
                continue;
            }
            std::cout << *forward << " ?? " << *backward << std::endl;
            std::cout << std::tolower(*forward) << " ?? " << std::tolower(*backward) << std::endl;
            if (std::tolower(*forward) != std::tolower(*backward)) return false;

            forward++;
            backward--;
        }

        return true;
    }
};
