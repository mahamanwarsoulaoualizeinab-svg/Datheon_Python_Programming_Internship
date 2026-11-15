

portfolio = {}


def add_stock():
    symbol = input("Enter stock symbol: ").upper()
    shares = int(input("Enter number of shares: "))
    buy_price = float(input("Enter purchase price per share: "))

    portfolio[symbol] = {
        "shares": shares,
        "buy_price": buy_price
    }

    print(f"{symbol} added successfully!")


def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\nYour Portfolio:")
    print("-" * 60)

    for symbol, stock in portfolio.items():
        shares = stock["shares"]
        buy_price = stock["buy_price"]
        total_cost = shares * buy_price

        print(
            f"{symbol} | Shares: {shares} | "
            f"Buy Price: {buy_price:.2f} | "
            f"Total Cost: {total_cost:.2f}"
        )

    print("-" * 60)


def calculate_performance():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_investment = 0
    total_current_value = 0

    for symbol, stock in portfolio.items():
        shares = stock["shares"]
        buy_price = stock["buy_price"]

        current_price = float(
            input(f"Enter current price for {symbol}: ")
        )

        investment = shares * buy_price
        current_value = shares * current_price

        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        print(f"\n{symbol}")
        print(f"Investment: {investment:.2f}")
        print(f"Current Value: {current_value:.2f}")
        print(f"Profit/Loss: {profit_loss:.2f}")

    total_profit_loss = total_current_value - total_investment

    print("\nPortfolio Summary")
    print(f"Total Investment: {total_investment:.2f}")
    print(f"Total Current Value: {total_current_value:.2f}")
    print(f"Total Profit/Loss: {total_profit_loss:.2f}")


def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()

    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed successfully!")
    else:
        print("Stock not found.")


def main():
    while True:
        print("\nStock Portfolio Performance Tracker")
        print("1. Add a stock")
        print("2. View portfolio")
        print("3. Calculate performance")
        print("4. Remove a stock")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            calculate_performance()
        elif choice == "4":
            remove_stock()
        elif choice == "5":
            print("Thank you for using the tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()