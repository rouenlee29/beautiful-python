# TODO add comments 
import sys

def swap(i,j,m):
  new_m = m.copy()
  new_m[i] = m[j]
  new_m[j] = m[i]
  return new_m

def check_sorted(m):
  sortedd = True
  for i in range(1,len(m)):
    if m[i]<m[i-1]:
      sortedd = False
      break # break out of for loop
  return sortedd

def main():
    
    raw = sys.argv[1]
    m = [int(r) for r in raw.split(",")]
    while check_sorted(m) == False:
        for i in range(0,len(m)):
            if (i!=0):
                if (m[i]< m[i-1]):
                    m = swap(i,i-1,m)
            if (i!= len(m)-1):
                if (m[i]> m[i+1]):
                    m = swap(i,i+1,m)
    print(m) 


if __name__ == "__main__":
    main()
        