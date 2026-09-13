// Monetary amounts in this example are integer cents.
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal_cents) const {
        if (subtotal_cents < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal_cents + shipping_(subtotal_cents);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal_cents) { return subtotal_cents >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
    std::cout << "Express boundary: " << express.total(100) << '\n';
    try { static_cast<void>(standard.total(-1)); }
    catch (const std::invalid_argument&) { std::cout << "Negative subtotal rejected\n"; }
    try { const Checkout missing{ShippingRule{}}; }
    catch (const std::invalid_argument&) { std::cout << "Missing rule rejected\n"; }
}
