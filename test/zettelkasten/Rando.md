---
title: Rando's Repository
description: Random Rubbish
published: false
date: 2025-01-02T01:55:24.809Z
tags: zettelkasten, inbox
editor: markdown
dateCreated: 2025-01-02T01:55:24.809Z
---

# Inbox
## Toolkit
### Multiple Creators on Mod.io Pages
You can set additional contributors with different levels of access.

It's specific to mod.io and the toolkit, so project files can be shared.

If you have access to the mod page as a contributor, you can upload to the same page. The publish handle is generated in the main meta with the first upload, just need to ensure that's the same.
```xml
<attribute id="PublishHandle" type="uint64" value="number"/>
```
## Modding Data
### `Force()` Examples
```js
new entry "Projectile_VacuumBulb"
type "SpellData"
data "SpellType" "Projectile"
data "SpellProperties" "IF(not SavingThrow(Ability.Strength, 18)):Force(-5, TargetToEntity, Neutral, false, true);DealDamage(1,Force)"
data "TargetFloor" "-1"
data "AreaRadius" "6"
data "ExplodeRadius" "6"
data "TargetConditions" "not Grounded() and IsMovable()"
data "Trajectories" "a312633d-f207-4e0d-953c-76bfdc06342c,4bf95009-1b5b-31e1-98b4-3367d0fa601d"
// Void Bulb
data "DisplayName" "hecb71a57g5a16g485cga535gdb6b73b54b46;1"
// Throw this alien bulb at a target and possibly pull in nearby objects and creatures.
data "Description" "h5e99507eg1e25g4418gb2eegf4abd901de9e;3"
data "TooltipDamageList" "DealDamage(1,Force)"
data "TooltipAttackSave" "Strength"
data "CycleConditions" "Enemy() and not Dead()"
data "SpellAnimation" "73afb4e5-8cfe-4479-95cf-16889597fee3,,;7e67bfd0-2fc2-4d10-bed5-cfda9e660de5,,;eb054308-7fce-4b85-bf4c-7a0031fda7ac,,;0b0dc35b-4953-45c0-a9eb-8d3fef5e798a,,;6ec808e1-e128-44ef-9361-a713bf86de8f,,;b2e9c771-3497-444c-b360-23b4441985a1,,;f920a0a6-f257-4ce4-8d17-2dcaa7bb7bbb,,;,,;,,"
data "SpellFlags" "AddFallDamageOnLand;DisplayInItemTooltip;IsHarmful;ImmediateCast"
data "DamageType" "Force"
```
```js
new entry "Projectile_LOW_Chasm_ForceGrenade"
type "SpellData"
data "SpellType" "Projectile"
using "Projectile_Bomb"
data "SpellProperties" "GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt);"
data "SpellRoll" "not SavingThrow(Ability.Strength, 15)"
data "SpellSuccess" "DealDamage(3d4+9,Force,Magical);Force(5, TargetToEntity)"
// Force Bomb
data "DisplayName" "h47d21786gf4d8g4e6dga0b3g81dabbda3fe6;2"
// Throw a bomb that wounds nearby creatures and possibly pushes them back.
data "Description" "h0413e714g1f94g4529gb84bg323388fc1ac2;2"
data "TooltipAttackSave" "Strength"
```
```js
new entry "Target_Shove"
type "SpellData"
data "SpellType" "Target"
data "SpellProperties" "RemoveStatus(SLEEP);RemoveStatus(SLEEPING);RemoveStatus(SG_Sleeping);"
data "TargetCeiling" "0"
data "TargetFloor" ".25"
data "TargetRadius" "1.5"
data "SpellRoll" "ShoveCheck()"
data "SpellSuccess" "IF(not Ally()):Force(ShoveDistance,OriginToEntity,Aggressive);IF(Ally()):Force(ShoveDistance,OriginToEntity,Friendly)"
data "SpellFail" "ApplyStatus(SAVED_AGAINST_HOSTILE_SPELL, 100, 0)"
data "TargetConditions" "not Self() and CanShoveWeight() and IsMovable() and not Grounded() and not Tagged('GASEOUS_FORM') and not (not Player(context.Source) and Combat(context.Source) and Character() and not (Enemy() or HasStatus('SG_Unconscious'))) and not Tagged('CANT_SHOVE_THROW')"
data "Icon" "Action_Shove"
// Shove
data "DisplayName" "h566b606eg4e52g452eg9313g703c8f77a44b;1"
// Try to push a target away. Your chances depend on your Athletics, and are higher if you're hidden or invisible. 
data "Description" "h3921ea48g1ac9g4310gbd52gb7041dcee29f;7"
// The shove distance depends on your <LSTag Tooltip="Strength">Strength</LSTag> and the target's weight.
data "ExtraDescription" "h0907f7c8g694cg45c2ga77fg06cc883b7a9d;3"
data "PrepareSound" "Generic_GeneralAction_Start"
data "PrepareLoopSound" "Generic_GeneralAction_Loop"
data "CastSound" "Action_Cast_Shove"
data "PreviewCursor" "Melee"
data "CastTextEvent" "Cast"
data "CycleConditions" "CanShoveWeight() and not Grounded()"
data "UseCosts" "BonusActionPoint:1"
data "SpellAnimation" "SnippedForSpace"
data "VerbalIntent" "Utility"
data "SpellFlags" "IsMelee;AddFallDamageOnLand;IsHarmful;CombatLogSetSingleLineRoll"
data "SpellActionType" "Shove"
data "HitAnimationType" "PhysicalDamage"
data "SpellAnimationIntentType" "Peaceful"
data "PrepareEffect" "c512042e-a04f-4a02-af7a-16f30e11ed95"
data "CastEffect" "3fdf3e73-59a3-4518-9521-35f40374d048"
data "TargetEffect" "5d8c64e3-f9ff-4ee0-b0b6-2a081c7244a8"
data "SpellSoundMagnitude" "Small"
data "Sheathing" "Sheathed"
```
> LaughingLeader — Today at 08:57
Force is in the LSLibDefinitions.xml as well, since it's a "Functor" (this file has arg names / how many args). I didn't know Force actually had more args :pausechamp2: 
https://github.com/Norbyte/lslib/blob/master/LSLibDefinitions.xml#L388

```xml
	<Function Type="Functor" Name="Force" RequiredArgs="1">
		<Arg Name="Distance" Type="Lua" />
		<Arg Name="Origin" Type="ForceFunctorOrigin" />
		<Arg Name="Aggression" Type="ForceFunctorAggression" />
		<Arg Name="ControlArc" Type="Boolean" /> <!--Arc can be controlled with spell placement, AOE only?-J-->
		<Arg Name="CanStand" Type="Boolean" /> <!--true:Entities will land in front of character if pulled (e.g. Target_ThornWhip), false:Entities can be flung over character-->
	</Function>
```

