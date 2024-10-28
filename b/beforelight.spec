Name:          beforelight
Version:       1.0.4
Release:       2.1
Summary:       A screen saver for X servers supporting the MIT-SCREEN-SAVER extension
Group:         System/X11
URL:           https://x.org
Source:        https://ftp.x.org/pub/individual/app/beforelight-%{version}.tar.bz2
License:       MIT
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXaw-devel
BuildRequires: libXmu-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXt-devel

%description
The beforelight program is a sample implementation of a screen saver for
X servers supporting the MIT-SCREEN-SAVER extension.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/beforelight
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.1.gz
%doc COPYING ChangeLog

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora

* Mon Nov 01 2010 Automatic Build System <autodist@mambasoft.it> 1.0.4-1mamba
- automatic update by autodist

* Wed Aug 19 2009 Ercole 'ercolinux' Carpanetto <ercole69@gmail.com> 1.0.3-1mamba
- package created by autospec
