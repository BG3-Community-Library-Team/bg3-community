---
title: How to add tabs to your wiki page
description: [sandbox] Guide including template
published: false
date: 2024-11-10T14:45:00.765Z
tags: test
editor: markdown
dateCreated: 2024-11-10T07:43:44.876Z
---

# Tabs and Sub-tabs

Among other uses tabsets are a convenient way to organize longer articles, make more complex guides easier to follow, or break down the display of extensive information.

> Please note that tabs are only available in the markdown editor, they are rendered upon saving. 
Do not convert back to the visual editor once you added tabsets, it would inevitably break them.
{.is-warning}

To use tabsets either follow the steps below or copy the templates provided.

# How to add a tabset

Optional: you can add content between the tabset header and the tabset if you want.

# Tab {.tabset}
## Step One
Convert your page to the markdown editor if it isn't already
> Content inside tabsets can be styled per usual.
{.is-info}

## Step Two
Create your tabset header - this will be the name of your tabs - use header 1 (one # before the title)
In this example the tabset header is "How to add a tabset".

## Step Three
Now you need to tell the wiki to create tabs - you do this by creating a header 2 called "Tab" followed by "{.tabset}".
This is how my full header looks in markdown:
"# Tab {.tabset}"

## Step Four
Create your tab names - your tab names need to be one header designation below the tabset header. So if your tabset header is header 1(one # before the title), the tab names need to be header 2(two ## before the title).
My tab names are: "Step one", "Step Two", "Step Three", "Step Four", and "Step Five".

## Step Five
If you want to add content below the tabset, create a new header with the same designation as the tabset header.
In this example: "# How to add sub-tabs"

# How to add sub-tabs

# Tab {.tabset}
## 1. Info
It doesn't matter if you create a complete tabset first and then add sub-tabs later, or add them directly as you write your article.

Either way, start by creating a tabset per usual.

## 2. add sub-tabs
To add sub-tabs, simply repeat the steps you took to create a tabset while adjusting the designation of your tabset header and tab names.
In this example we used header 1 and 2 which means we have to use header 3 and 4 for the subtabs.

### Sub-tab example
### Tab {.tabset}
#### 2.1 empty tab
#### 2.2 empty tab
#### 2.3 empty tab

## 3. add sub-tabs to sub-tabs
### Tab {.tabset}
#### 3.1
Subsequent tabsets can be added by further adjusting the header designation. Keep adding two ## to the title and tab names.
#### 3.2 like so
### Sub-sub-tabset example
### Tab {.tabset}
#### 3.2.1 empty tab
#### 3.2.2 empty tab
#### 3.2.3 empty tab

## 4. below and beyond
### Tab {.tabset}
#### 4.1
Let's see how many layers of tabsets can be added?
#### 4.2 
#### Tab {.tabset}
##### 4.2.1 empty tab
##### 4.2.2 empty tab


## Step 5


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


















