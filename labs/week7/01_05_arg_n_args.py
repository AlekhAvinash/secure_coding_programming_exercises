# write a function that takes two positional arguments and uses *args
# your function should:
"""
arguments:
    name: name of person
    job: job title of person
    *args: possesions that they own

returns --> Str
   It should return a string that says a nice message like
  "hello Gilad, I heard your job of washing dishes allows you to own a lawn-mower, house, cat, and bat"

Remember, your string needs to _grow_ with the *args - it needs infinite potential!

"""

def msg(name: str, job: str, *obs: list[str]) -> str:
    return f"Hello, {name}!! I heard your job of {job} allows you to own {', '.join(obs)}"

print(msg("Alekh", "Violinist", "a violin", "finger guards", "spare strings", "and a lot more!!"))