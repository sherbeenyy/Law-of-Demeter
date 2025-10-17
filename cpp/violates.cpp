#include <iostream>

using namespace std;
// Low-level class representing a wallet.
class Wallet {
private:
    float money;

public:
    Wallet(float initialMoney) : money(initialMoney) {}

    float getMoney() {
        return money;
    }

    void debit(float amount) {
        if (money >= amount) {
            money -= amount;
        } else {
            cout << "Error: Insufficient funds in wallet." << endl;
        }
    }
};

// Mid-level class representing a customer.
class Customer {
private:
    Wallet wallet;

public:
    Customer(float money) : wallet(money) {}

    // This getter is the root of the problem.
    // It exposes the internal Wallet object to the outside world.
    Wallet& getWallet() {
        return wallet;
    }
};

// High-level class that processes payments.
class Store {
public:
    // VIOLATION: The Store "reaches through" the Customer to get the Wallet.
    // This is a "train wreck" call: customer.getWallet().debit()
    // The Store is tightly coupled to the Customer because it knows that a Customer
    // has a Wallet and how to operate that wallet.
    void processPayment(Customer& customer, float amount) {
        cout << "Store is processing payment..." << endl;
        
        // The store is talking to a "stranger" (the wallet) it got from a "friend" (the customer).
        customer.getWallet().debit(amount);
        
        float remaining = customer.getWallet().getMoney();
        cout << "Payment successful. Customer has $" << remaining << " left." << endl;
    }
};

int main() {
    Customer customer(100.0f);
    Store store;
    store.processPayment(customer, 25.0f);
    return 0;
}
