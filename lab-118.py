# Add comments that explain the intention and flow of your code
# Use print() to print elements of your Python code to the console
# Use string manipulations to get the sequence of insulin from preproinsulin
# Do basic math on the molecular weight and sequence of insulin
# Assign string, int, and float variables to numbers that represent the weight of insulin
# Explore Python exceptions


# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr"
    "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)

print(preproInsulin)

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin
# Creating a list of the amino acid (AA) weights
items_list = [
    "A",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "Y",
]
aaWeights = {
    "A": 89.09,
    "C": 121.16,
    "D": 133.10,
    "E": 147.13,
    "F": 165.19,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "K": 146.19,
    "L": 131.17,
    "M": 149.21,
    "N": 132.12,
    "P": 115.13,
    "Q": 146.15,
    "R": 174.20,
    "S": 105.09,
    "T": 119.12,
    "V": 117.15,
    "W": 204.23,
    "Y": 181.19,
}

# Count the number of each amino acids
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in items_list}
print("aaCountInsulin: ", aaCountInsulin)
# Multiply the count by the weights
molecularWeightInsulin = sum(
    {x: (aaCountInsulin[x] * aaWeights[x]) for x in items_list}.values()
)
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print(
    "Error percentage: "
    + str(
        (
            (molecularWeightInsulin - molecularWeightInsulinActual)
            / molecularWeightInsulinActual
        )
        * 100
    )
)
