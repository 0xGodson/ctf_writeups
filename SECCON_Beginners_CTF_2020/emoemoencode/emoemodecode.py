emoemo = "🍣🍴🍦🌴🍢🍻🍳🍴🍥🍧🍡🍮🌰🍧🍲🍡🍰🍨🍹🍟🍢🍹🍟🍥🍭🌰🌰🌰🌰🌰🌰🍪🍩🍽"

for c in emoemo:
    print(chr(ord(c)-0x1f300), end="")
print()