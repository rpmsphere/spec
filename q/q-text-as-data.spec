Name:		q-text-as-data
Version:	2.0.0
Release:	1
Summary:	q - Text as Data
Group:		Applications/Text
License:	GPLv3
URL:		https://github.com/harelba/q
Source:		https://github.com/harelba/q/archive/%{version}.tar.gz#/q-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	rubygem-ronn

%description
q allows to perform SQL-like statements on tabular text data.

%prep
%setup -qn q-%{version}

%build
ronn doc/USAGE.markdown
sed -i 's|/usr/bin/env python$|/usr/bin/python3|' bin/q

%install
rm -vrf ${RPM_BUILD_ROOT}/
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}
install -Dm 0755 bin/q ${RPM_BUILD_ROOT}%{_datadir}/%{name}/
ln -s  %{_datadir}/%{name}/q ${RPM_BUILD_ROOT}%{_bindir}/%{name}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -m 0644 doc/USAGE ${RPM_BUILD_ROOT}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%doc README.markdown doc/AUTHORS doc/IMPLEMENTATION.markdown doc/LICENSE doc/RATIONALE.markdown doc/THANKS doc/USAGE.markdown 
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jul 01 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuild for Fedora
* Fri Dec 12 2014 Harel Ben-Attia <harelba@gmail.com> 1.5.0-1
- Moved stuff from create-rpm script into the rpm spec itself
* Sat Jun 14 2014 Harel Ben-Attia <harelba@gmail.com> 1.4.0-1
- Changed RPM package name to q-text-as-data
- Fixed RPM creation logic after folder restructuring
- Man page is now taken directly from USAGE.markdown
* Mon Mar 03 2014 Harel Ben-Attia <harelba@gmail.com> 1.3.0-1
- Version 1.3.0 packaging
* Thu Feb 20 2014 Harel Ben-Attia <harelba@gmail.com> 1.1.7-1
- Added man page
* Wed Feb 19 2014 Jens Neu <jens@zeeroos.de> 1.1.5-1
- initial release
