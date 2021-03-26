%global debug_package %{nil}

Summary: Real-time audio synthesis and graphics/multimedia language
Name: chuck
Version: 1.4.0.0
Release: 8.1
License: GPL
Group: Applications/Multimedia
URL: http://chuck.cs.princeton.edu/
Source0: http://chuck.cs.princeton.edu/release/files/chuck-%{version}.tgz
# emacs mode from: http://wiki.cs.princeton.edu/index.php/Recent_chuck-mode.el
Source1: chuck-mode.el
BuildRequires: bison
BuildRequires: flex
BuildRequires: libsndfile-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: alsa-lib-devel

%description
ChucK is a general-purpose programming language, intended for
real-time audio synthesis and graphics/multimedia programming.  It
introduces a truly concurrent programming model that embeds timing
directly in the program flow.  Other potentially useful features include
the ability to write/change programs on-the-fly.

%prep
%setup -q

%build
cd src
make linux-pulse

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m755 src/chuck %{buildroot}%{_bindir}/chuck

# install emacs mode
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
cp -a %{SOURCE1} %{buildroot}%{_datadir}/emacs/site-lisp/chuck.el
mkdir -p %{buildroot}%{_libdir}/xemacs/site-packages/lisp/chuck/
cp -a %{SOURCE1} %{buildroot}%{_libdir}/xemacs/site-packages/lisp/chuck/chuck.el

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING DEVELOPER PROGRAMMER QUICKSTART README 
%doc THANKS TODO VERSIONS examples
%{_bindir}/*
%{_datadir}/emacs/site-lisp/*
%{_libdir}/xemacs/site-packages/lisp/chuck/*

%changelog
* Tue Sep 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0.0
- Rebuild for Fedora
* Wed Oct 12 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.6.0-1.220a
- update to experimental 1.3.6.0 (released for the 220a class)
* Tue Jan 14 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.3.0-1
- update to 1.3.3, add pulse build
* Sun Sep 29 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.2.0-1
- final 1.3.2.0 release
* Sat Sep 14 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add optflags for proper build on arm
* Thu Aug 29 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.2.0-0.1.beta4
- update to latest beta-4 test release
- add patch for util_thread.h
* Tue Oct  2 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.3-1
- updated to 1.3.1.3
* Sun Sep 16 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.2-1
- updated to 1.3.1.2
* Thu Sep 13 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.1-1
- updated to 1.3.1.1
* Fri Sep  7 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.0-1
- updated to 1.3.1.0, now 64 bit native
* Wed Aug 29 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.0.2-1
- updated to 1.3.0.2
* Sat Aug 25 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.0.0-1
- updated to 1.3.0.0
* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.3-1
- added -lpthread patch to build on fc13/gcc444
* Mon Oct 12 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.3-1
- updated to 1.2.1.3
* Thu Sep  3 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.2-2
- change build flags on fc11, otherwise segfaults on startup
* Thu Jun 11 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.2-1
- add gcc44 patch for building on fc11
* Fri Jul 18 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.2-1
- updated to 1.2.1.2 (keep building it with -DAJAY for experimental
  features)
* Wed Jul  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- build fixes for gcc4.3 on fc9
* Mon Oct  8 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.1c-1
- unofficial update/fix release
* Thu Oct  4 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.1-2
- small bug fix release (no change in main version number)
* Wed Oct  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.1-1
- updated to 1.2.1.1, updated emacs mode to latest version
* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.7-2
- build for fc6
* Fri Sep 22 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.7-1
- updated to 1.2.0.7, redid makefile patch for defining -DAJAY
  (to enable the PRC and Skot objects)
* Tue Jul 25 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.6-3
- keep the old chuck.el file name (not chuck-mode.el)
* Tue Jul 25 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.6-2
- updated to 1.2.0.6, updated emacs mode file
* Wed Jul 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.5-2
- build with additional experimental objects (see patch0), thanks to
  Ge Wang for the tip
- add an alsa only chuck in /usr/bin/chuck-alsa
- install emacs mode for chuck files
* Mon Jul 10 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.5-1
- initial build.
