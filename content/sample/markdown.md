Title: Markdown Test Page
Subtitle: Simple Markdown Test
Tags: markdown
Slug: markdown-test
Author: if1live
Date: 2010-01-01

[markdown syntax](http://daringfireball.net/projects/markdown/syntax)

## h2 heading
### h3 heading
#### h4 heading
##### h5 heading
###### h6 heading

## normal
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

## code block
```py
import unittest
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size/2 - 1] + copy[size/2]) / 2
class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
if __name__ == '__main__':
    unittest.main()
```

## inline test
this is ```block elem```.  
this is **bold elem**.  
this is *italic elem*.  
this is [link elem](/).  

## image test
![sample gif]({filename}../static/test/sidetail-sora.gif)

![sample png]({filename}../static/test/sora-kasugano.png)


## unordered list
* unordered list 1
* unordered list 2
	* unordered list 1
	* unordered list 2
* unordered list 3

## ordered list
1.  ordered list 1
1.  ordered list 2
	1.  ordered list 1
	1.  ordered list 2
1.  ordered list 3

## blockquotes
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.


##Table


|  A  |  B    |A or B | 
|-----|-------|-------|
|False| False | False | 
|True | False | True  | 
|False| True  | True  | 
|True | True  | True  | 