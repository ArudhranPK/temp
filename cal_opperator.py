inp = input("Enter the operation in the form of \n'OPPERAND OPERATOR OPERAND' : ")

if "+" in inp:
    operand = "+"
elif "-" in inp:
    operand = "-"
elif "*" in inp:
    operand = "*"
elif "/" in inp:
    operand = "/"

inp = inp.split(operand)
opp1, opp2 = inp[0], inp[1]
opp1, opp2 = opp1.strip(), opp2.strip()
print(f"\nPREORDER : {operand}{opp1},{opp2}")
print(f"POSTORDER : {opp1},{opp2}{operand}")