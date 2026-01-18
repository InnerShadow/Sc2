from multiprocessing import Pool
from src.loader_functions.loader import load_data

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    with Pool(processes = 4) as pool:
        results = pool.map(load_data, [0, -1, 10, -10])
    # end with
# end if
