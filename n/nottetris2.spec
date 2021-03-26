Name:           nottetris2
Version:        1
Release:        9.1
Summary:        Classic Tetris mixed with physics
License:        Zlib
Group:          Amusements/Games/Action/Arcade
URL:            http://stabyourself.net/nottetris2/
Source:         http://stabyourself.net/dl.php?file=nottetris2/%{name}-source.zip
Requires:       love
BuildArch:      noarch

%description
Not Tetris 2 is the spiritual successor of the classic Tetris mixed with physics.
The result is a fun spinoff in which blocks are no longer bound to the usual grid.
Blocks can be rotated and placed at any angle, resulting in a complete mess if
not careful. And with the newest cutting edge technology, Not tetris 2 allows
line clears when the lines are sufficiently filled. The old mode is still
available for play and is now called Stack.

%prep
%setup -q -c
sed -i 's/\r$//' *.txt
mv 'Not Readme.txt' readme.txt
mv 'Not Tetris 2.love' %{name}.love
echo -e "#!/bin/sh\nlove %{_datadir}/%{name}/%{name}.love\n" > %{name}

%build

%install
install -D -m 0644 %{name}.love %{buildroot}%{_datadir}/%{name}/%{name}.love
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc readme.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.love

%changelog
* Thu May 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuild for Fedora
* Fri Mar 22 2013 joop.boonen@opensuse.org
- Corrected the License
* Sun Feb 17 2013 jengelh@inai.de
- nottetris2 requires love-0.7.2 and will not work with 0.8.0
* Wed Jun 22 2011 prusnak@opensuse.org
- created package
