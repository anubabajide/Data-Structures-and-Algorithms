# python3
import sys


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """

  seen = set()
  bwt_sorted = sorted(bwt)
  starts = {}
  for i in range(len(bwt_sorted)):
    if bwt_sorted[i] not in starts:
      starts[bwt_sorted[i]] = i
      
  occ_counts_before = {c:[0]*(len(bwt)+1) for c in starts}
  
  for i in range(len(bwt)):
    occ_counts_before[bwt[i]][i+1] += 1
  
  for c in occ_counts_before:
    for i in range(2, len(occ_counts_before[c])):
      occ_counts_before[c][i] += occ_counts_before[c][i-1]
  

  return starts, occ_counts_before



def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  top = 0
  bottom = len(bwt) - 1
  pattern = list(pattern)
  while top <= bottom:
    if pattern:
      symbol = pattern.pop()
      # if symbol in bwt[top:bottom+1]:
      top = starts[symbol] + occ_counts_before[symbol][top]
      bottom = starts[symbol] + occ_counts_before[symbol][bottom+1] - 1  
      # else:
      #   return 0
    else:
      return bottom - top + 1
  return 0
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
