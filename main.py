import pandas


def avatarcsvloader(pathrest, filename, givenpath ='C:/Users/endyd/OneDrive/문서/ACTVERSE/AVATAR_DATA_SET-20220913T084458Z-001/AVATAR_DATA_SET/'):
    fullname = givenpath+pathrest+filename+'.csv'
    output = pandas.read_csv(fullname)
    return output


#testfile = pandas.read_csv('C:/Users/endyd/OneDrive/문서/ACTVERSE/AVATAR_DATA_SET-20220913T084458Z-001/AVATAR_DATA_SET/1.OFT(WT-N=50)/raw/H1.mat.csv_new.csv')
