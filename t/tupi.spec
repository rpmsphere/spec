%global debug_package %{nil}

Summary:	2D vector-based animation environment
Name:		tupi
Version:	0.2.9
Release:	22.1
License:	GPLv3
URL:		http://www.maefloresta.com/
Group:		Graphics/Editors and Converters
Source0:	https://dl.sourceforge.net/project/tupi2d/Source%20Code/%{name}-%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	rubypick, ruby
BuildRequires:	aspell-devel
BuildRequires:	quazip-devel
BuildRequires:	rubygems-devel
BuildRequires:	libtheora-devel
BuildRequires:	libogg-devel

%description
A design and authoring tool for digital artists interested in 2D Animation.

%prep
%setup -q
sed -i 's|/usr/include/libavformat/|/usr/include/ffmpeg/ /usr/include/libavformat/|' tupiglobal.pri
sed -i 's|CODEC_FLAG_GLOBAL_HEADER|AV_CODEC_FLAG_GLOBAL_HEADER|' src/plugins/export/libavplugin/tlibavmoviegenerator.cpp

%build
qmake-qt5 PREFIX=/usr
make

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_mandir}
make -i -k install INSTALL_ROOT=%{buildroot}/usr DESTDIR=%{buildroot}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
mv %{buildroot}/usr/applications %{buildroot}/usr/share/applications
mv %{buildroot}/usr/pixmaps %{buildroot}/usr/share/pixmaps
mv %{buildroot}/usr/data %{buildroot}/usr/share/%{name}
mv %{buildroot}/usr/plugins %{buildroot}/usr/share/%{name}
mv %{buildroot}/usr/themes %{buildroot}/usr/share/%{name}
mv %{buildroot}/usr/man1 %{buildroot}/usr/share/man/man1

%files
%{_datadir}/doc/%{name}
%{_bindir}/*
%{_libdir}/lib%{name}*
%{_datadir}/applications/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Jul 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.9
- Rebuild for Fedora
* Sat Oct 19 2013 umeabot <umeabot> 0.2-0.09122012.4.mga4
+ Revision: 534845
- Mageia 4 Mass Rebuild
* Sun Sep 15 2013 juancho <juancho> 0.2-0.09122012.3.mga4
+ Revision: 479135
- Fix xml launcher file (BUG #10640)
* Thu Jul 11 2013 fwang <fwang> 0.2-0.09122012.2.mga4
+ Revision: 452802
- fix build with ffmpeg 2.0
* Mon Jan 14 2013 umeabot <umeabot> 0.2-0.09122012.2.mga3
+ Revision: 384842
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
  + boklm <boklm>
    - Update group: Graphics/Editors -> Graphics/Editors and Converters
* Tue Jan 01 2013 juancho <juancho> 0.2-0.09122012.1.mga3
+ Revision: 337076
- Added patch to fix build against ffmpeg 1.0.1
- Fixed mkrel
- imported package tupi
