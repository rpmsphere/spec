%undefine _debugsource_packages

Name:         mfm
License:      GPL
Group:        Productivity/File utilities
Version:      1.3
Release:      820.1
Summary:      Motif file manager
Source:       mfm1.3.tar.Z
Patch0:        mfm-1.3.dif
BuildRequires: imake
BuildRequires: libXpm-devel
BuildRequires: motif-devel

%description
A file manager for X11 using Motif.

Authors:
--------
    Andrew T. Renalds <renalds@abn.com>

%prep
%setup -q -n mfm1.3
%patch 0
touch mfm.man

%build
xmkmf -a
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 Mfm.color.sample.ad %{buildroot}%{_datadir}/X11/app-defaults/Mfm
mkdir -p %{buildroot}%{_includedir}/X11/bitmaps/mfm
install bitmaps/* %{buildroot}%{_includedir}/X11/bitmaps/mfm

%files
%doc doc/*
%{_bindir}/%{name}
%{_includedir}/X11/bitmaps/%{name}
%{_datadir}/X11/app-defaults/*

%changelog
* Fri Jun 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Tue Sep 17 2002 - ro@suse.de
- removed bogus self-provides
* Tue Jun 12 2001 - fehr@suse.de
- prevent abort with new imake
* Wed May 09 2001 - mfabian@suse.de
- bzip2 sources
* Mon Nov 20 2000 - fehr@suse.de
- now build with openmotif
* Fri Nov 17 2000 - fehr@suse.de
- set group tag
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Jul 12 1999 - uli@suse.de
- now builds with lesstif
* Wed Dec 10 1997 - ro@suse.de
- build static and dynamic version
* Mon Oct 13 1997 - fehr@suse.de
- prepare for automatic build of package
