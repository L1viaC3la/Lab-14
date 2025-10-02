def llogarit_perqindjen(pjesa: float, teresia: float) -> float:
    if teresia <= 0 or pjesa < 0:
        return -1
    return (pjesa / teresia) * 100

pjesa = float(input("Pjesa: "))
teresia = float(input("Teresia: "))
rezultati = llogarit_perqindjen(pjesa, teresia)

if rezultati == -1:
    print("Të dhëna të pavlefshme")
else:
    print(f"Perqindja: {rezultati:.2f}%")
