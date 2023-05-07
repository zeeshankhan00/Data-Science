def inverse_normal_cdf(p:float, mu: float = 0, sigma: float =1, tolerance: float = 0.00001) -> float:
  if mu != 0 or sigma !=1:
    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
      mid_z = (low_z+ hi_z)/2
      mid_p = normal_cdf(mid_z)
      if mid_p < p:
        low_z = mid_z
      else:
        hi_z = mid_z
    return mid_z

