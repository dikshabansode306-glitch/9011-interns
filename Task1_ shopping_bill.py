def calculateElectronicsGST(a, b):
    """Step 1: Add a + b, then add 18% GST."""
    return (a + b) * 1.18

def calculateFashionGST(c, d):
    """Step 2: Add c + d, then add 13% GST."""
    return (c + d) * 1.13

def calculateFoodGST(e):
    """Step 3: Add 7% GST to e."""
    return e * 1.07

def totalBill(a, b, c, d, e):
    """Step 4: Call the three GST functions and add their returned amounts."""
    return calculateElectronicsGST(a, b) + calculateFashionGST(c, d) + calculateFoodGST(e)

def calculateDiscountedBill(a, b, c, d, e):
    """Step 5: Calculate a 20% discount on total, subtract it, and return final payable."""
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    final_payable = total - discount
    
    # Matches the task's expected output format exactly
    print(f"Total after GST = {total:.2f} | Discount = {discount:.2f} | Final payable amount = {final_payable:.2f}")
    
    return final_payable

# Main execution block using the mandatory sample test values
if __name__ == "__main__":
    calculateDiscountedBill(100, 100, 100, 100, 100)
