---
title: Class DB Reference
description: Osiris Class-Specific DBs
published: true
date: 2024-05-02T16:31:31.558Z
tags: osiris, db, classes, dbs
editor: markdown
dateCreated: 2024-05-02T03:10:28.282Z
---

# Class-Specific DBs
The following DBs are ones that are Class-Specific.

# {.tabset}
## Bard
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CRIME_MusicalPerformance_DEBUG_QuickPerformanceTimer|DEBUG Quick Performance Timer|1|Integer|--|--|--|--|
|DB_CRIME_MusicalPerformance_DC|?|2|Integer DC|Tag UUID Difficulty|--|--|--|
|DB_CRIME_MusicalPerformance_Status|?|3|String Status|String Crime Type|String Event|--|--|
|DB_Bard_InstrumentRootToSpell|?|2|UUID|String Instrument Suffix|--|--|--|
|DB_CRIME_MusicalPerformance|?|3|?|Character UUID|String Crime Type|--|--|
|DB_CRIME_MusicalPerformance_WaitForFlourishesToStop|?|1|?|--|--|--|--|
|DB_CRIME_MusicalPerformance_Flourish|?|3|?|?|Character UUID|--|--|
|DB_CRIME_MusicalPerformance_SoundNames|?|3|?|?|?|--|--|
|DB_CRIME_MusicalPerformance_Listener|?|3|Integer|Character UUID|Character UUID|--|--|
|DB_CRIME_MusicalPerformance_SoundStarted|?|2|Character UUID|String|--|--|--|
|DB_CRIME_MusicalPerformance_Confronted|?|3|Integer|Character UUID|?|--|--|
|DB_CRIME_MusicalPerformance_NPCIgnoring|?|3|Character UUID|String|String concatenatedString|--|--|
|DB_CRIME_MusicalPerformance_NPCs|?|3|Integer|?|Character UUID|--|--|
|DB_CRIME_MusicalPerformance_TossCoin|?|2|Character UUID|Character UUID|--|--|--|
|DB_CRIME_MusicalPerformanceSpell|?|2|String Crime ID|String Spell ID|--|--|--|
|DB_CRIME_BardNPCPerformingWithPlayers|Bard NPCs performing with Players|3|Character UUID|?|?|--|--|
|DB_Bard_InstrumentRootToSpell|?|2|UUID|String Spell ID|--|--|--|

## Cleric
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_GLO_Spells_DivineInterventionSpells|List of Divine Intervention Spells|1|Spell ID|--|--|--|--|

## Paladin
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Debug_GLO_PaladinOathbreaker_ForceOathbreaker|Force an Oath Break|1|Integer|--|--|
|DB_GLO_Spells_DominatedOwnerStatus|List of Statuses that fall under Dominated|2|Status ID|Status ID|--|--|--|
|DB_GLO_Spells_TurnCharactersEvilStatuses|List of statuses that turn characters Evil|1|Status ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_RedemptionPrice|Cost of Redemption at a given level|2|Integer (Level Number)|Integer (Price)|--|--|--|
|DB_GLO_PaladinOathbreaker_LinkedDialogues|Linked Dialogs relating to Oathbreaker|1|Dialog Resource ID|--|--|--|--|
|DB_GLO_PaladinOathbreakerPath_SelectedOathbreaker|List of Characters that have selected Oathbreaker|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_CrimeID|?|2|Character UUID|Crime ID|--|--|--|
|DB_GLO_PaladinOathbreakerPath_WaitForCrime|?|2|Character UUID|Crime ID|--|--|--|
|DB_GLO_PaladinOathbreakerPath_KnightTalkedTo|List of Characters that have spoken to the Oathbreaker Knight|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreakerPath_WaitForDialog|?|1|Dialog Resource|--|--|--|--|
|DB_GLO_OathbreakerKnight_StartFirstAppearanceWith|?|1|?|--|--|--|--|
|DB_GLO_PaladinOathbreaker_Oathbreakers|List of Oathbreakers|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_SinsAndCrimeTypes|Sins and Crime Types that can proc an Oath-break|1|Flag String ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_GenericCrimes|Generic Crimes that can proc an Oath-break|1|Flag String ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_ProtectedNPCs|List of protected NPCs relating to Oath Breaking|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_SubclassTags|Link between Subclass Tag and Oath-Breaker Subclass Tag|2|Subclass Tag UUID|Oathbreaker Subclass Tag UUID|--|--|--|
|DB_GLO_PaladinOathbreaker_SubclassOathBrokenFlags|Link between Subclass Tag and Oath Broken Flag UUID|2|Broken Oath Flag|Subclass Tag UUID|--|--|--|
|DB_GLO_PaladinOathbreaker_EvilTags|Tags that prevent an Oath-break|1|Tag UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_CrimesToReact|Crimes that will cause a reaction from characters for specific Paladin Oaths|3|Subclass Tag ID|Crime String ID|NPC Tag ID|--|--|
|DB_GLO_PaladinOathbreaker_PotentialCrimeID|ID of Potential Oathbreaking Crime|1|Crime ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_NotifyAfterDialogEnds|?|3|Dialog Resource|Integer|?|--|--|
|DB_GLO_PaladinOathbreaker_ReactedToBreakingOath|?|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_RedemptionFromOathbreaker|Character that's gained Redemption|1|Character UUID|--|--|--|--|

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRY_RTN_Bard_GetPerformSpell|Returns Perform Spell|1|String Spell ID|--|--|