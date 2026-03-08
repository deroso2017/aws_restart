# if-else statements, while loops, lists, and for loops

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

pKR = {"y": 10.07, "c": 8.18, "k": 10.53, "h": 6.00, "r": 12.48, "d": 3.65, "e": 4.25}

seqCount = {x: float(insulin.count(x)) for x in ["y", "c", "k", "h", "r", "d", "e"]}
print("seqCount: ", seqCount)

pH = 0

while pH <= 14:
    # Calculate positive charge contribution (basic amino acids: K, H, R)
    positiveCharge = sum(
        {
            x: ((seqCount[x] * (10 ** pKR[x])) / ((10**pH) + (10 ** pKR[x])))
            for x in ["k", "h", "r"]
        }.values()
    )

    # Calculate negative charge contribution (acidic amino acids: Y, C, D, E)
    negativeCharge = sum(
        {
            x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10 ** pKR[x])))
            for x in ["y", "c", "d", "e"]
        }.values()
    )
    netCharge = positiveCharge - negativeCharge

    print("{0:.2f}".format(pH), netCharge)
    pH += 1
