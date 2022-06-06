# URL Filtered Words List

A dictionary of words to check against for post IDs in urls, for example so youtube.com/watch?v=**watch**XXXXXX never shows up, there are many reasons you may want to do this: for example a url may imply its offical (such as ?updateXXXXX) etc, and so no swears show up. It's not a super big issue since its unlikely one of them shows up anyway but if you were looking for said list: here it is!

You can download the code and edit it to change for what you want to include and exclude in your URLs. Currently it excludes anything with a symbol (well, the ones I added to the list), and anything with a capital to exclude accronyms and initalisms. You may want to edit this, for example not exclude things with a hyphen if you are doing a base-64 number with - and _. 

(also: please fogive my code, i tried looking through an array of words to exclude but it wasnt working)


I got the list of english words from [HERE](https://github.com/dwyl/english-words/)
