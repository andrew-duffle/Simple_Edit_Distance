def distance(word1,word2):

    diffs={}   #create tuple dictionary
    for i in range(len(word1)+1):
        diffs[i,0]=i
    for j in range(len(word2)+1):
        diffs[0,j]=j
    for i in range (1,len(word1)+1):
        for j in range(1,len(word2)+1):
            inserted= diffs[i,j-1] +1 #one point for insertion
            deleted= diffs[i-1,j] +1 #one point for deletion
            subed= diffs[i-1,j-1] if word1[i-1]==word2[j-1] else diffs[i-1,j-1]+1 #two points for sub edit per JA 1 point for sub
            diffs[i,j]=min(inserted, deleted, subed)
    return diffs[i,j]
