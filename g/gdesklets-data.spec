Name:           gdesklets-data
Version:        0.35.6
Release:        1
Summary:        Applets for gDesklets
Group:          User Interface/Desktops
License:        GPLv2
URL:            https://gdesklets.de/
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}_0.35.6-2ubuntu1.diff.gz
BuildArch:      noarch
Requires:       gdesklets
Vendor:		Clément Stenac <zorglub@debian.org>

%description
This package provides desklets for the gDesklets application and contains:
* ACPI 0.1 * Battery 0.3 * Bible-desklet 2.0.1 * BinaryClock 1.2 * Borders
* Boxmail 0.50 * BSRDG 0.1 * Bubblefishymon 0.1.1 * Bugzilla * Calendar 0.21
* CircleButtonBar 0.3 * Clock 0.50 * Another clock * XMMS * Cpuinfo
* Debian cow * Deskquotes 1.2 * Desktao 0.3 * DinoCam 1.0 * DiskIo 0.1
* DiskMount 0.3.2 * Displayconstraints0.1 * (Ebay 0.1.1) * Ebichuclock 0.1.1
* Ephemeride 1 * ExternIP 0.3.0 * Fortune * GnomeBar 2.0.2 * Goodtime 0.2
* Hddtemp 0.1 * HottieOfTheHour 0.3.1 * I2CTemp 0.12 * IconButton 0.1.4
* Image 0.1 * Imapmail 0.1 * Imonc 0.6 * Info * Infobar 0.3
* InfodomesticsBar 1.0 * Irc 1.2 * Juju Countdown2 0.1
* LinuxTag Edition 0.11 * Lmsensors 0.8 * LT-hddtemp * LTPager 0.1
* LTPagerSb 0.1 * LTVSeti 0.2 * LTVariations 0.26 * LTXmms 0.3 * Memo 0.1.4
* MemoOver 0.1.0 * Memory 0.2.0 * Mldonkey 0.1.2 * Modified xmms
* Multitail 0.3.1 * NetworkInfo * Ping 1.0.0 * Popmail 0.1.4 * Praytime 0.21
* Psi Battery 0.1 * Psi Launcher 1.0 * Psi Pager * Psi Seti 0.2
* Psi Small 0.5.1 * Psi Small Notify 0.01 * Psi Tasklist * Psi Tiny
* Psi Weather * Psi small * Rhythmlet 0.3g-r3 * Rss 0.1 * Rss-grab 0.6.4
* Seti * SideCandy 0.1 * SC-Diskinfo 0.10.2 * SC-HDDTemp 0.2 * SC-Mount 0.5
* SC-MPC 0.21 * SC-Popmail 0.1.3 * SC-PrintQueue 0.9 * SC-RAM 0.3.1
* SC-Sytadin 0.50 * SC-Users 1.4 * ShadowImage 0.2 * StarterBar 0.31.3
* Stockinfo 0.2 * StickyNotes 0.15 * SysInfo 0.25 * Sytadin 0.2
* Tasklist 0.10 * Temperature 0.2 * Themes 0.1.1 * Todo 0.1.1
* VariableBorder * Volume * Weather 0.26 * WeeklyCalendar 0.31
* Wireless 0.2 * XMLQuotes 2.4 * Xmms

%prep
%setup -q
%patch -p1
sed -i -e 's/^include/#include/' -e '/dh_/d' debian/rules
sed -i 's|/usr/bin/env python|/usr/bin/python2|' */*.bin */*/*.bin

%build
cat debian/dirs | while read i; do mkdir -p debian/%{name}$i; done
make -f debian/rules install

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -pr debian/%{name}/* %{buildroot}
rm -rf %{buildroot}%{_datadir}/gdesklets/Displays/ebay
sed -i 's/ callback="prefs_cb"//' %{buildroot}%{_datadir}/gdesklets/Displays/stickynotes/notes.display

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_datadir}/gdesklets/Sensors/Rss/rdfxml.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/gdesklets/Sensors/*/*.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/gdesklets/Sensors/*/*/*.py

%clean
rm -rf %{buildroot}

%files
%doc debian/{changelog,copyright,README.Debian}
%{_datadir}/gdesklets/*

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.35.6
- Rebuilt for Fedora
