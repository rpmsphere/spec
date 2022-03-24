%undefine _debugsource_packages

Name:           xosview2
Version:        2.3.1
Release:        1
Summary:        System resource monitor
License:        GPLv2, BSD
Source: xosview2-2.3.1.tar.gz
URL: https://sourceforge.net/projects/xosview/files/latest/download
BuildRequires: gawk libXext-devel gcc-c++ libXft-devel libXpm-devel libSM-devel

%description
xosview is a lightweight program that gathers information
from your operating system and displays it in graphical form.
It attempts to show you in a quick glance an overview of how
your system resources are being utilized.

%prep
%setup -q

%build
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/X11/app-defaults/*
%{_docdir}/xosview2/*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.1
- Rebuilt for Fedora
* Sat Jul 11 2015 Mike Romberg <mike-romerg@comcast.net> 2.8-1
- Initial version of the package
