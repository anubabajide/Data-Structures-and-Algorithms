def find_duplicates(s):
  s=s.lower(); l=s.split(" "); dupes =[]
  for i in range(len(l)):
    for j in range((i+1), len(l)):
      if l[i] == l[j]:
        dupes.append(l[i])
  return dupes
