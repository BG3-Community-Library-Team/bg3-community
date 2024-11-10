---
title: How to add tabs to your wiki page
description: [sandbox] Guide including template
published: false
date: 2024-11-10T13:02:33.528Z
tags: test
editor: markdown
dateCreated: 2024-11-10T07:43:44.876Z
---

# Tabs and Subtabs

Among other uses Tabsets are a convenient way to organize longer articles, make more complex guides easier to follow, or break down the display of extensive information.

> Please not that Tabs are only available in the markdown editor, they are rendered upon saving. 
Do not convert back to the visual editor once you added Tabs, it would break them.
{.is-warning}


# How to add Tabs

To use tabsets either follow the steps below or copy the templates provided.

# Tab {.tabset}
## Step One
Convert your page to the markdown editor if it isn't already

> Content inside tabsets can be styled per usual.
{.is-info}

## Step Two
Create your tabset header - this will be the name of your tabs - use header 1 (one # before the title)
In this example the tabset header is "Tabs - How To".
## Step Three
Now you need to tell the wiki to create tabs - you do this by creating a header 2 called "Tab" followed by "{.tabset}".
This is how my full header looks in markdown:
"# Tab {.tabset}"
## Step Four
Create your tab names - your tab names need to be one header designation below the tabset header. So if your tabset header is header 2(two ### before the title), the tab names need to be header 3(three ## before the title).
My tab names are: "Step one", "Step Two", "Step Three", "Step Four", "Step Five" and "Template".
## Step Five
If you want to add content below the tabset, create a new header with the same designation as the tabset header.
In this example: "# Subtabs"

# Subtabs

you can add some text here

# Tab {.tabset}
## Step 1
content
## Step 2
### Subtab {.tabset}
#### 2.1
content
#### 2.2
content
## Step 3
### Subtab {.tabset}
#### 3.1
content
#### 3.2
content
#### 3.3
content
## Step 4
content
## Step 5
### Subtab {.tabset}
#### 5.1
content
#### 5.2
content
# Templates
For convenience, simply copy / paste the below code into your markdown editor, rename the tabs, and remove or add tabs according to your vision.

## Template Tabs

```
# Tabs - How To
# Tab {.tabset}
## Step One
## Step Two
## Step Three
## Step Four
## Step Five
# Next Section
```

## Template Subtabs




![cmty_pride_logo.webp](/test/alithea/cmty_pride_logo.webp)


















