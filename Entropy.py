# This is the Password Security and Attack Simulation project.

# Create a password strength analysis for first module.
# Use EntropyCalcResearch.txt

def Entropy_gakaj():
    import math, string, time




    def entropyCalculator():
        length = 0
        password = input("Input password to be tested:\n") # determine Password to be tested
        length = len(password) # find length of password






        def NCalc(password):
            N = 0

            symbols = "!£$%^&*()_-+=|?><@:;~#{[]}.,!"

            if any(char.islower() for char in password):
                N += 26
                print("Lowercase")
            if any(char.isupper() for char in password):
                N += 26
                print("Uppercase")
            if any(char.isdigit() for char in password):
                N += 10
                print("Digit")
            if any(char in symbols for char in password):
                N += len(symbols)
                print("Symbols")
            if N >= 1:
                return N
            else:
                return "No password detected"
                    
                    
        NValue = NCalc(password)
        def entropyCalc(N,length):
            entropy = length * math.log2(N)
            # create logic for whether it is strong or week and return it
            return entropy

        print(f"Length of password is {length} and the N Value is {NValue}")
        #N = NCalc(password, symbols)
        EntropyValue = entropyCalc(NValue, length)

        print(f"Entropy calculated as {EntropyValue}")
        print("""Table is:\n | Entropy (bits) | Strength    |
        | -------------- | ----------- |
        | < 28           | Very weak   |
        | 28–35          | Weak        |
        | 36–59          | Reasonable  |
        | 60–127         | Strong      |
        | 128+           | Very strong |
        """)

        def assessment(a):
            if a < 28:
                return "Very Weak"
            if a >= 28 and a<=35:
                return "Weak"
            if a >= 36 and a<= 59:
                return "Reasonable"
            if a >= 60 and a<=127:
                return "Strong"
            if a >= 128:
                return "Very Strong Bravo!"

        assessment = assessment(EntropyValue)
        print(f"From this table we can see the value of {EntropyValue} is {assessment}")
        return EntropyValue
        

    entropyValue = entropyCalculator()
    print(entropyValue)

Entropy_gakaj()