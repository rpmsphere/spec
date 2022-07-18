Summary:	GUI for youtube-dl
Name:		youtube-dl-gui
Version:	1.8.3
Release:	1
License:	Public Domain
Group:		Video
URL:		https://github.com/oleksis/youtube-dl-gui
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	python2-setuptools
BuildRequires:	python2-wxpython
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:  python3
#BuildRequires:  python2-twodict
Requires:	ffmpeg
Requires:	python2-wxpython
Requires:	youtube-dl
BuildArch:	noarch

%description
Youtube-dlG is a multi-platform GUI for the popular command line video
download tool youtube-dl. The GUI lets you download multiple videos at
once, can automatically convert downloaded videos to audio, lets you
select the video quality and more.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=/usr --root=%{buildroot}

mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=YouTube-dl GUI
Comment=GUI for YouTube-dl
Exec=%{name}
Icon=%{name}_48x48.png
Terminal=false
Type=Application
Categories=Video;
EOF

#sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
#{_datadir}/youtube-dlg
%{_mandir}/man1/*
%{python3_sitelib}/*

%changelog
* Sun Jul 10 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.3
- Rebuilt for Fedora
* Mon Jun 01 2015 Stan8 <stasiek0000@poczta.onet.pl> 0.3.8-Stan8
- (e726d43) Updated youtube-dl-gui.spec
