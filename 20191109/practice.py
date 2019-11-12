print("Let`s practice everything.")
print("You\'d need to know\'bout escapes with \\ that do \nnewlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there isnone.
"""
print("_________")
print(poem)
print("__________")

five = 10 - 2 + 3 - 6
print("This shold be five: %s" % five)

def secret_fomula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return(jelly_beans, jars, crates)

start_point = 10000
beans, jars, crates = secret_fomula(start_point)

print("With a starting point of: %d" % start_point)
print("We`d have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can do:")
print("We would have %d beans, %d jars, and %d crates." % secret_fomula(start_point))
