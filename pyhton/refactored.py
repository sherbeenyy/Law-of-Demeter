# refactored.py
from copy import deepcopy

# --- Functions that know about the "Customer" data structure ---

"""A helper function that knows how to get a customer's balance."""
def get_customer_balance(customer: dict) -> float:
    return customer['wallet']['money']


"""
Handles the logic for a customer payment. This is the "friend" function
that is allowed to know the customer's internal structure.
It returns a NEW, updated customer state to promote immutability.
"""
def customer_pays(customer: dict, amount: float) -> dict:

    print(f"{customer['name']} is making a payment of ${amount:.2f}")

    if get_customer_balance(customer) >= amount:
        # Create a deep copy to avoid changing the original data (immutability).
        new_customer = deepcopy(customer)
        new_customer['wallet']['money'] -= amount
        return new_customer

    # If not enough money, return the original state unchanged.
    print(f"{customer['name']} has insufficient funds.")
    return customer

"""
REFACTORED: This function is now decoupled from the Customer's data structure.
It talks ONLY to its "immediate friend" functions (`customer_pays`, `get_customer_balance`).
It delegates the tasks instead of doing them itself. It has no knowledge
of a 'wallet' or 'money'.
"""
# --- Function that knows about the "Store" logic ---

def process_payment(store_name: str, customer: dict, amount:float) -> dict:

    print(f"Store '{store_name}' is requesting payment...")
    
    # Delegate the payment task to the appropriate helper function.
    updated_customer = customer_pays(customer, amount)

    remaining = get_customer_balance(updated_customer)
    print(f"Payment processed. {updated_customer['name']} has ${remaining:.2f} left.")

    return updated_customer

# --- Main execution ---
if __name__ == "__main__":
    # Define our initial, immutable data state.
    customer_data = {
        'name': 'Bob',
        'wallet': {'money': 100.0}
    }
    store_name = "The Corner Shop"

    # The function receives the old state and returns the new state.
    final_customer_state = process_payment(store_name, customer_data, 25.0)

    print(f"\nOriginal state was not changed: {customer_data}")
    print(f"Final state: {final_customer_state}")
