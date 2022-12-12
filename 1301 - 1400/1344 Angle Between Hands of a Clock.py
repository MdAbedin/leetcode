class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
      h_angle = 360*(hour/12) + 30*(minutes/60)
      m_angle = 360*(minutes/60)

      hi = max(h_angle, m_angle)
      lo = min(h_angle, m_angle)

      return min(hi-lo, lo + 360-hi)
