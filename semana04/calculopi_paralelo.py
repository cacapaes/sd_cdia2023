from numba import config,prange, njit, threading_layer

@njit(parallel=True)
def test_pi_loop():
    num_steps = 100000
    step = 1.0 / num_steps

    the_sum = 0.0
    for j in prange(num_steps):
        c = step
        x = ((j-1) - 0.5) * step
        the_sum += 4.0 / (1.0 + x * x)

    pi = step * the_sum
    return pi

if __name__ == "__main__":
    pi = test_pi_loop()
    print(pi)
