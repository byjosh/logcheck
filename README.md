# logcheck
Check minutes seen in a minicom log file with date logged as [2025-01-01 09:00:00]

uses some builtin modules to accept an arbitary text file with date and time in [2025-01-01 09:00:00] format at start of line - then checks for specified months the days up to today that have missing minutes.
if used other than by original author you will need to change the months available - and it assumes the file is all within the same calendar year (i.e. a file starting near end of a year and finishing in the next year would break assumption).
