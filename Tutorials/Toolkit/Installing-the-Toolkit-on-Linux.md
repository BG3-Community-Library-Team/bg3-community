---
title: Installing the Toolkit on Linux
description: Toolkit Linux Guide
published: false
date: 2025-03-04T13:31:21.612Z
tags: linux, toolkit
editor: markdown
dateCreated: 2025-02-24T16:01:49.767Z
---

# How to install the Larian Studios - Baldurs Gate 3 Toolkit on Linux

To get things out of the way immediately... how you can install the Toolkit varies depending on your distro.
Each distro tab will feature only its own way of installing it, so choose the one whichever fits yours.
In addition to this, this guide is created based on a snapshot of our current understanding. If there are changes to the toolkit or your distro (updates) or you are using a different version than what we were able to make run, this might be something you have to figure out yourself or ask around for.

# Sections {.tabset}

## Ubuntu
### Tested on Ubuntu 24.04

{.links-list}

This guide explains how to install and run the Baldur's Gate 3 Toolkit on Linux using a virtual machine as a workaround for compatibility issues. It is based on tests performed on Ubuntu 24.04.1 LTS with Steam (Snap version) and an NVIDIA GTX 1650 GPU.

### Introduction

Running the Baldur's Gate 3 Toolkit on Linux can be challenging due to compatibility issues with Wine and Proton. After multiple attempts to run the toolkit using Wine 10.0 and Proton (via the Snap version of Steam), I found that while the application would start, the render window failed to display anything.

After extensive testing, the most reliable solution was to run the toolkit on a Windows 10 Tiny virtual machine using VMware Workstation. This guide outlines the steps needed to set up this environment.

### Test Environment

- VMware Workstation 17 Pro (17.6.2 build-24409262)
- Windows 10 Tiny ISO (lightweight version of Windows 10)
- Steam (Snap version) with the latest Proton
- Baldur's Gate 3 Toolkit and Game files (installed on Linux host)
- Tested with: Lenovo IdeaPad Gaming 3 / NVIDIA GTX 1650 / 32 GB RAM
![ubuntu_test_specs.png](/tutorials/install-toolkit-linux/ubuntu_test_specs.png)

### Initial Attempts and Issues

The initial attempt was to run the toolkit using Proton and Wine 10.0. Here are the findings:

1. The toolkit launches but the render window fails to display anything, even with the 'shaking-thing' workaround.
2. Logs are flooded with errors, eventually leading to a crash.
3. Experimented with:
```
- Different DXVK settings
- Forcing the NVIDIA GPU as the primary Vulkan device
- Comparing native Wayland vs. XWayland performance
```
4. A custom bash script and DXVK configuration were used but didn't resolve the rendering issues. You can check the configuration here: [DXVK Config and Script](https://gist.github.com/nandez/b4b35095ef7e619be95eb9e2bbc9f39d).



After spending a full day trying to make it work natively on Linux, I opted for a virtual machine solution. I installed VMware Workstation and set up a Windows 10 Tiny VM. This allowed me to:

```
- Share both the game and toolkit folders from the Linux host to the VM,
  avoiding redundant downloads.
- Enable 3D graphics acceleration, which resolved the rendering issues.
- Achieve a "stable" environment where the toolkit runs...
```


### Setting up Windows 10 VM

1. Download and Install VMware Workstation Pro
- Download the bundle from [Broadcom site](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Workstation%20Pro&displayGroup=VMware%20Workstation%20Pro%2017.0%20for%20Linux&release=17.6.2&os=&servicePk=526673&language=EN)
(you may need to create an account to sign in)
- Install using the following commands:

```bash
sudo apt update
sudo apt install build-essential
sudo ./VMware-Workstation-Full-*.bundle
```
2. Launch VMWare and create a new virtual machine.
- Select the Windows 10 Tiny ISO (or whatever image you want to use)
- Allocate the following resources:

![win10_vm_settings.png](/tutorials/install-toolkit-linux/win10_vm_settings.png)

| Device | Summary |
|--|--|
| RAM | >= 16GB (The toolkit used at least 10 GB while testing) |
| Processors | 8 (Recommended) |
| HD | ~30 GB (Since the toolkit and game are not installed in the VM, a smaller disk might suffice). |
| GPU | 3D graphics acceleration enabled (*) <br/><br/>Settings -> Display -> 3D Graphics -> Accelerate 3d Graphics. Allocate 8 GB for graphics memory. |


<details>
  <summary>(*) VMware Virtual GPU</summary>
  VMware uses a virtual GPU for 3D acceleration, translating DirectX commands to the host GPU hardware.

>...With 3D acceleration the guest OS gets access to a virtual GPU that understands GPU-specific features such as DirectX. The VM driver+virtual hardware translates the 3D accelaration commands that it receives and executes those on the GPU hardware. Since VMware Workstation 15.5 it uses a special sandboxed process for that...

  More details can be found here:
  - [VMware Workstation 17 Pro supports use of host GPU?](https://community.broadcom.com/vmware-cloud-foundation/communities/community-home/digestviewer/viewthread?MessageKey=c9a72dbf-f2c7-4882-a944-de035fdcee3c&CommunityKey=fb707ac3-9412-4fad-b7af-018f5da56d9f#bmc9a72dbf-f2c7-4882-a944-de035fdcee3c)
  - [Sandboxed Graphics Processes](https://blogs.vmware.com/workstation/2020/05/directx-11-now-with-workstation-tp20h2.html)
  
</details>

3. Configuring Shared Folders
- In VMware Workstation, got to **VM > Settings -> Options -> Shared Folders**.
- Select **Always Enabled** and map both the Toolkit installation path and the Game path.

![vm_shared_folders.png](/tutorials/install-toolkit-linux/vm_shared_folders.png)

4. Launch the VM and follow the Windows installation process.

### Running Toolkit

1. Inside the VM, navigate to Network -> vmware-host -> Shared Folders, to find the game and toolkit installation folders from the linux host.

![bg3_folders_win10_vm.png](/tutorials/install-toolkit-linux/bg3_folders_win10_vm.png)

2. Launch the toolkit (Glasses.exe) from inside the BG3 Toolkit installation folder.

![bg3_toolkit_win10_vm.png](/tutorials/install-toolkit-linux/bg3_toolkit_win10_vm.png)

3. Select the Data folder from the Baldur's Gate 3 installation path and click ok.

4. Wait for editor to load up.

![bg3_running_toolkit_win10_vm.png](/tutorials/install-toolkit-linux/bg3_running_toolkit_win10_vm.png)

This guide is meant to be a walkthrough to help others successfully run the Baldur's Gate 3 Toolkit on Linux using a Windows 10 VM as a workaround. As stated before, this is by no means a comprehensive guide, and for simplicity, some steps are skipped. This is a workaround developed after a lot of trial and error, so some steps might be different for you depending on your hardware specifications and/or Linux distribution.

## Arch
### Tested on 6.13.2-arch1-1 - x86_64 - x11


{.links-list}


## Fedora
### Tested on Fedora 41


{.links-list}