---
title: Dictionary Test
description: 
published: true
date: 2024-06-21T05:22:47.864Z
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
        -int click "size in feet" "http://www.github.com"
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
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
        -int click "size in feet" "http://www.github.com"
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

----
