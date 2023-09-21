%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build
%undefine __arch_install_post

Name: live-usb-install
Summary: Install various Linux distributions from ISO, CD/DVD, Internet or IMG file to USB flash drive.
Version: 2.5.3
Release: 1
Group: USU Packages
License: Free Software
URL: https://live.learnfree.eu/
Source0: %{name}-%{version}.tar.gz
#BuildArch: noarch
BuildRequires: desktop-file-utils
#Requires: python2,
#Requires: python2-glade2,
#Requires: syslinux,
#Requires: wget,
#Requires: p7zip-full,
#Requires: unrar
#Requires: |
#Requires: unrar-free,
#Requires: hal
#Requires: |
#Requires: udev,
#Requires: parted,
#Requires: sudo

%description
Currently supports 125 distributions, with total 698 versions.
More info at https://live.learnfree.eu/
Supported distributins:  - AVG Rescue CD
- Agilia Linux
- Alpine
- Android x86
- Antix
- Aptosid
- Arios
- ArtistX
- Asturix
- BackBox
- Backtrack
- Beini
- Bodhi
- Bolix
- Calculate Linux
- Canaima
- CentOS
- Chakra
- CloneZilla
- CrunchBang Linux
- Damn Small Linux
- Debian Live
- Doudou
- Dr.Web LiveCD
- Dragora
- Dreamlinux
- Dynebolic
- EasyPeasy
- Elementary OS
- Elive
- F-Secure Rescue CD
- FaunOS
- Fedora
- Finnix
- FreeDOS
- GNUSTEP
- GParted Live CD
- GeeXBox
- Gentoo
- Greenie
- Grml
- Hirens Boot CD
- IPCop
- Imagine OS
- Jolicloud
- Kanotix
- Kaspersky Rescue Disk
- Kiwi
- Knoppix
- Kubuntu
- LinEx
- Linux Deepin
- Linux Mint
- LinuxCoin
- Linvo
- Lubuntu
- Macpup
- Madbox
- Mageia
- Mandriva
- MeeGo
- MoonOS
- Mythbuntu
- NTPasswd
- Network Security Toolkit
- NimbleX
- OpenSUSE
- Ophcrack
- PCLinuxOS
- Pardus
- Parted Magic
- PelicanHPC
- Peppermint OS
- Pinguy
- Puppy
- PureOS
- Puredyne
- Qimo
- Quirky
- ROSA
- RainOS
- Sabayon
- Sabily
- SalineOS
- Salix
- Scientific Linux
- SimplyMEPIS
- Slax
- Slitaz
- Sugar On A Stick
- SuperOS
- Superb Mini Server
- Supreme SuperGamer
- SystemRescueCD
- Tails
- Tiny Core Linux
- Trisquel
- USU
- Ubuntu
- Ubuntu GNOME
- Ubuntu Lite
- Ubuntu Netbook Remix
- Ubuntu Rescue Remix
- Ultilex
- Ultimate Boot CD
- UltimateEdition
- Unity Linux
- Vector Linux
- WattOS
- WebConverger
- WifiWay
- Wolvix
- Xen Livecd
- Xubuntu
- YLMF
- Zentyal
- Zenwalk
- ZevenOS
- Zorin OS
- eQuityOS
- edu.cd.svoboden.net
- gNewSense
- gOS
- live.linuX-gamers.net
- xPUD

%prep
%setup -q -n %{name}
sed -i -e 's|/usr/bin/env python$|/usr/bin/python2|' -e 's|/usr/bin/python$|/usr/bin/python2|' `find . -name '*.py'`

%build
cat > %{name} <<EOF
#!/usr/bin/bash
cd /usr/share/%{name}
python2 %{name}.py
EOF

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}
#mv %{buildroot}%{_datadir}/%{name}/locale %{buildroot}%{_datadir}
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}/usr/share/live-usb-install/tools/pypack/pypack

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
#{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.3
- Rebuilt for Fedora
