%undefine _debugsource_packages
%undefine _auto_set_build_flags

Summary:	Command line program for save JPEG image of VNC server's screen
Name:		vncsnapshot
Version:	1.2a
Release:	3.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	https://dl.sourceforge.net/vncsnapshot/%{name}-%{version}-src.tar.bz2
URL:		https://vncsnapshot.sourceforge.net/
BuildRequires:	libjpeg-devel gcc-c++
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel

%description
VNC Snapshot is a command-line program for VNC. It will save a JPEG
image of the VNC server's screen.

%prep
%setup -q

%build
%__make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.man1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGE* BUGS README RELEASE-NOTES.txt web*html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2a
- Rebuilt for Fedora
* Thu Aug 07 2008 cyberorg@opensuse.org
- Initial openSUSE spec
