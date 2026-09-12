#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>

using Context = std::unordered_set<std::string>;
struct Expression {
    virtual ~Expression() = default;
    virtual bool evaluate(const Context& context) const = 0;
};
class Role final : public Expression {
    std::string name_;
public:
    explicit Role(std::string name) : name_(std::move(name)) {}
    bool evaluate(const Context& context) const override { return context.contains(name_); }
};
class Both final : public Expression {
    std::unique_ptr<Expression> left_, right_;
public:
    Both(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {
        if (!left_ || !right_) throw std::invalid_argument("Missing expression");
    }
    bool evaluate(const Context& context) const override {
        return left_->evaluate(context) && right_->evaluate(context);
    }
};
int main() {
    const Both rule{std::make_unique<Role>("editor"), std::make_unique<Role>("verified")};
    std::cout << std::boolalpha << rule.evaluate(Context{"editor"}) << '\n';
    std::cout << rule.evaluate(Context{"editor", "verified"}) << '\n';
}
