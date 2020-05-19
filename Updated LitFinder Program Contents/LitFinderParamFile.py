##############################
## Parameter file for JUMPb ##
##############################

###################################
## Parameters for search methods ##
###################################
input_type = 0                  # 0 = list input, 1 = typed gene input. If input type==1, type in the name of the gene. If multiple individual inputs, separate by comma
organism = 0                    # If alternative is desired, specify organism (only one)
filter_option = 1               # 0 = no filter, 1 = filter
filter_keyword = 0              # 0 = no filter for keywords, 1 = filter for keywords (keywords should be specified {ie. cancer}, if multiple separate by commas {ie. cancer,alzheimer})
filter_journal = 0              # 0 = no filter for journals, 1 = filter for journals (journals should be specified {ie. nature}, if multiple separate by commas {ie. nature, science})
filter_year = 0                 # 0 = no filter for year, 1 = filter for year (year should be specified {ie. 2009}, use only one)
output_limit = 0                # 0 = returns all data, 1 = maxima imposed, specify later
citation_data = 0               # 0 = citation data enabled, 1 = citation data disabled
output_data = 0                 # 0 = output exported to file, 1 = output not exported


###########################
## User input components ##
###########################
#If input_type == 0, then input the user files containing gene list, one list per file
user_input_file = "InputUIDs.py"

#If input_type == 1, then input the gene names, separated by commas (gene symbol preferred {ie. actin = ACTB, netrin-1 = NTN1}
user_input_genes = ''
#If filter_keyword == 1, specify the keywords, separated by commas
keywords = 'cancer' 
#If filter_journal == 1, specify the journal, separated by commas
journals = 'nature'
#If filter_journal == 1, specify the journal, separated by commas
year = ''
organism_name='mouse'



######################################
## Parameters for processing output ##
######################################
#If output_limit == 1, specify the maximum number of papers per gene will be permitted
output_limits = 1000
#If citation_data = 0, specify the number of top citations user would like returned
citation_limit=10
#If output_data == 0, specify name of file to be exported
output_file = 'C:\\Users\\' + 'VanderwallDavid' + '\\Desktop\\'+'ParamFileWorked'+'.xlsx'

