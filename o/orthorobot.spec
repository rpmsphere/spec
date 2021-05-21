Name:           orthorobot
Version:        0
Release:        8.1
Summary:        A perspective based puzzle game
License:        Zlib
Group:          Amusements/Games/Action/Arcade
URL:            http://stabyourself.net/orthorobot/
Source:         http://stabyourself.net/dl.php?file=orthorobot/%{name}-source.zip
Requires:       love
BuildArch:      noarch

%description
Literally bridging the gap between 2D and 3D games, Ortho Robot is a perspective
based puzzle game, where you flatten the view to move across gaps. Your
objective is to reach the ending green block (either by standing directly on it
or standing on it in relative space). For some extra challenge, try to collect
all coins and perfect your time, steps and number of warps.

%prep
%setup -q -c
mv "Ortho Robot.love" %{name}.love
echo -e "#!/bin/sh\nlove %{_datadir}/%{name}/%{name}.love\n" > %{name}

%build

%install
install -D -m 0644 %{name}.love %{buildroot}%{_datadir}/%{name}/%{name}.love
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Thu May 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0
- Rebuilt for Fedora
* Sun Dec 15 2013 prusnak@opensuse.org
- change dependency to love-0_8_0
* Sun Aug 25 2013 prusnak@opensuse.org
- created package
