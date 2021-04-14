%undefine _debugsource_packages
%global _firmwarepath   /usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:          brcm-firmware
Version:       0.20180401
Release:       2
Summary:       brcm firmware for various WiFi and Bluetooth devices
# Broadcom/Cyprus can't fucking work it out themselves
License:       Proprietary
# The Cyprus, nee Broadcom Wireless drivers need a brcmfmac<model>-sdio.txt or 
# brcmfmac<model>-pcie.txt that they don't redistribute with their firmware for
# various reasons which aren't really clear. This is a collection of them.
# The various files needed are documented in the following two files in the kernel
# drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c
# drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c
# Recnetly they've also added loading of brcmfmac<model>-<interface>.clm_blob 
# for "regulatory constraints" (hello that's what the damn crda interface is for!)

# The first of these come from the RPi Foundation
# https://github.com/RPi-Distro/firmware-nonfree/tree/master/brcm
Source1:       brcmfmac43430-sdio.txt
Source2:       brcmfmac43455-sdio.txt
Source3:       brcmfmac43455-sdio.clm_blob
# Source5:       brcmfmac43143-sdio.txt
# Source6:       brcmfmac43241b0-sdio.txt
# Source7:       brcmfmac43241b4-sdio.txt
# Source8:       brcmfmac43241b5-sdio.txt
# https://raw.githubusercontent.com/OpenELEC/wlan-firmware/master/firmware/brcm/brcmfmac4329-sdio.txt
Source9:       brcmfmac4329-sdio.txt
# https://raw.githubusercontent.com/OpenELEC/wlan-firmware/master/firmware/brcm/brcmfmac4330-sdio.txt
Source10:      brcmfmac4330-sdio.txt
# Source11:      brcmfmac4334-sdio.txt
# https://raw.githubusercontent.com/Asus-T100/firmware/master/brcm/brcmfmac43340-sdio.txt
Source12:      brcmfmac43340-sdio.txt
# Source13:      brcmfmac4335-sdio.txt
# Source14:      brcmfmac43362-sdio.txt
# Source15:      brcmfmac4339-sdio.txt
# Source16:      brcmfmac43430a0-sdio.txt
# Source17:      brcmfmac4354-sdio.txt
# Source18:      brcmfmac4356-sdio.txt
# Source19:      brcmfmac4373-sdio.txt
# Source20:      brcmfmac43602-pcie.txt
# Source21:      brcmfmac4350-pcie.txt
# Source22:      brcmfmac4350c2-pcie.txt
# Source23:      brcmfmac4356-pcie.txt
# Source24:      brcmfmac43570-pcie.txt
# Source25:      brcmfmac4358-pcie.txt
# Source26:      brcmfmac4359-pcie.txt
# Source27:      brcmfmac4365b-pcie.txt
# Source28:      brcmfmac4365c-pcie.txt
# Source29:      brcmfmac4366b-pcie.txt
# Source30:      brcmfmac4366c-pcie.txt
# Source31:      brcmfmac4371-pcie.txt

# The first of these come from the RPi Foundation
# https://github.com/RPi-Distro/firmware-nonfree/tree/master/brcm
Source100:     BCM4345C0.hcd
# https://github.com/OpenELEC/misc-firmware/raw/master/firmware/brcm/BCM43430A1.hcd
Source101:     BCM43430A1.hcd

BuildArch:     noarch
BuildRequires: linux-firmware
Requires:      linux-firmware

%description
The missing bits of firmware, text files and other bits that actually make 
Broadcom and Cyprus wireless devices such as Bluetooth and WiFi actually 
work in Linux almost out of the box.

%prep

%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE1} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE2} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE3} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE9} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE10} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE12} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE100} %{buildroot}/%{_firmwarepath}/brcm/
install -p %{SOURCE101} %{buildroot}/%{_firmwarepath}/brcm/

%files
%{_firmwarepath}/brcm/*

%changelog
* Sun Apr  1 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.20180401-1
- Initial package
