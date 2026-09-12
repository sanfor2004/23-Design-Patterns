#include <iostream>

class Metrics {
    int requests_ = 0;
    Metrics() = default;
public:
    Metrics(const Metrics&) = delete;
    Metrics& operator=(const Metrics&) = delete;
    static Metrics& instance() {
        static Metrics metrics;
        return metrics;
    }
    void record() { ++requests_; }
    int requests() const { return requests_; }
};
int main() {
    auto& first = Metrics::instance();
    auto& second = Metrics::instance();
    first.record();
    second.record();
    std::cout << "Same instance: " << std::boolalpha << (&first == &second) << '\n';
    std::cout << "Requests: " << first.requests() << '\n';
}
