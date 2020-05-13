import pandas as pd

# read in csv files from previous downloads
# set tcmainid as index
# to be able to cross reference against most recent download
citations = pd.read_csv('citations.csv ', index_col='Citation #')

# download most recent citations
citations_recent = pd.read_csv('https://opendatafiles.blob.core.windows.net/odfiles/spd_PDCitations.csv', 
                               index_col='Citation #',
                               low_memory=False)
# combine citations
all_citations = pd.concat([citations,
                           citations_recent])

# remove duplicates
all_citations = all_citations.loc[~all_citations.index.duplicated(),:]

# save the most recently updated citations
all_citations.to_csv('citations.csv')

#################################
# same as the above, but for the arrests dataset
# read in csv files from previous downloads
# set arrest # as index
# to be able to cross reference against most recent download
arrests = pd.read_csv('arrests.csv ', index_col='Arrests #')

# download most recent arrests
arrests_recent = pd.read_csv('https://opendatafiles.blob.core.windows.net/odfiles/spd_PDArrests.csv', 
                               index_col='Arrests #',
                               low_memory=False)
# combine citations
all_arrests = pd.concat([arrests,
                        arrests_recent])

# remove duplicates
all_arrests = all_arrests.loc[~all_arrests.index.duplicated(),:]

# save the most recently updated citations
all_arrests.to_csv('arrests.csv')