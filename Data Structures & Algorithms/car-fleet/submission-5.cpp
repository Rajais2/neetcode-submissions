class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // Creating our stack
        stack<double> st;

        // Setting up to pair all cars' positions with their speed
        vector<pair<int, int>> cars;

        // Filling up our vector container full of pairs
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }

        // Sort the cars by their positions descending
        sort(cars.begin(), cars.end(),
             [](const pair<int,int>& a, const pair<int,int>& b) {
                 return a.first > b.first;
             });

        // Begin processing/traversing all the cars
        for (auto &car : cars) {
            // Calculating the time for the current car
            double time = (double)(target - car.first) / car.second;

            // If our stack is empty or the new car's time is greater
            // than the last car's, we need a new fleet so push the car
            // onto the stack 
            if (st.empty() || time > st.top()) {
                st.push(time); 
            } else {
                // Otherwise, we don't need a new fleet so we continue
                continue;
            }
        }

        // The number of fleets is equal to the size of our stack
        return st.size();
    }
};