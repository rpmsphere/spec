Name: tubeplayer
Summary: Youtube video player
Version: 2012.08.19
Release: 7.1
Group: Applications/Internet
License: GPL
URL: http://mspadaru.wordpress.com/2012/08/19/tubeplayer/
Source0: http://sourceforge.net/code-snapshots/svn/t/tu/tubeplayer/code/tubeplayer-code-2-trunk.zip
Source1: %{name}.png
BuildArch: noarch
Requires: python-pyside

%description
TubePlayer is an app that alows you to play youtube videos without opening a
browser. You just copy-paste the video’s URL and it gets added to the playlist.
You can also import whole playlists.

%prep
%setup -q -n tubeplayer-code-2-trunk

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp src/*.py %{buildroot}%{_datadir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python main.py
EOF

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Tube Player
Comment=Youtube video player
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Applications;Network;
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2012.08.19
- Rebuild for Fedora
