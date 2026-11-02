"""Practice price calculator for your first session with Claude Code."""


def price_with_vat(price, vat=0.21):
    """Return the price with the tax applied."""
    # TODO: round the result to 2 decimals and reject negative prices with ValueError
    return price * (1 + vat)


def total(prices, vat=0.21):
    """Add up the prices in a list, with tax."""
    return sum(price_with_vat(p, vat) for p in prices)


if __name__ == "__main__":
    print(total([10, 19.99, 5.5]))
