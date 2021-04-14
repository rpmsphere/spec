Name:           gnustep-gui
#Version:        0.24.1
Version:        0.25.1
Release:        4.1
Summary:        The GNUstep GUI library
License:        GPLv2+ and GPLv3+
Group:          Development/Libraries
URL:            http://www.gnustep.org
Source:         ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
BuildRequires:  gcc-objc
BuildRequires:  gmp-devel
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libffi-devel
BuildRequires:  avahi-devel
Buildrequires:  libicu-devel
BuildRequires:  libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  cups-devel
BuildRequires:  aspell-devel
BuildRequires:  giflib-devel
BuildRequires:  audiofile-devel
BuildRequires:  portaudio-devel >= 19
BuildRequires:	texinfo, texi2html, texinfo-tex
BuildRequires:  gnustep-make >= 2.6.4-9
BuildRequires:  gnustep-base-devel >= 1.24.0
BuildRequires:  gnustep-base >= 1.24.0
Requires:       gnustep-base >= 1.24.0
Requires:       %{name}-libs = %{version}-%{release}

%description 
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

%package libs
Summary:        Libraries for %{name}
Group:          Development/Libraries
License:        LGPLv2+ and LGPLv3+

%description libs
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

This package contains the libraries for %{name}

%package devel
Summary:        Header files for the gnustep-gui package
Group:          Development/Libraries
Requires:       gnustep-make >= 2.6.4-9
Requires:       gnustep-base-devel >= 1.22.0
Requires:       %{name}-libs = %{version}-%{release}

%description devel
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

This package contains the header files for gnustep-gui.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation
BuildArch:      noarch
License:        GFDL
Requires:       %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description doc
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

This package contains the documentation for %{name}

%prep
%setup -q

%build
%gnustep_configure
%gnustep_make -n
%gnustep_makedoc 

%install
%gnustep_install -n
%gnustep_installdoc

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post doc
/sbin/install-info %{_infodir}/AppKit %{_infodir}/dir || :

%preun doc
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/AppKit %{_infodir}/dir || :
fi

%files
%{_bindir}/gclose
%{_bindir}/gopen
%{_bindir}/gcloseall
%{_bindir}/make_services
%{_bindir}/set_show_service
%{gnustep_bundledir}/
%{gnustep_cpickdir}/
%{gnustep_imagedir}/
%{gnustep_kbdir}/
%{gnustep_psdir}/
%{gnustep_sounddir}/
%{gnustep_libraries}//gnustep-gui/
%{gnustep_srvdir}/
%{_mandir}/man1/*

%doc ANNOUNCE BUGS COPYING NEWS README

%files devel
%{_includedir}/AppKit/
%{_includedir}/GNUstepGUI/
%{_includedir}/Cocoa/
%{_includedir}/gnustep/gui/
%{_libdir}/libgnustep-gui.so
%{gnustep_additional}/gui.make

%files libs
%{_libdir}/libgnustep-gui.so.*
%doc COPYING.LIB

%files doc
%{_infodir}/AppKit.info.gz
%{_datadir}/GNUstep/Documentation/*
%doc Documentation/manual/LICENSE

%changelog
* Wed Jan 11 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.24.1
- Rebuilt for Fedora
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.24.0-4
- rebuild for ICU 56.1
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 0.24.0-2
- rebuild for ICU 54.1
* Sun Oct  5 2014 Jochen Schmitt <Jochen herr-schmitt de> - 0.24.0-1
- New upstream release
- Add missing BRs
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Wed Aug 14 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.23.1-6
- Remove obsoletes gnustep rpm macros.
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- Add gnustep-base as a BR to fix BZ #002416
* Fri Apr  5 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.23.1-4
- Rework for changed gnustep rpm macros
* Thu Apr  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.23.1-3
- Rebuilt for new gnustep-make release
* Mon Apr  1 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.23.1-2
- Usage of gnustep rpm macros
* Sat Mar 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.23.1-1
- New upstream release
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.22.0-4
- rebuild due to "jpeg8-ABI" feature drop
* Fri Nov 30 2012 Jochen Schmitt <Jochen herr-schmitt de> - 0.22.0-3
- Rebuilt for new gnustep-base release
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Wed Feb  8 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.22.0-1
- New upstream release
* Wed Jan  4 2012 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-5
- Fix depedencies issues on rawhide (libobjc.so.3)
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> 0.20.0-4
- Rebuild for new libpng
* Mon Oct 10 2011 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-3
- Rebuilt again
* Sun Oct  9 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.20.0-2
- Rebuilt for gnustep-base-1.23.0
* Wed Apr 27 2011 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-1
- New upstream release which is compatible to gcc-4.6
* Thu Feb 10 2011 Jochen Schmitt <Jochen herr-schmitt de> - 0.20.0-0.20110210
- First building unstable release agains gcc-4.6.0
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Jan 23 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-3
- Rebuild for new libobjc
* Tue Jul  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-2
- Use new gnustep parallel build feature
* Fri May 14 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-1
- New upstream release
* Tue Oct 13 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-5
- Fix missing BRs
* Tue Sep 29 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-4
- Fix typo
* Sun Sep 27 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-3
- Create separate libs subpackage
- Fix license tag
* Thu Sep 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-2
- Rework for new gnustep-make and gnustep-base releases
* Tue Feb 17 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-1
- New upstream release
* Thu Dec 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.14.0-2
- Add some missing BRs
* Wed Dec 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.14.0-1
- Initional Package
