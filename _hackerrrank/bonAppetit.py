# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    # remove the declined item
    bill.remove(bill[k])
    # find the actual share
    actual = sum(bill)/2

    if b == actual:
        print("Bon Appetit")
    else:
        print(int(b-actual))
    return


print(bonAppetit([3, 10, 2, 9], 1, 7))
