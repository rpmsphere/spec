Summary: 	Karaoke Lyrics Editor
Name: 		karlyriceditor
Version:	1.3
Release: 	1
License: 	GPLv3+
Group: 		Applications/Multimedia
URL: 		http://www.karlyriceditor.com
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-1.3-av.patch
BuildRequires:	qt4-devel, ffmpeg-devel

%description
Karaoke Lyrics Editor is a program which lets you edit and synchronize
lyrics with karaoke songs in varions formats. Unlike just regular lyrics
available everywhere, lyrics suitable for karaoke players need to have
timing marks which tell the player when to show a specific line, and
when and how highlight the words.
 
Author:
-------
George Yunaev

%prep
%setup -q
%patch0 -p1
sed -i 's|PIX_FMT_RGB24|AV_PIX_FMT_RGB24|' src/ffmpegvideodecoder.cpp

%build
qmake-qt4 PREFIX=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 packages/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 packages/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuild for Fedora
* Tue May 29 2012 johnwu <johnwu@ossii.com.tw>
- first 
