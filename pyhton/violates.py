# violation.py

# In functional programming, LoD applies to data structures.
# A function should not reach deep into a nested structure.

"""
VIOLATION: This function knows the internal structure of the customer data.
It "reaches through" the customer dictionary to get to the wallet, and
through the wallet to get to the money. This creates tight coupling.

If we decide to rename 'wallet' to 'payment_method' or 'money' to 'balance',
this function breaks immediately.
"""
def process_payment(store_name: str, customer: dict, amount: float) -> dict:

    print(f"Store '{store_name}' is processing payment...")

    # Direct access into a nested structure to perform a command (mutation).
    # This is highly coupled to the data's shape.
    customer['wallet']['money'] -= amount

    # Direct access for a query.
    remaining = customer['wallet']['money']
    print(f"Payment successful. {customer['name']} has ${remaining:.2f} left.")

    # In a functional style, we should return a new state, but for this
    # simple example, we return the mutated original to highlight the coupling.
    return customer

# --- Main execution ---
if __name__ == "__main__":std
    # Define our initial data state.
    customer_data = {
        'name': 'Bob',
        'wallet': {'money': 100.0}
    }
    store_name = "The Corner Shop"

    # The function mutates the original `customer_data` dictionary.
    updated_customer = process_payment(store_name, customer_data, 25.0)

    print(f"\nFinal state: {updated_customer}")
