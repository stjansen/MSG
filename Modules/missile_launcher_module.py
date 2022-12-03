import numpy as np

# Determine whether to launch a missile
def missileLauncher(
    is_hostile, 
    pk_ratio, 
    rng = np.random.RandomState(None), 
    verbose = 0
):
    if verbose >= 1:
        print("\n-- Missile launcher --")
        print(f"Missile send: {is_hostile}")
    
    missile_hit = False
    if (is_hostile):
        random_number = rng.random(1)[0]
        if verbose >= 2:
            print(f"Random number picked: {random_number:.2f}")
        if random_number < pk_ratio:
            missile_hit = True

        if verbose >= 1:
            print(f"Missile hit: {missile_hit}")

    return missile_hit