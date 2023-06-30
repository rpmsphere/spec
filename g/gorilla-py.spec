Name: gorilla-py
Summary: A Remake of Gorilla.bas
Version: 20100625
Release: 8.1
Group: Amusements/Games
License: Creative Commons
URL: https://inventwithpython.com/blog/2010/06/25/gorilla-py-a-remake-of-gorilla-bas/
Source0: https://inventwithpython.com/gorilla.py
Source1: %{name}.desktop
Source2: %{name}.png
BuildArch: noarch
BuildRequires: dos2unix
Requires: pygame

%description
An entire generation of people remember the Gorilla.BAS game that came with
Qbasic, where gorillas on top of buildings threw exploding bananas at each
other. This is a Python remake of that game using the Pygame game engine,
and is fairly heavily commented so you can explore the source.

%prep

%build

%install
install -Dm755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
dos2unix $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i '1i #!/usr/bin/python' $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Nov 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20100625
- Rebuilt for Fedora
