import tensorflow as tf
import pandas as pd
import timeit
import numpy

dateparse = lambda x, y: pd.to_datetime(x + ' ' + y)

propertyCount = pd.read_csv("./data/DMA_Property Count_2016_2017.csv")
postCodes = pd.read_csv("./data/postcode.csv")

# dataw1 = pd.read_csv("./data/W1_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# dataw2 = pd.read_csv("./data/W2_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# dataw3 = pd.read_csv("./data/W3_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# dataw4 = pd.read_csv("./data/W4_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# dataw5 = pd.read_csv("./data/W5_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)

# datan1 = pd.read_csv("./data/N1_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datan2 = pd.read_csv("./data/N2_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datan3 = pd.read_csv("./data/N3_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datan4 = pd.read_csv("./data/N4_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datan5 = pd.read_csv("./data/N5_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
#
# datas1 = pd.read_csv("./data/S1_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datas2 = pd.read_csv("./data/S2_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datas3 = pd.read_csv("./data/S3_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datas4 = pd.read_csv("./data/S4_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datas5 = pd.read_csv("./data/S5_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
#
# datae1 = pd.read_csv("./data/E1_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datae2 = pd.read_csv("./data/E2_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datae3 = pd.read_csv("./data/E3_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datae4 = pd.read_csv("./data/E4_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)
# datae5 = pd.read_csv("./data/E5_2016_2017.csv", parse_dates={'Datetime': ['Date', 'Time']}, date_parser=dateparse, keep_date_col=True)

# allCsvs = pd.concat([datae1,datae2,datae3,datae4,datae5,
#                  datan1,datan2,datan3,datan4,datan5,
#                  datas1,datas2,datas3,datas4,datas5,
#                  dataw1,dataw2,dataw3,dataw4,dataw5])

# westRegion = pd.concat([dataw1,dataw2,dataw3,dataw4,dataw5]);

# westRegion = pd.read_csv("./data/west.csv")
#
# mergedWithPropertyData = pd.merge(westRegion, propertyCount, on='DMA')
#
# mergedWithPostCode = pd.merge(mergedWithPropertyData, postCodes, on='DMA')
#
# mergedWithPostCode.to_csv("./data/west_processed.csv")

df = pd.read_csv("./data/west_processed.csv")

del df['Unnamed: 0']

df.to_csv("./data/west_processed.csv")

# mergedWithPropertyData.to_pickle("./data/all")

# df = pd.read_pickle("./data/all")
#
# west = df[(df['Area'].isin(['W1', 'W2', 'W3', 'W4', 'W5']))]
# west.to_csv("./data/west.csv")
#
# north = df[(df['Area'].isin(['N1', 'N2', 'N3', 'N4', 'N5']))]
# north.to_csv("./data/north.csv")
#
# south = df[(df['Area'].isin(['S1', 'S2', 'S3', 'S4', 'S5']))]
# south.to_csv("./data/south.csv")
#
# east = df[(df['Area'].isin(['E1', 'E2', 'E3', 'E4', 'E5']))]
# east.to_csv("./data/east.csv")