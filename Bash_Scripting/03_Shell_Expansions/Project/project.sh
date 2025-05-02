# Create a fs like:
#
# Jan/
#   1/
#       - log_file.txt
#   2/
#       - log_file.txt
#   3/
#       - log_file.txt
#   4/
#       - log_file.txt
#   For each day (1 - 31)
# 
# Do this for Jan, Feb, and Mar
#

mkdir -p ./{January/{01..31},Feburary/{01..28},March/{01..31}}

touch ./{January/{01..31},Feburary/{01..28},March/{01..31}}/log-daily