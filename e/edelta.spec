Name:    edelta
Version: 0.9e
Release: 4.1
License: GPL
Group: Productivity/Archiving/Backup 
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: zlib-devel
URL: http://www.diku.dk/~jacobg/edelta/
Source: http://www.diku.dk/~jacobg/edelta/edelta-0.9e.tar.gz
Summary: A XDelta-style binary differ

%description
EDelta is a fast XDelta-style binary differ, but optimized for executables
which have a very systematic way of changing between versions. It has not been
thoroughly evaluated so far, but on one example (two versions of Vim) it
produces a 30kB delta where XDelta needs 250kB. My personal use for edelta is
to quickly deploy Linux kernels from my development-laptop to my test-machines,
especially when working over my slow ADSL line at home. I frequently see factor
of 100 speedups compared to shipping the whole file.

Authors:
--------
     Jacob Gorm Hansen

%prep
%setup -q

%build
gcc %{optflags} -Wall -finline-functions -lz edelta.c sha1.c -o %{name}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc Contributors COPYING scripts

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9e
- Rebuilt for Fedora
* Tue Apr  3 2007 mrueckert@suse.de
- added zlib-devel to the buildrequires
* Fri Jan  5 2007 mrueckert@suse.de
- initial package of version 0.9e
