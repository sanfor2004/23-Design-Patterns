#include <iostream>
#include <memory>
#include <string_view>

struct Button {
    virtual ~Button() = default;
    virtual std::string_view paint() const = 0;
};
struct Panel {
    virtual ~Panel() = default;
    virtual std::string_view paint() const = 0;
};
struct DarkButton final : Button {
    std::string_view paint() const override { return "dark button"; }
};
struct DarkPanel final : Panel {
    std::string_view paint() const override { return "dark panel"; }
};
struct LightButton final : Button {
    std::string_view paint() const override { return "light button"; }
};
struct LightPanel final : Panel {
    std::string_view paint() const override { return "light panel"; }
};
struct Theme {
    virtual ~Theme() = default;
    virtual std::unique_ptr<Button> button() const = 0;
    virtual std::unique_ptr<Panel> panel() const = 0;
};
struct DarkTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<DarkPanel>(); }
};
struct LightTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<LightPanel>(); }
};
void render(const Theme& theme) {
    const auto button = theme.button();
    const auto panel = theme.panel();
    std::cout << button->paint() << " + " << panel->paint() << '\n';
}
int main() {
    render(DarkTheme{});
    render(LightTheme{});
}
