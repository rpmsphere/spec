%global debug_package %{nil}

Summary: An OpenGL rollercoaster ride animation
Name: rollercoaster
Version: 1.1.0
Release: 21.1
License: GPL
Group: Amusements/Graphics
URL: http://plusplus.free.fr/rollercoaster/
Source:   http://plusplus.free.fr/rollercoaster/rollercoaster-%{version}-src.tar.gz
Source1:  rollercoaster-%{version}-ss.diff.gz
Source14: http://plusplus.free.fr/rollercoaster/DevilsTower.trk
Source15: http://plusplus.free.fr/rollercoaster/DizzyButterfly.trk
Source16: http://plusplus.free.fr/rollercoaster/speedy_loops.trk
Source17: http://plusplus.free.fr/rollercoaster/WildeMaus.trk
Source18: http://plusplus.free.fr/rollercoaster/WildeMaus2.trk
Source19: http://plusplus.free.fr/rollercoaster/Brainstorm.trk
Source20: http://plusplus.free.fr/rollercoaster/SunnyWE.trk
Source21: http://plusplus.free.fr/rollercoaster/Hypotron.trk
Source22: http://plusplus.free.fr/rollercoaster/KarmicRelief.trk
Source23: http://plusplus.free.fr/rollercoaster/millenium.trk
Patch1:	rollercoaster-Makefile.patch
Requires: xscreensaver
BuildRequires: mesa-libGL-devel, mesa-libGLU-devel, libXt-devel, libXmu-devel
BuildRequires: freeglut-devel 

%package xscreensaver
Summary: An OpenGL rollercoaster ride animation for xscreensaver
License: GPL
Group: Amusements/Graphics
Requires: rollercoaster

%description
rollercoaster renders a rollercoaster animation using OpenGL.

%description xscreensaver
rollercoaster is a module for xscreensaver that renders a rollercoaster 
animation using OpenGL.

%prep
%setup -q -n rollercoaster-%{version}-src
gunzip -c %{SOURCE1} | patch -f || true
%patch1 -p1 -b .make

%build
%{__make} -f Makefile.linux screensaver
cp bin/roller-ss bin/roller-ss.save
make -f Makefile.linux clean
%{__make} -f Makefile.linux

%install
%{__install} -D -m0755 bin/roller-ss.save %{buildroot}/usr/libexec/xscreensaver/roller-ss
%{__install} -D -m0755 bin/roller %{buildroot}/usr/bin/roller
mkdir -p %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 bin/*.tga bin/*.trk %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE14} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE15} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE16} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE17} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE18} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE19} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE20} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE21} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE22} %{buildroot}%{_datadir}/rollercoaster/
%{__install} -D -m0644 %{SOURCE23} %{buildroot}%{_datadir}/rollercoaster/

%clean
%{__rm} -rf %{buildroot}

%files
/usr/bin/roller
%{_datadir}/rollercoaster

%files xscreensaver
/usr/libexec/xscreensaver/roller-ss

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuild for Fedora
* Sat Jul  7 2012 josef radinger <cheese@nosuchhost.net>
- 1.1.0-3
- fiddle with build-order
- fix description
* Sat Jul  7 2012 josef radinger <cheese@nosuchhost.net>
- 1.1.0-2
- fix DATADIR
* Sat Jul  7 2012 josef radinger <cheese@nosuchhost.net>
- 1.1.0-1
- bump version
- update xscreensaver-patch
* Sat Jul  7 2012 josef radinger <cheese@nosuchhost.net>
- 1.0.0-3
- add tracks and fix paths
- fix version+release for subpackage
* Sat Jul  7 2012 josef radinger <cheese@nosuchhost.net>
- 1.0.0-2
- add BuildRequires 
- patch Makefile
- add additional tracks
- create subpackage for xscreensaver and add main-package rollercoaster
* Tue Sep  7 2004 Bert de Bruijn <bert@debruijn.be>
- Initial package for version 1.0.0
