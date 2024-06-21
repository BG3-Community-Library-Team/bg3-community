---
title: Dictionary Test
description: 
published: true
date: 2024-06-21T05:25:55.337Z
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
    
    Fish[an <b>important</b> <a href="http://google.com">link</a>] 
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
    
    Fish[an <b>important</b> <a href="http://google.com">link</a>] 
```

----
