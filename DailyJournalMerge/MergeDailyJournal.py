import os
from GetMergedFilename import get_week_file
from GetListDaysOfWeek import get_week_days

filenames = get_week_days()
path = "E:\OneDrive\Journals\\"

with open(get_week_file(), "w") as outfile:
    for filename in filenames:
        try:
            with open(path + filename) as infile:
                heading = os.path.splitext(filename)[0]
                outfile.write("# " + heading + "\n\n")
                outfile.write(infile.read())
                outfile.write("\n\n---\n\n")
        except IOError:
            print(f"Error: {filename} does not appear to exist.")
