# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """

  def index(val):
    global count
    count += 1
    return val+str(count)

  global count
  count = -1
  result = []
  temp_text = list(text)
  temp_text = list(map(index, temp_text))
  temp_text.sort(key=lambda x: text[int(x[1:]):])
  for i in temp_text:
    result.append(int(i[1:]))
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
