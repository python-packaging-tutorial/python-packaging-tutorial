#!/usr/bin/env python

"""
hacky script to convert the txt exported from google slides to rst for hieroglyph
"""

inlines = open("2018-AnacondaCON-PackageBuilding.pptx.txt").readlines()
outfilename = "PackageBuilding.rst"

rst = []

# first line is the title:
title = inlines.pop(0).strip()
rst.append("#" * len(title))
rst.append(title)
rst.append("#" * len(title))
rst.append("")
# find end of title page:
line = inlines.pop(0)
while line.strip() != '1':
    rst.append(line)
    line = inlines.pop(0)

while inlines:
    # look for slide break:
    slide_num = 0
    for i, line in enumerate(inlines):
        # numbers by themselves on a line is a new slide
        try:
            num = int(line)
        except ValueError:
            continue
        if num != slide_num:
            slide_num = num
            start_ind = i
        else:
            # we've hit the second numbers
            end_ind = i
            break
    # write content
    # slide header is right before slide number
    header = inlines[start_ind - 1].strip()
    rst.append(header)
    rst.append("-" * len(header))

    # content is the stuff above it
    for line in inlines[:start_ind - 1]:
        rst.append(line)
    # footer is the stuff in between
    rst.append("")
    for line in inlines[start_ind + 1:end_ind]:
        rst.append(line)
    # clear it all out:
    del inlines[:end_ind + 1]
    # and clear out any empty lines
    while inlines and (not inlines[0].strip()):
        del inlines[0]






open(outfilename, 'w').write("\n".join(rst))

