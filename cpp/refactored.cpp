#include <iostream>

using namespace std;
// Low-level class (can remain unchanged).
class Wallet {
private:
    float money;

public:
    Wallet(float initialMoney) : money(initialMoney) {}

    float getMoney() const {
        return money;
    }

    bool hasSufficientFunds(float amount) const {
        return money >= amount;
    }

    void debit(float amount) {
        if (hasSufficientFunds(amount)) {
            money -= amount;
        }
    }
};

// Mid-level class now handles its own internal logic.
class Customer {
private:
    Wallet wallet;

public:
    Customer(float money) : wallet(money) {}

    // REFACTORED: The Customer now provides a high-level method to make a payment.
    // It does NOT expose its internal wallet. It handles the details itself,
    // thereby hiding its implementation.
    void makePayment(float amount) {
        cout << "Customer is making a payment of $" << amount << endl;
        if (wallet.hasSufficientFunds(amount)) {
            wallet.debit(amount);
        } else {
            cout << "Customer has insufficient funds." << endl;
        }
    }

    float checkBalance() const {
        return wallet.getMoney();
    }
};

// High-level class is now much simpler and decoupled.
class Store {
public:
    // REFACTORED: The Store talks ONLY to its "immediate friend," the Customer.
    // It tells the customer what it wants (to make a payment) but not HOW to do it.
    // It has no knowledge of a "Wallet".
    void processPayment(Customer& customer, float amount) {
        cout << "Store is requesting payment from customer..." << endl;

        // The Store delegates the payment task to the Customer.
        customer.makePayment(amount);
        
        float remaining = customer.checkBalance();
        cout << "Payment processed. Customer now has $" << remaining << " left." << endl;
    }
};

int main() {
    Customer customer(100.0f);
    Store store;
    store.processPayment(customer, 25.0f);
    return 0;
}
