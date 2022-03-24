Name:           rem2ics
Version:        0.93
Release:        1
Summary:        Converts the output of "remind -s" into RFC2445 iCalendar format
Group:          Applications/Productivity
License:        GPLv2+
URL:            http://mark.atwood.name/code/rem2ics/
Source0:        rem2ics
Source1:        rem2ics-Makefile
BuildArch:      noarch
BuildRequires:  perl

%description
rem2ics converts the output of "remind -s" into RFC2445 iCalendar format.
You may want to install remind if you install this package.

%prep
%setup -T -c
cp %SOURCE0 .
cp %SOURCE1 Makefile

%build
make  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/rem2ics
%{_mandir}/man1/rem2ics.1*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93
- Rebuilt for Fedora
* Tue Mar 25 2008 Till Maas <opensource till name> - 0.92-1
- initial spec for Fedora
