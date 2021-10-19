# Enable all rules by default
all

######################################################
# Deactivated/excluded rules
######################################################

# Allow first header to not be a top level header
# since top-level is set by metadata
exclude_rule 'MD002'
# First line in file does not have to be a top level header
# since top-level is set by metadata
exclude_rule 'MD041'
# Allow multiple consecutive blank lines
exclude_rule 'MD012'
# Allow raw HTML to include videos, for example.
exclude_rule 'MD033'
# Bare URL used rule seems buggy (false positives), therefore excluded
exclude_rule 'MD034'
# Allow code blocks without a language specified
exclude_rule 'MD040'

######################################################
# Adapted rules
######################################################

# Enforce dashes as symvol in lists
rule 'MD004', :style => :dash
# Extend line length for text.
# This will complain for overly wide tables and code blocks.
rule 'MD013', :line_length => 99999

# Nested lists should be indented with four spaces.
# Modification: Question marks should be allowed
rule 'MD026', :punctuation => '.,;:!'

# Ordered lists must have prefix that increases in order
rule 'MD029', :style => :ordered
