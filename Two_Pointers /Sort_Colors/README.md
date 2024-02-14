# Statement 
 Given an array, colors, which contains a combination of the following three elements:
 - 0 representing red 
 - 1 representing white
 - 2 representing blue 

 Sort the array in place so that the lemenets of the same color are adjacent, with the colors in the order of red, white, and blue 


# Solution 
 - Declare three pointers: red (initilialized to the array's starting index), white (initilialized to the array's starting index), and blue (initialized to the array's last index)
 - Iterate through colors, moving elements to their correct positions based on their values 
 - If colors[white] is 0, we swap the values of colors[white] and colors[red]. We also increment both the white and red pointers by 1
 - Otherwise, if colors[white] will be 2, so we swwap the values colors[white] and colors[blue] and decrement the blue pointer by 1
 - Keep iterating until the white pointer exceeds the blue pointer