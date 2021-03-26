#
# spec file for package domination
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           domination
Version:        1.1.1.6
Release:        lp150.9.3
Summary:        Board game that is a bit like the well known game Risk
License:        GPL-3.0
Group:          Amusements/Games/Strategy
Url:            http://domination.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Domination/%{version}/Domination_%{version}.zip
Source1:        %{name}-FlashGUI.sh
Source2:        %{name}-Increment1GUI.sh
Source3:        %{name}-SimpleGUI.sh
Source4:        %{name}-SwingGUI.sh
Source5:        %{name}.desktop
Source6:        %{name}.png
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  unzip
Requires:       %{name}-data
Requires:       jre >= 1.6.0
BuildArch:      noarch

%description
Domination is a board game that is a bit like the well known game Risk.

Domination is a game that is a bit like the well known board game of Risk
or RisiKo. It has many game options and includes many maps.

Written in java it includes a map editor, a simple map format, multiplayer
network play, single player, hotseat, 5 user interfaces and many more features,
it works in all OSs that run java.

%prep
%setup -q -n Domination

# Convert to unix line end
find -name "*.txt" -print0 -or -name "*.ini" -print0 -or -name "*.cmd" -print0 \
    -or -name "*.htm" -print0 -or -name "*.cards" -print0 -or -name "*.map" -print0 \
    -or -name "*.properties" -print0 | xargs -0 dos2unix

%build

%install
# install wrappers
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}-FlashGUI
install -Dm 0755 %{S:2} %{buildroot}%{_bindir}/%{name}-Increment1GUI
install -Dm 0755 %{S:3} %{buildroot}%{_bindir}/%{name}-SimpleGUI
install -Dm 0755 %{S:4} %{buildroot}%{_bindir}/%{name}-SwingGUI

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{help,lib,maps,maps/preview,resources}
for d in help lib resources ; do
   install -Dm 0644 $d/* %{buildroot}%{_datadir}/%{name}/$d
done

cp -a maps %{buildroot}%{_datadir}/%{name}/

# install files
for f in *.jar *.htm *.txt *.ini ; do
    install -Dm 0644 "$f" %{buildroot}%{_datadir}/%{name}
done

# install icon
install -Dm 0644 %{S:6} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:5} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root)
%{_bindir}/%{name}-*GUI
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Tue Sep 22 2015 nemysis@openSUSE.org
- Update to 1.1.1.6, please look
  /usr/share/domination/ChangeLog.txt
* Mon Mar 30 2015 dimstar@opensuse.org
- Add domination.png as icon (converted from resources/icon.ico):
  The .ico file at least is 32x32 pixels, whereas the provided pnt
  was only 16x16.
* Fri Nov 14 2014 nemysis@gmx.ch
- Change Source0 Web URL
* Thu Nov 13 2014 nemysis@gmx.ch
- Use Group Amusements/Games/Arcade/Strategy instead of
  Amusements/Games/Arcade/StrategyGame
- Use check for openSUSE %%if 0%%{?suse_version}
- Remove BuildRequires for desktop-file-utils
- Fix typo
* Sun Oct  5 2014 nemysis@gmx.ch
- Change %%fdupes
* Tue Sep 30 2014 nemysis@gmx.ch
- Remove not needed mkdir -p
- Use %%{name}.desktop instead of Desktop Entry in spec
* Wed Sep 17 2014 nemysis@gmx.ch
- Initial package creation
