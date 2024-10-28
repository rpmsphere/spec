%undefine _debugsource_packages

Name:           kom
Version:        0.9a.git04
Release:        60.1
License:        GPL
Source0:        %{name}-0.9a-git04.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ ruby qt4-devel aspell-devel mesa-libGL-devel
BuildRequires:  gstreamer-devel
Requires:       ruby qt4 aspell gstreamer mesa-libGL
Group:          Productivity/Graphics/Other
Summary:        KTooN Open Media Library
URL:            https://www.ktoon.net/
BuildRequires:  compat-ffmpeg-devel

%description
KOM is a framework designed to provide all the GUI components required
by KTooN and some other handy resources.

%package devel
Group: Productivity/Graphics/Other
Summary: Library for KOM project, headers
Requires: %{name}

%description devel
Library for KOM project, headers.

%prep
%setup -q -n %{name}-0.9a-git04

%build
qmake-qt4 -recursive
sed -i -e 's|^INCPATH.*=|INCPATH=-I/usr/include/compat-ffmpeg |' -e 's|^LIBS.*=|LIBS=-L%{_libdir}/compat-ffmpeg |' `find . -name Makefile`
make

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/ruby
cp -a qonf* $RPM_BUILD_ROOT/%{_datadir}/ruby
cd kom/kcore
install -d $RPM_BUILD_ROOT/%{_includedir}/kcore
install -p *.h $RPM_BUILD_ROOT/%{_includedir}/kcore
install -Dm755 libkcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkcore.so.1.0.0
ln -s libkcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkcore.so
ln -s libkcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkcore.so.1
ln -s libkcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkcore.so.1.0
cd ../ksound
install -d $RPM_BUILD_ROOT/%{_includedir}/ksound
install -p *.h $RPM_BUILD_ROOT/%{_includedir}/ksound
install -Dm755 libksound.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libksound.so.1.0.0
ln -s libksound.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libksound.so
ln -s libksound.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libksound.so.1
ln -s libksound.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libksound.so.1.0
cd ../kgui
install -d $RPM_BUILD_ROOT/%{_includedir}/kgui
install -p *.h $RPM_BUILD_ROOT/%{_includedir}/kgui
install -Dm755 libkgui.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkgui.so.1.0.0
ln -s libkgui.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkgui.so
ln -s libkgui.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkgui.so.1
ln -s libkgui.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libkgui.so.1.0
cd ../plugins/kgstengine
install -Dm755 libkgstengine.so $RPM_BUILD_ROOT/%{_libdir}/kom/plugins/libkgstengine.so

%files
%{_libdir}/lib*
%{_datadir}/ruby/*
%{_libdir}/kom

%files devel
%{_includedir}/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9a.git04
- Rebuilt for Fedora
* Sun Jun  3 2007 nemecp4@gmail.com
- call make install again (hack with calling configure twice)
- copy qconf manualy
* Fri Jun  1 2007 pnemec@suse.cz
- fixed some problems,
- not calling make install anymore, use manual installation
* Mon May 28 2007 nemecp4@gmail.com
- initial version
- need ugly hack to fix build on x86_64 platform
