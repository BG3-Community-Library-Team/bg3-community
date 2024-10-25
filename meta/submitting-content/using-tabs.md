---
title: How to add tabs to your wiki page
description: Guide including template
published: true
date: 2024-10-25T10:00:45.947Z
tags: guide, test
editor: markdown
dateCreated: 2024-06-28T10:32:48.003Z
---

# Tabs - How To
<!-- add some fancy text here if you want to -->
Tabsets are a convenient way to organize longer articles, make more complex guides easier to follow, or break down the display of extensive information, among other uses.
To use tabsets either follow the steps below or copy the template provided below.

## Tab {.tabset}
### Step One
Tabs are only available in the markdown editor, they are rendered upon saving.
Convert your page to the markdown editor if it isn't already
Do not convert back to the visual editor, it would break your tabs.
### Step Two
Create your tabset header - this will be the name of your tabs - use header 1 (one # before the title)
In this example the tabset header is "Tabs - How To".
### Step Three
Now you need to tell the wiki to create tabs - you do this by creating a header 2 called "Tab" followed by "{.tabset}".
This is how my full header looks in markdown:
"## Tab {.tabset}"
### Step Four
Create your tab names - your tab names need to be one header designation below the tabset header. So if your tabset header is header 2(two ### before the title), the tab names need to be header 3(three ### before the title).
My tab names are: "Step one", "Step Two", "Step Three", "Step Four", "Step Five" and "Template".
### Step Five
If you want to add content below the tabset, create a new header with the same designation as the tabset header.
In this example: "## Next Section"

### Template
For convenience, simply copy / paste the below code into your markdown editor, rename the tabs, and remove or add tabs according to your vision.

```
# Tabs - How To
## Tab {.tabset}
### Step One
### Step Two
### Step Three
### Step Four
### Step Five
## Next Section
```

## Next Section

![add_tabs_to_the_wiki.webp](/test/add_tabs_to_the_wiki.webp =500x)

<!-- add some more fancy text, I recommend questionable poetry -->
![cmty_pride_logo.webp](/test/alithea/cmty_pride_logo.webp)























