Name: liblogging
Version: 0.7.1
Release: 4.1
Group: Development/Libraries/C and C++
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: dos2unix
URL: http://www.liblogging.org/
Source: liblogging-%{version}.tar.bz2
Summary: An easy to use, portable, open source library for system logging

%description
The original idea was to provide a very slim BEEP look-alike to implement with
a few hundered lines of code. Well, during development new ideas popped up and
the design goal now has evolved to provide a library useful for all kinds of
system logging.

Liblogging is unique in the way that it was specifically designed for system
logging and ease of use. There are many BEEP libraries out there and most of
them support the syslog reliable RAW profile. However, these libraries have a
very complex API, which is overdone just for logging. Software implementors
stay away from those libraries. We hope that liblogging will make reliable
syslog available to everyone. There is a very short, easy to use and learn API.

Authors:
--------
    Rainer Gerhards <rgerhards@adiscon.com>
    Devin Kowatch <devink@sdsc.edu> - *nix port

%package devel
Group: Development/Libraries/C and C++
Requires: liblogging = %{version}
Summary: Development files for liblogging

%description devel
The original idea was to provide a very slim BEEP look-alike to implement with
a few hundered lines of code. Well, during development new ideas popped up and
the design goal now has evolved to provide a library useful for all kinds of
system logging.

Liblogging is unique in the way that it was specifically designed for system
logging and ease of use. There are many BEEP libraries out there and most of
them support the syslog reliable RAW profile. However, these libraries have a
very complex API, which is overdone just for logging. Software implementors
stay away from those libraries. We hope that liblogging will make reliable
syslog available to everyone. There is a very short, easy to use and learn API.

This package holds the development files for liblogging

Authors:
--------
    Rainer Gerhards <rgerhards@adiscon.com>
    Devin Kowatch <devink@sdsc.edu> - *nix port

%prep
%setup -q
dos2unix AUTHORS ChangeLog COPYING

%build
%configure --disable-static
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall
%{__rm} -v $RPM_BUILD_ROOT%{_libdir}/liblogging.la

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/liblogging.so.0
%{_libdir}/liblogging.so.0.0.0

%files devel
%defattr(-,root,root,-)
%doc doc/html/*.html
%doc AUTHORS ChangeLog COPYING
%{_libdir}/liblogging.so
%{_libdir}/pkgconfig/liblogging.pc
%{_includedir}/liblogging

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.1
- Rebuilt for Fedora
* Tue May  6 2008 mrueckert@suse.de
- package the docs
* Tue May  6 2008 mrueckert@suse.de
- initial package
