class Solution(object):

  def isIsomorphic(self, s, t):
    """:type s: str

    :type t: str
    :rtype: bool
    """
    map_s_to_t = {}
    map_t_to_s = {}

    for char_s, char_t in zip(s, t):
      # Check existing mapping from s -> t
      if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
        return False

      # Check existing mapping from t -> s (ensures one-to-one bijection)
      if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
        return False

      map_s_to_t[char_s] = char_t
      map_t_to_s[char_t] = char_s

    return True