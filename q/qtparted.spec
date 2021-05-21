%undefine _debugsource_packages

Name:		qtparted
Version:	0.6.0
Summary:	Graphical Partitioning Tool
URL:		http://qtparted.sf.net/
Release:	1
Source:		http://freefr.dl.sourceforge.net/project/qtparted/qtparted-%version/qtparted-%version.tar.xz
Source10:	qtparted.pamd
Source11:	qtparted.pam
License:	GPL
Group:		Applications/System
BuildRequires:  qt4-devel
BuildRequires:  parted-devel

%description
QtParted is a graphical partition editor, similar to PartitionMagic(tm).

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DQT_QMAKE_EXECUTABLE=qmake-qt4 .
%cmake_build

%install
%cmake_install
# pam/kapabilities support
mkdir -p %{buildroot}%{_sbindir}
mv %buildroot%_bindir/* %buildroot%_sbindir
mkdir -p %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/qtparted
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/qtparted
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
install -m 644 -D %{SOURCE11} %{buildroot}%{_sysconfdir}/security/console.apps/qtparted

%files
%{_sbindir}/qtparted*
%{_bindir}/*
%{_datadir}/applications/*
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_datadir}/%name
%{_datadir}/pixmaps/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.0
- Rebuilt for Fedora
* Thu Feb 17 2011 Bernhard Rosenkraenzer <bero@arklinux.org> 0.5.0-1ark
- 0.5.0 final
* Thu Feb  3 2011 Bernhard Rosenkraenzer <bero@arklinux.org> 0.5.0-0.263.1ark
- 0.5.0svn - Qt4 at last
* Wed Jan 19 2011 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.6-7ark
- Rebuild with libpng 1.5
* Sat Jun 19 2010 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.6-6ark
- Adapt to current OS
* Tue Aug 14 2007 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.6-5ark
- Rebuild for parted 1.8.8
* Sat May 12 2007 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.6-4ark
- Rebuild -- parted 1.8.7 has a new soname
* Thu May  3 2007 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.6-3ark
- Build for parted 1.8.x
- x86_64 build fix
* Sun May 28 2006 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.6-2ark
- Parted 1.7.1
* Tue Apr  4 2006 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-4ark
- Rebuild w/ new parted, new Qt
* Wed Nov  2 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-3ark
- Rebuild w/ new parted
* Tue Sep 27 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-2ark
- Rebuild for Qt 3.3.5
* Fri Aug 12 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-1ark
- 0.4.5
* Sun Jul  3 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-8ark
- Allow building without X for use in the installer
* Wed Mar  2 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-7ark
- Recompile for testing with parted 0.6.21
* Sun Nov 28 2004 David Tio <deux@arklinux.org> 0.4.4-6ark
- Recompile after reverting back to parted 0.6.12
* Wed Sep 08 2004 David Tio <deux@arklinux.org> 0.4.4-5ark
- Recompile using parted 0.6.14
- Recompile using ntfsprogs 1.9.4
* Mon Aug 30 2004 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-4ark
- Recompile after reverting to parted 0.6.11
* Tue Aug 17 2004 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-3ark
- Rebuild with parted 0.6.12
* Mon Jun  7 2004 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-2ark
- Make it compile with current toolchain
* Mon Apr 26 2004 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-1ark
- 0.4.4
* Mon Mar 22 2004 Zackary Deems <zdeems@arklinux.org> 0.4.3-1ark
- New version - enabled ntfs support
- Better ntfs resizing support
- Fix for gcc 3.3 compiling
- Rebuilt using new ntfsprogs
* Sat Jun 21 2003 David Sainty <saint@arklinux.org> 0.3.2-1ark
- 0.3.2
* Fri May 30 2003 Bernhard Rosenkraenzer <bero@arklinux.org> 0.3.1-1ark
- initial RPM
