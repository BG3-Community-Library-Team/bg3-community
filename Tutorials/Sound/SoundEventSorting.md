---
title: Using Sound Events to Narrow Down Source Files
description: A tutorial on how to use Audio Events from a Sounds merged.lsf to group sound files in a SoundBank
published: true
date: 2024-05-20T21:04:24.499Z
tags: tutorials, audio, sound
editor: markdown
dateCreated: 2024-05-20T20:34:45.294Z
---

BG3 Soundbanks have very little rhyme or reason as to their contents. Rather than being sorted by type of sound or speaker, they are grouped by ‘[Audio Events](https://wiki.bg3.community/Information/Sound/Summary#audio-events).’ These events are grouped into relevantly-named folders in Shared\\Public\\Shared\\Content\\Assets\\Sounds. For this tutorial, we will be using the merged.lsf(x) found in Shared\\Public\\Shared\\Content\\Assets\\Sounds\\Vocals\\\[PAK\]\_Vocals.

Here is an example of one of that file's Sound Events:

```xml
<node id="Resource">
	<attribute id="DisplayName" type="LSString" value="" />
	<attribute id="Duration" type="float" value="8.300573" />
	<attribute id="GMSoundCategory" type="int8" value="0" />
	<attribute id="GMSubSection" type="LSString" value="" />
	<attribute id="ID" type="FixedString" value="40a08c44-c740-a693-ba33-7a4e4743c367" />
	<attribute id="Internal" type="bool" value="True" />
	<attribute id="Localized" type="bool" value="False" />
	<attribute id="MaxDistance" type="float" value="-1" />
	<attribute id="Name" type="LSString" value="BGClickReaction_ReptAction_MoveTo" />
	<attribute id="Preload" type="bool" value="False" />
	<attribute id="SoundBank" type="FixedString" value="VOCALS" />
	<attribute id="SoundCategory" type="int8" value="0" />
	<attribute id="SoundCodec" type="int8" value="7" />
	<attribute id="SoundEvent" type="FixedString" value="BGClickReaction_ReptAction_MoveTo" />
	<attribute id="SoundEventID" type="uint32" value="1053678736" />
	<attribute id="SoundEventUUID" type="guid" value="2856fe7c-ec95-4cbc-a640-79b855885b6f" />
	<attribute id="SourceFile" type="LSString" value="Public/Shared/Assets/Sound/VOCALS.bnk" />
	<attribute id="_OriginalFileVersion_" type="int64" value="144115196665790668" />
</node>
```

There are really only three lines we need to look at: the SoundEvent for an idea of what these sounds will be about, the SoundEventID, which we will use when we get to the relevant SoundBank,  and the SourceFile, which tells us exactly which SoundBank this resource is linked to. Copy the SoundEventID, `"1053678736"`.

Now let's open up VOCALS.bnk.xml. You can find instructions for converting this .bnk to .xml, as well as extracting the linked sound files themselves, [here](/Tutorials/Sound/Extract-Audio).

This file is *very* large! Use the search function with your copied SoundEventID and you will find only one result, though, a CAkEvent object:

```xml
<obj na="CAkEvent" ix="17401">
   <fld ty="u8" na="eHircType" va="4" vf="0x04 [Event]"/>
   <fld ty="u32" na="dwSectionSize" va="13" vf="0x0D"/>
   <fld ty="sid" na="ulID" va="1053678736"/>
   <obj na="EventInitialValues">
    <fld ty="var" na="ulActionListSize" va="2"/>
    <lst na="actions" co="2">
     <obj na="Action" ix="0">
      <fld ty="tid" na="ulActionID" va="676495828"/>
     </obj>
     <obj na="Action" ix="1">
      <fld ty="tid" na="ulActionID" va="1017479151"/>
     </obj>
    </lst>
   </obj>
  </obj>
```

From here, we need the ulActionID(s). Some events will have only one, others will have multiple. We want to search the document for both these IDs until we find a "CAkActionPlay" object, which in this case we got from searching for the Event's second ulActionID, `"1017479151"`:

```xml
<obj na="CAkActionPlay" ix="17400">
   <fld ty="u8" na="eHircType" va="3" vf="0x03 [Action]"/>
   <fld ty="u32" na="dwSectionSize" va="22" vf="0x16"/>
   <fld ty="sid" na="ulID" va="1017479151"/>
   <fld ty="u16" na="ulActionType" va="1027" vf="0x0403 [Play]"/>
   <obj na="ActionInitialValues">
    <fld ty="tid" na="idExt" va="254604354"/>
    <fld ty="u8" na="idExt_4" va="0" vf="0x00">
     <fld ty="bit0" na="bIsBus" va="0"/>
    </fld>
    <obj na="AkPropBundle<AkPropValue,unsigned char>">
     <fld ty="u8" na="cProps" va="0"/>
     <lst na="pProps" co="0"/>
    </obj>
    <obj na="AkPropBundle<RANGED_MODIFIERS<AkPropValue>>">
     <fld ty="u8" na="cProps" va="0"/>
     <lst na="pProps" co="0"/>
    </obj>
    <obj na="PlayActionParams">
     <fld ty="u8" na="byBitVector" va="4" vf="0x04">
      <fld ty="bit0" na="eFadeCurve" va="4" vf="4 [Linear]"/>
     </fld>
     <fld ty="tid" na="bankID" va="206361915" hn="VOCALS"/>
     <fld ty="u32" na="bankType" va="0" vf="0x0000 [None]"/>
    </obj>
   </obj>
  </obj>
```

What we want from the CAkActionPlay is the “idExt,” here, `"254604354"`. This is the next term we need to search the soundbank for.

What we find is multiple different types of matches, but the ones we need are the "DirectParentID" of various "CAkSwitchCntr" sections. I like to add notes to the first line of each of these containers for better organization, of the original SoundEvent name we started with back in the merged.lsf(x). For this tutorial, that's `<!-- "BGClickReaction_ReptAction_MoveTo" -->`. From here, scroll down to the `<obj na="Children">` line.

```xml
<obj na="CAkSwitchCntr" ix="8217"> <!-- "BGClickReaction_ReptAction_MoveTo" -->
   <fld ty="u8" na="eHircType" va="6" vf="0x06 [Switch Container]"/>
   <fld ty="u32" na="dwSectionSize" va="148" vf="0x94"/>
   <fld ty="sid" na="ulID" va="1052821107"/>
   <obj na="SwitchCntrInitialValues">
    <obj na="NodeBaseParams">
     <obj na="NodeInitialFxParams">
      <fld ty="u8" na="bIsOverrideParentFX" va="0" vf="0x00"/>
      <fld ty="u8" na="uNumFx" va="0"/>
     </obj>
     <fld ty="u8" na="bIsOverrideParentMetadata" va="0" vf="0x00"/>
     <fld ty="u8" na="uNumFx" va="0"/>
     <fld ty="u8" na="bOverrideAttachmentParams" va="0" vf="0x00"/>
     <fld ty="tid" na="OverrideBusId" va="0"/>
     <fld ty="tid" na="DirectParentID" va="254604354"/>
     <fld ty="u8" na="byBitVector" va="0" vf="0x00">
      <fld ty="bit0" na="bPriorityOverrideParent" va="0"/>
      <fld ty="bit1" na="bPriorityApplyDistFactor" va="0"/>
      <fld ty="bit2" na="bOverrideMidiEventsBehavior" va="0"/>
      <fld ty="bit3" na="bOverrideMidiNoteTracking" va="0"/>
      <fld ty="bit4" na="bEnableMidiNoteTracking" va="0"/>
      <fld ty="bit5" na="bIsMidiBreakLoopOnNoteOff" va="0"/>
     </fld>
     <obj na="NodeInitialParams">
      <obj na="AkPropBundle<AkPropValue,unsigned char>">
       <fld ty="u8" na="cProps" va="0"/>
       <lst na="pProps" co="0"/>
      </obj>
      <obj na="AkPropBundle<RANGED_MODIFIERS<AkPropValue>>">
       <fld ty="u8" na="cProps" va="0"/>
       <lst na="pProps" co="0"/>
      </obj>
     </obj>
     <obj na="PositioningParams">
      <fld ty="u8" na="uBitsPositioning" va="0" vf="0x00">
       <fld ty="bit0" na="bPositioningInfoOverrideParent" va="0"/>
       <fld ty="bit1" na="bHasListenerRelativeRouting" va="0"/>
       <fld ty="bit2" na="ePannerType" va="0" vf="0 [DirectSpeakerAssignment]"/>
       <fld ty="bit5" na="e3DPositionType" va="0" vf="0 [Emitter]"/>
      </fld>
     </obj>
     <obj na="AuxParams">
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit2" na="bOverrideUserAuxSends" va="0"/>
       <fld ty="bit3" na="bHasAux" va="0"/>
       <fld ty="bit4" na="bOverrideReflectionsAuxBus" va="0"/>
      </fld>
      <fld ty="tid" na="reflectionsAuxBus" va="0"/>
     </obj>
     <obj na="AdvSettingsParams">
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bKillNewest" va="0"/>
       <fld ty="bit1" na="bUseVirtualBehavior" va="0"/>
       <fld ty="bit3" na="bIgnoreParentMaxNumInst" va="0"/>
       <fld ty="bit4" na="bIsVVoicesOptOverrideParent" va="0"/>
      </fld>
      <fld ty="u8" na="eVirtualQueueBehavior" va="1" vf="0x01 [FromElapsedTime]"/>
      <fld ty="u16" na="u16MaxNumInstance" va="0"/>
      <fld ty="u8" na="eBelowThresholdBehavior" va="0" vf="0x00 [ContinueToPlay]"/>
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bOverrideHdrEnvelope" va="0"/>
       <fld ty="bit1" na="bOverrideAnalysis" va="0"/>
       <fld ty="bit2" na="bNormalizeLoudness" va="0"/>
       <fld ty="bit3" na="bEnableEnvelope" va="0"/>
      </fld>
     </obj>
     <obj na="StateChunk">
      <fld ty="var" na="ulNumStateProps" va="0"/>
      <lst na="stateProps" co="0"/>
      <fld ty="var" na="ulNumStateGroups" va="0"/>
      <lst na="pStateChunks" co="0"/>
     </obj>
     <obj na="InitialRTPC">
      <fld ty="u16" na="uNumCurves" va="0"/>
      <lst na="pRTPCMgr" co="0"/>
     </obj>
    </obj>
    <fld ty="u8" na="eGroupType" va="0" vf="0x00 [Switch]"/>
    <fld ty="tid" na="ulGroupID" va="1194675850"/>
    <fld ty="tid" na="ulDefaultSwitch" va="0"/>
    <fld ty="u8" na="bIsContinuousValidation" va="0" vf="0x00"/>
    <obj na="Children">
     <fld ty="u32" na="ulNumChilds" va="3"/>
     <fld ty="tid" na="ulChildID" va="43248976"/>
     <fld ty="tid" na="ulChildID" va="487431427"/>
     <fld ty="tid" na="ulChildID" va="527576120"/>
    </obj>
    <fld ty="u32" na="ulNumSwitchGroups" va="3"/>
    <lst na="SwitchList" co="3">
     <obj na="CAkSwitchPackage" ix="0">
      <fld ty="sid" na="ulSwitchID" va="2764240573"/>
      <fld ty="u32" na="ulNumItems" va="1"/>
      <obj na="NodeList">
       <fld ty="tid" na="NodeID" va="527576120"/>
      </obj>
     </obj>
     <obj na="CAkSwitchPackage" ix="1">
      <fld ty="sid" na="ulSwitchID" va="1160234136"/>
      <fld ty="u32" na="ulNumItems" va="1"/>
      <obj na="NodeList">
       <fld ty="tid" na="NodeID" va="43248976"/>
      </obj>
     </obj>
     <obj na="CAkSwitchPackage" ix="2">
      <fld ty="sid" na="ulSwitchID" va="3418139957"/>
      <fld ty="u32" na="ulNumItems" va="1"/>
      <obj na="NodeList">
       <fld ty="tid" na="NodeID" va="487431427"/>
      </obj>
     </obj>
    </lst>
    <fld ty="u32" na="ulNumSwitchParams" va="3"/>
    <lst na="rParams" co="3">
     <obj na="AkSwitchNodeParams" ix="0">
      <fld ty="tid" na="ulNodeID" va="527576120"/>
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bIsFirstOnly" va="0"/>
       <fld ty="bit1" na="bContinuePlayback" va="0"/>
      </fld>
      <fld ty="u8" na="byBitVector" va="1" vf="0x01">
       <fld ty="bit0" na="eOnSwitchMode" va="1" vf="1 [Stop]"/>
      </fld>
      <fld ty="s32" na="FadeOutTime" va="0"/>
      <fld ty="s32" na="FadeInTime" va="0"/>
     </obj>
     <obj na="AkSwitchNodeParams" ix="1">
      <fld ty="tid" na="ulNodeID" va="43248976"/>
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bIsFirstOnly" va="0"/>
       <fld ty="bit1" na="bContinuePlayback" va="0"/>
      </fld>
      <fld ty="u8" na="byBitVector" va="1" vf="0x01">
       <fld ty="bit0" na="eOnSwitchMode" va="1" vf="1 [Stop]"/>
      </fld>
      <fld ty="s32" na="FadeOutTime" va="0"/>
      <fld ty="s32" na="FadeInTime" va="0"/>
     </obj>
     <obj na="AkSwitchNodeParams" ix="2">
      <fld ty="tid" na="ulNodeID" va="487431427"/>
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bIsFirstOnly" va="0"/>
       <fld ty="bit1" na="bContinuePlayback" va="0"/>
      </fld>
      <fld ty="u8" na="byBitVector" va="1" vf="0x01">
       <fld ty="bit0" na="eOnSwitchMode" va="1" vf="1 [Stop]"/>
      </fld>
      <fld ty="s32" na="FadeOutTime" va="0"/>
      <fld ty="s32" na="FadeInTime" va="0"/>
     </obj>
    </lst>
   </obj>
  </obj>
```

We can see there are three “Children” listed. Different CAkSwitchCntr entries will have different numbers of ulChildID's. Take these and search for them, we're now looking for where the matches are the DirectParentID of one of two objects: either a "CAkRanSeqCntr" or a "CAkSound," depending on the complexity of the event's variations. For this event, there's three variations, so we get "CAkRanSeqCntr" results, like this one below. If your results for your seatch are DirectParentIDs of a CAkSound, skip this next step.

```xml
<obj na="CAkRanSeqCntr" ix="8127">
   <fld ty="u8" na="eHircType" va="5" vf="0x05 [Random/Sequence Container]"/>
   <fld ty="u32" na="dwSectionSize" va="318" vf="0x13E"/>
   <fld ty="sid" na="ulID" va="32089990"/>
   <obj na="RanSeqCntrInitialValues">
    <obj na="NodeBaseParams">
     <obj na="NodeInitialFxParams">
      <fld ty="u8" na="bIsOverrideParentFX" va="0" vf="0x00"/>
      <fld ty="u8" na="uNumFx" va="0"/>
     </obj>
     <fld ty="u8" na="bIsOverrideParentMetadata" va="0" vf="0x00"/>
     <fld ty="u8" na="uNumFx" va="0"/>
     <fld ty="u8" na="bOverrideAttachmentParams" va="0" vf="0x00"/>
     <fld ty="tid" na="OverrideBusId" va="0"/>
     <fld ty="tid" na="DirectParentID" va="43248976"/>
     <fld ty="u8" na="byBitVector" va="0" vf="0x00">
      <fld ty="bit0" na="bPriorityOverrideParent" va="0"/>
      <fld ty="bit1" na="bPriorityApplyDistFactor" va="0"/>
      <fld ty="bit2" na="bOverrideMidiEventsBehavior" va="0"/>
      <fld ty="bit3" na="bOverrideMidiNoteTracking" va="0"/>
      <fld ty="bit4" na="bEnableMidiNoteTracking" va="0"/>
      <fld ty="bit5" na="bIsMidiBreakLoopOnNoteOff" va="0"/>
     </fld>
     <obj na="NodeInitialParams">
      <obj na="AkPropBundle<AkPropValue,unsigned char>">
       <fld ty="u8" na="cProps" va="0"/>
       <lst na="pProps" co="0"/>
      </obj>
      <obj na="AkPropBundle<RANGED_MODIFIERS<AkPropValue>>">
       <fld ty="u8" na="cProps" va="0"/>
       <lst na="pProps" co="0"/>
      </obj>
     </obj>
     <obj na="PositioningParams">
      <fld ty="u8" na="uBitsPositioning" va="0" vf="0x00">
       <fld ty="bit0" na="bPositioningInfoOverrideParent" va="0"/>
       <fld ty="bit1" na="bHasListenerRelativeRouting" va="0"/>
       <fld ty="bit2" na="ePannerType" va="0" vf="0 [DirectSpeakerAssignment]"/>
       <fld ty="bit5" na="e3DPositionType" va="0" vf="0 [Emitter]"/>
      </fld>
     </obj>
     <obj na="AuxParams">
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit2" na="bOverrideUserAuxSends" va="0"/>
       <fld ty="bit3" na="bHasAux" va="0"/>
       <fld ty="bit4" na="bOverrideReflectionsAuxBus" va="0"/>
      </fld>
      <fld ty="tid" na="reflectionsAuxBus" va="0"/>
     </obj>
     <obj na="AdvSettingsParams">
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bKillNewest" va="0"/>
       <fld ty="bit1" na="bUseVirtualBehavior" va="0"/>
       <fld ty="bit3" na="bIgnoreParentMaxNumInst" va="0"/>
       <fld ty="bit4" na="bIsVVoicesOptOverrideParent" va="0"/>
      </fld>
      <fld ty="u8" na="eVirtualQueueBehavior" va="1" vf="0x01 [FromElapsedTime]"/>
      <fld ty="u16" na="u16MaxNumInstance" va="0"/>
      <fld ty="u8" na="eBelowThresholdBehavior" va="0" vf="0x00 [ContinueToPlay]"/>
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bOverrideHdrEnvelope" va="0"/>
       <fld ty="bit1" na="bOverrideAnalysis" va="0"/>
       <fld ty="bit2" na="bNormalizeLoudness" va="0"/>
       <fld ty="bit3" na="bEnableEnvelope" va="0"/>
      </fld>
     </obj>
     <obj na="StateChunk">
      <fld ty="var" na="ulNumStateProps" va="0"/>
      <lst na="stateProps" co="0"/>
      <fld ty="var" na="ulNumStateGroups" va="0"/>
      <lst na="pStateChunks" co="0"/>
     </obj>
     <obj na="InitialRTPC">
      <fld ty="u16" na="uNumCurves" va="0"/>
      <lst na="pRTPCMgr" co="0"/>
     </obj>
    </obj>
    <fld ty="u16" na="sLoopCount" va="1"/>
    <fld ty="u16" na="sLoopModMin" va="0"/>
    <fld ty="u16" na="sLoopModMax" va="0"/>
    <fld ty="f32" na="fTransitionTime" va="1000.0"/>
    <fld ty="f32" na="fTransitionTimeModMin" va="0.0"/>
    <fld ty="f32" na="fTransitionTimeModMax" va="0.0"/>
    <fld ty="u16" na="wAvoidRepeatCount" va="1"/>
    <fld ty="u8" na="eTransitionMode" va="0" vf="0x00 [Disabled]"/>
    <fld ty="u8" na="eRandomMode" va="1" vf="0x01 [Shuffle]"/>
    <fld ty="u8" na="eMode" va="0" vf="0x00 [Random]"/>
    <fld ty="u8" na="byBitVector" va="18" vf="0x12">
     <fld ty="bit0" na="_bIsUsingWeight" va="0"/>
     <fld ty="bit1" na="bResetPlayListAtEachPlay" va="1"/>
     <fld ty="bit2" na="bIsRestartBackward" va="0"/>
     <fld ty="bit3" na="bIsContinuous" va="0"/>
     <fld ty="bit4" na="bIsGlobal" va="1"/>
    </fld>
    <obj na="Children">
     <fld ty="u32" na="ulNumChilds" va="21"/>
     <fld ty="tid" na="ulChildID" va="119788967"/>
     <fld ty="tid" na="ulChildID" va="181035554"/>
     <fld ty="tid" na="ulChildID" va="186996580"/>
     <fld ty="tid" na="ulChildID" va="233445023"/>
     <fld ty="tid" na="ulChildID" va="294749589"/>
     <fld ty="tid" na="ulChildID" va="343922165"/>
     <fld ty="tid" na="ulChildID" va="368961440"/>
     <fld ty="tid" na="ulChildID" va="387063020"/>
     <fld ty="tid" na="ulChildID" va="429323929"/>
     <fld ty="tid" na="ulChildID" va="448016407"/>
     <fld ty="tid" na="ulChildID" va="454021811"/>
     <fld ty="tid" na="ulChildID" va="471252354"/>
     <fld ty="tid" na="ulChildID" va="481481881"/>
     <fld ty="tid" na="ulChildID" va="529877422"/>
     <fld ty="tid" na="ulChildID" va="542586646"/>
     <fld ty="tid" na="ulChildID" va="572735731"/>
     <fld ty="tid" na="ulChildID" va="655702997"/>
     <fld ty="tid" na="ulChildID" va="712432745"/>
     <fld ty="tid" na="ulChildID" va="735216418"/>
     <fld ty="tid" na="ulChildID" va="960209531"/>
     <fld ty="tid" na="ulChildID" va="1017850951"/>
    </obj>
    <obj na="CAkPlayList">
     <fld ty="u16" na="ulPlayListItem" va="21"/>
     <lst na="pItems" co="21">
      <obj na="AkPlaylistItem" ix="0">
       <fld ty="tid" na="ulPlayID" va="712432745"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="1">
       <fld ty="tid" na="ulPlayID" va="368961440"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="2">
       <fld ty="tid" na="ulPlayID" va="343922165"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="3">
       <fld ty="tid" na="ulPlayID" va="387063020"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="4">
       <fld ty="tid" na="ulPlayID" va="454021811"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="5">
       <fld ty="tid" na="ulPlayID" va="186996580"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="6">
       <fld ty="tid" na="ulPlayID" va="429323929"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="7">
       <fld ty="tid" na="ulPlayID" va="735216418"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="8">
       <fld ty="tid" na="ulPlayID" va="448016407"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="9">
       <fld ty="tid" na="ulPlayID" va="572735731"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="10">
       <fld ty="tid" na="ulPlayID" va="542586646"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="11">
       <fld ty="tid" na="ulPlayID" va="119788967"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="12">
       <fld ty="tid" na="ulPlayID" va="960209531"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="13">
       <fld ty="tid" na="ulPlayID" va="655702997"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="14">
       <fld ty="tid" na="ulPlayID" va="233445023"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="15">
       <fld ty="tid" na="ulPlayID" va="481481881"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="16">
       <fld ty="tid" na="ulPlayID" va="1017850951"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="17">
       <fld ty="tid" na="ulPlayID" va="181035554"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="18">
       <fld ty="tid" na="ulPlayID" va="294749589"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="19">
       <fld ty="tid" na="ulPlayID" va="471252354"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
      <obj na="AkPlaylistItem" ix="20">
       <fld ty="tid" na="ulPlayID" va="529877422"/>
       <fld ty="s32" na="weight" va="50000"/>
      </obj>
     </lst>
    </obj>
   </obj>
  </obj>
```

Now we'll search for the CAkRanSeqCntr's children, where finally one of the matches will be the ulID of a CAkSound event. You might also find CAkSound events using their DirectParentIDs from a CAkSwitchCntr's Children entries, depending on what kind of event you're saearching, but once you've got to the CAkSound, all that matters is its “sourceID.” This is the name of the actual .wem file the code points to.

```xml
<obj na="CAkSound" ix="8106">
   <fld ty="u8" na="eHircType" va="2" vf="0x02 [Sound]"/>
   <fld ty="u32" na="dwSectionSize" va="66" vf="0x42"/>
   <fld ty="sid" na="ulID" va="119788967"/>
   <obj na="SoundInitialValues">
    <obj na="AkBankSourceData">
     <fld ty="u32" na="ulPluginID" va="262145" vf="0x00040001 [VORBIS]">
      <fld ty="u16" na="type" va="1" vf="0x01 [Codec]"/>
      <fld ty="u16" na="company" va="0" vf="0x00 [Audiokinetic]"/>
     </fld>
     <fld ty="u8" na="StreamType" va="2" vf="0x02 [Streaming]"/>
     <obj na="AkMediaInformation">
      <fld ty="tid" na="sourceID" va="880791538"/>
      <fld ty="u32" na="uInMemoryMediaSize" va="3530" vf="0xDCA"/>
      <fld ty="u8" na="uSourceBits" va="0" vf="0x00">
       <fld ty="bit0" na="bIsLanguageSpecific" va="0"/>
       <fld ty="bit1" na="bPrefetch" va="0"/>
       <fld ty="bit3" na="bNonCachable" va="0"/>
       <fld ty="bit7" na="bHasSource" va="0"/>
      </fld>
     </obj>
    </obj>
    <obj na="NodeBaseParams">
     <obj na="NodeInitialFxParams">
      <fld ty="u8" na="bIsOverrideParentFX" va="0" vf="0x00"/>
      <fld ty="u8" na="uNumFx" va="0"/>
     </obj>
     <fld ty="u8" na="bIsOverrideParentMetadata" va="0" vf="0x00"/>
     <fld ty="u8" na="uNumFx" va="0"/>
     <fld ty="u8" na="bOverrideAttachmentParams" va="0" vf="0x00"/>
     <fld ty="tid" na="OverrideBusId" va="0"/>
     <fld ty="tid" na="DirectParentID" va="32089990"/>
     <fld ty="u8" na="byBitVector" va="0" vf="0x00">
      <fld ty="bit0" na="bPriorityOverrideParent" va="0"/>
      <fld ty="bit1" na="bPriorityApplyDistFactor" va="0"/>
      <fld ty="bit2" na="bOverrideMidiEventsBehavior" va="0"/>
      <fld ty="bit3" na="bOverrideMidiNoteTracking" va="0"/>
      <fld ty="bit4" na="bEnableMidiNoteTracking" va="0"/>
      <fld ty="bit5" na="bIsMidiBreakLoopOnNoteOff" va="0"/>
     </fld>
     <obj na="NodeInitialParams">
      <obj na="AkPropBundle<AkPropValue,unsigned char>">
       <fld ty="u8" na="cProps" va="0"/>
       <lst na="pProps" co="0"/>
      </obj>
      <obj na="AkPropBundle<RANGED_MODIFIERS<AkPropValue>>">
       <fld ty="u8" na="cProps" va="0"/>
       <lst na="pProps" co="0"/>
      </obj>
     </obj>
     <obj na="PositioningParams">
      <fld ty="u8" na="uBitsPositioning" va="0" vf="0x00">
       <fld ty="bit0" na="bPositioningInfoOverrideParent" va="0"/>
       <fld ty="bit1" na="bHasListenerRelativeRouting" va="0"/>
       <fld ty="bit2" na="ePannerType" va="0" vf="0 [DirectSpeakerAssignment]"/>
       <fld ty="bit5" na="e3DPositionType" va="0" vf="0 [Emitter]"/>
      </fld>
     </obj>
     <obj na="AuxParams">
      <fld ty="u8" na="byBitVector" va="8" vf="0x08">
       <fld ty="bit2" na="bOverrideUserAuxSends" va="0"/>
       <fld ty="bit3" na="bHasAux" va="1"/>
       <fld ty="bit4" na="bOverrideReflectionsAuxBus" va="0"/>
      </fld>
      <fld ty="tid" na="auxID" va="3473647148"/>
      <fld ty="tid" na="auxID" va="1518716931"/>
      <fld ty="tid" na="auxID" va="0"/>
      <fld ty="tid" na="auxID" va="0"/>
      <fld ty="tid" na="reflectionsAuxBus" va="0"/>
     </obj>
     <obj na="AdvSettingsParams">
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bKillNewest" va="0"/>
       <fld ty="bit1" na="bUseVirtualBehavior" va="0"/>
       <fld ty="bit3" na="bIgnoreParentMaxNumInst" va="0"/>
       <fld ty="bit4" na="bIsVVoicesOptOverrideParent" va="0"/>
      </fld>
      <fld ty="u8" na="eVirtualQueueBehavior" va="1" vf="0x01 [FromElapsedTime]"/>
      <fld ty="u16" na="u16MaxNumInstance" va="0"/>
      <fld ty="u8" na="eBelowThresholdBehavior" va="0" vf="0x00 [ContinueToPlay]"/>
      <fld ty="u8" na="byBitVector" va="0" vf="0x00">
       <fld ty="bit0" na="bOverrideHdrEnvelope" va="0"/>
       <fld ty="bit1" na="bOverrideAnalysis" va="0"/>
       <fld ty="bit2" na="bNormalizeLoudness" va="0"/>
       <fld ty="bit3" na="bEnableEnvelope" va="0"/>
      </fld>
     </obj>
     <obj na="StateChunk">
      <fld ty="var" na="ulNumStateProps" va="0"/>
      <lst na="stateProps" co="0"/>
      <fld ty="var" na="ulNumStateGroups" va="0"/>
      <lst na="pStateChunks" co="0"/>
     </obj>
     <obj na="InitialRTPC">
      <fld ty="u16" na="uNumCurves" va="0"/>
      <lst na="pRTPCMgr" co="0"/>
     </obj>
    </obj>
   </obj>
  </obj>
```

Now all that's left to do is listen to it to find out exactly what sound it is! Search for that string of numbers wherever you've unpacked your SharedSounds.pak, or converted its .wem files to .wav. For this example, it's `"880791538"`. From listening to it, we now know that it's Player Voice 7 saying “Breathe deep, and move.”

This is a long, tedious, repetitive process. Now that you understand how to do it, here's a tip to speed things up:

In between CAkSwitchCntr/CAkRanSeqCntr entries will always be the same category - for this example, they will all be different point & click lines that play for a specific voice when you click on the ground to move to a location. The CAkRanSeqCntr's in between CAkSwitchCntr's break up the distinguishments of whether you're moving normally, in combat, or sneaking.   
For another soundbank, it could be all the different recordings of the same spell shout, or footsteps, etc.

There is also a video tutorial covering this whole process, as well as usage of the [BG3 Soundbank Source Grabber](https://github.com/TrampolineTales/BG3SoundBankSourceGrabber) tool for creating search queries of multiple SourceIDs at once, available [here](https://www.youtube.com/watch?v=zt9zGqRqJoo).

Credits:

These instructions are a modified, expanded version of instructions written by Nexus user [tepig327](https://www.nexusmods.com/baldursgate3/users/106327958).