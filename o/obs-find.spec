Name:               obs-find
Version:            1.0
Release:            4.1
Summary:            Find packages on the openSUSE Build Service
Source0:            obs-find.pl
Group:              Development/Tools/Other
License:            GNU General Public License version 2 or later (GPL v2 or later)
Requires:           osc
Requires:           perl
BuildArch:          noarch

%description
A frontend to "osc" to search for packages in openSUSE Build Service instances.

%prep
%setup -c -T

%build

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 "%{SOURCE0}" "$RPM_BUILD_ROOT%{_bindir}/obs-find"

%files
%{_bindir}/obs-find

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora

* Wed Jan  5 2011 pascal.bleser@opensuse.org
- initial version (1.0)
