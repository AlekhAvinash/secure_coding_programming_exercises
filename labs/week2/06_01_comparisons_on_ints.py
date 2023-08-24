# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10
if a>b:
    print(f"The integer {a} is greater than {b}.")
else:
    print(f"The integer {b} is greater than {a}.")

# What is smaller , c or d?
c = 2.02
d = 2.01119999
if d>c:
    print(f"The float {c} is greater than {d}.")
else:
    print(f"The float {d} is greater than {c}.")

# what is bigger e or f?
e = float("inf")
f = 12912912912091928312903713582043754302895723048957
if e>f:
    print(f"The value {e} is greater than {f}.")
else:
    print(f"The value {f} is greater than {e}.")

# are these equal?

g = 1.02020202020
i = 1.0202020202011111
if i==g:
    print(f"The float {i} is greater than {g}.")
else:
    print(f"The float {g} is greater than {i}.")
