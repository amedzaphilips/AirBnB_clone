# Web - Static

##What is the DOM
The Document Object Model (DOM) is a programming interface for web documents. It represents the structure of a document as a tree of objects, where each node in the tree corresponds to a part of the document (such as an element, attribute, or text). The DOM allows programs and scripts to dynamically access and update the content, structure, and style of documents.

## Building Your First Web Page
If you can, imagine a time before the invention of the Internet. Websites didn’t exist, and books, printed on paper and tightly bound, were your primary source of information. It took a considerable amount of effort—and reading—to track down the exact piece of information you were after.

Today you can open a web browser, jump over to your search engine of choice, and search away. Any bit of imaginable information rests at your fingertips. And chances are someone somewhere has built a website with your exact search in mind.

Within this book I’m going to show you how to build your own websites using the two most dominant computer languages—HTML and CSS.

Before we begin our journey to learn how to build websites with HTML and CSS, it is important to understand the differences between the two languages, the syntax of each language, and some common terminology.


### What Are HTML & CSS?
__HTML__, HyperText Markup Language, gives content structure and meaning by defining that content as, for example, headings, paragraphs, or images. CSS, or Cascading Style Sheets, is a presentation language created to style the appearance of content—using, for example, fonts or colors.

The two languages—HTML and CSS—are independent of one another and should remain that way. CSS should not be written inside of an HTML document and vice versa. As a rule, HTML will always represent content, and CSS will always represent the appearance of that content.

With this understanding of the difference between HTML and CSS, let’s dive into HTML in more detail.


### Understanding Common HTML Terms
While getting started with HTML, you will likely encounter new—and often strange—terms. Over time you will become more and more familiar with all of them, but the three common HTML terms you should begin with are elements, tags, and attributes.

###Elements
Elements are designators that define the structure and content of objects within a page. Some of the more frequently used elements include multiple levels of headings (identified as `<h1>` through `<h6>` elements) and paragraphs (identified as the `<p>` element); the list goes on to include the `<a>`, `<div>`, `<span>`, `<strong>`, and `<em>` elements, and many more.

Elements are identified by the use of less-than and greater-than angle brackets, < >, surrounding the element name. Thus, an element will look like the following:

1	`<a>`

              
__Tags__
The use of less-than and greater-than angle brackets surrounding an element creates what is known as a tag. Tags most commonly occur in pairs of opening and closing tags.

An opening tag marks the beginning of an element. It consists of a less-than sign followed by an element’s name, and then ends with a greater-than sign; for example, `<div>`.

A closing tag marks the end of an element. It consists of a less-than sign followed by a forward slash and the element’s name, and then ends with a greater-than sign; for example, `</div>`.

The content that falls between the opening and closing tags is the content of that element. An anchor link, for example, will have an opening tag of `<a>` and a closing tag of `</a>`. What falls between these two tags will be the content of the anchor link.

So, anchor tags will look a bit like this:

1	`<a>...</a>`

              
__Attributes__
Attributes are properties used to provide additional information about an element. The most common attributes include the id attribute, which identifies an element; the class attribute, which classifies an element; the src attribute, which specifies a source for embeddable content; and the href attribute, which provides a hyperlink reference to a linked resource.

Attributes are defined within the opening tag, after an element’s name. Generally attributes include a name and a value. The format for these attributes consists of the attribute name followed by an equals sign and then a quoted attribute value. For example, an <a> element including an href attribute would look like the following:

1	`<a href="https://github.com/Josh-Atsu">my github</a>`


## Setting Up the HTML Document Structure
HTML documents are plain text documents saved with an .html file extension rather than a .txt file extension. To begin writing HTML, you first need a plain text editor that you are comfortable using. Sadly this does not include Microsoft Word or Pages, as those are rich text editors. Two of the more popular plain text editors for writing HTML and CSS are Dreamweaver and Sublime Text. Free alternatives also include Notepad++ for Windows and TextWrangler for Mac.

All HTML documents have a required structure that includes the following declaration and elements: `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.

The document type declaration, or `<!DOCTYPE html>`, informs web browsers which version of HTML is being used and is placed at the very beginning of the HTML document. Because we’ll be using the latest version of HTML, our document type declaration is simply `<!DOCTYPE html>`. Following the document type declaration, the `<html>` element signifies the beginning of the document.

Inside the `<html>` element, the `<head>` element identifies the top of the document, including any metadata (accompanying information about the page). The content inside the `<head>` element is not displayed on the web page itself. Instead, it may include the document title (which is displayed on the title bar in the browser window), links to any external files, or any other beneficial metadata.

All of the visible content within the web page will fall within the `<body>` element. A breakdown of a typical HTML document structure looks like this:

	<!DOCTYPE html>
	<html lang="en">
	  <head>
	    <meta charset="utf-8">
	    <title>Hello World</title>
	  </head>
	  <body>
	    <h1>Hello World</h1>
	    <p>This is a web page.</p>
	  </body>
	</html>
