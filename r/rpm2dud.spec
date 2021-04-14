Name:           rpm2dud
License:        GPL v3 or later
Group:          Hardware/Other
Summary:        Create driver update from rpms
Version:        0.9
Release:        5.1
Source:         rpm2dud-0.9.tar.bz2
BuildArch:      noarch

%description
Create a driver update from rpms.

Authors:
--------
    Steffen Winterfeldt

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 rpm2dud $RPM_BUILD_ROOT/usr/bin

%clean 
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/rpm2dud
%doc README COPYING

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuilt for Fedora
* Fri Sep  2 2011 snwint@suse.de
- initial version
