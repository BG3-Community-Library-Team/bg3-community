---
title: Dictionary Test
description: 
published: true
date: 2024-06-21T05:26:26.696Z
tags: 
editor: markdown
dateCreated: 2024-06-20T22:50:16.737Z
---

```kroki
mermaid

---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int size in feet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
    
    Fish{"&lt;a href&#61;&#39;https://google.com&#39;&gt;Google link here&lt;/a&gt;"}
```
    
    
```md
mermaid

---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int size in feet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
    
    Fish{"&lt;a href&#61;&#39;https://google.com&#39;&gt;Google link here&lt;/a&gt;"}
```

----
