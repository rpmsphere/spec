%undefine _debugsource_packages
%define oname	ExMplayer

Name:		exmplayer
Version:	5.0.1
Release:	11.1
Summary:	MPlayer GUI with thumbnail seeking and 3D Video support
License:	GPLv2+
Group:		Video/Players
URL:		https://exmplayer.sourceforge.net/
Source0:	https://github.com/rupeshs/ExMplayer/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		exmplayer-3.8.0-segfault.patch
BuildRequires:	cmake
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	qt4-devel
#BuildRequires:	ffmpeg-devel
Requires:	ffmpeg
Requires:	mplayer
Requires:	youtube-dl

%description
ExMplayer (Extended MPlayer) is a GUI front-end for MPlayer with flow view
and tool like media cutter. It can play audio, video, dvd files(.vob), vcd
files(.mpg,.dat) etc and supports network streaming. It supports subtitles,
subtitle decoding is done by using ass library. It can play any media formats
without any external codecs.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

# wrong-file-end-of-line-encoding
sed -i 's/\r$//' Release_notes.txt README.md
sed -i '2298d' src/playerwindow.cpp
sed -i -e 's|(picflow>.*0|(picflow!=NULL|' -e 's|fullScreenControls<=0|fullScreenControls==NULL|' -e 's|mp>0|mp!=NULL|' src/playerwindow.cpp
sed -i -e 's|readInfo>0|readInfo!=NULL|' -e 's|openMediaInfo>0|openMediaInfo!=NULL|' -e 's|readFile>0|readFile!=NULL|' src/mplayerfe.cpp
sed -i 's|myProcess>0|myProcess!=0|' src/pictureflow.cpp

%build
qmake-qt4 src/%{oname}.pro
make

%install
%makeinstall

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 linux_build/fmts %{buildroot}%{_sysconfdir}/%{name}/fmts
install -m 0644 linux_build/sc_default.xml %{buildroot}%{_sysconfdir}/%{name}/sc_default.xml

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m 0644 %{name}_enqueue.desktop %{buildroot}%{_datadir}/applications/%{name}_enqueue.desktop

mkdir -p %{buildroot}%{_datadir}/%{name}
ln -s %{_bindir}/ffmpeg %{buildroot}%{_datadir}/%{name}/ffmpeg

# install menu icons
for N in 16 32 48 64 128 256;
do
  convert debian/%{name}.png -resize ${N}x${N} $N.png;
  install -D -m 0644 $N.png %{buildroot}%{_datadir}/icons/hicolor/${N}x${N}/apps/%{name}.png
done

%files
%doc README.md Release_notes.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_enqueue.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%config(noreplace) %{_sysconfdir}/%{name}/fmts
%config(noreplace) %{_sysconfdir}/%{name}/sc_default.xml

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.1
- Rebuilt for Fedora
* Tue Jul 28 2015 daviddavid <daviddavid> 5.0.1-2.mga6
+ Revision: 858766
- add youtube-dl as a Recommends
  * as exmplayer integrates a Video Downloader feature using youtube-dl
* Tue Jul 28 2015 daviddavid <daviddavid> 5.0.1-1.mga6
+ Revision: 858726
- imported package exmplayer
