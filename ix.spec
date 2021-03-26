Name:           ix
Version:        0.4
Release:        4.1
Summary:        Client for the ix.io pastebin
Group:          Applications/Internet
License:        Unknown
URL:            http://ix.io
Source0:        http://ix.io/client
BuildArch:      noarch
Requires:       python2

%description
Client for the ix.io pastebin.

%prep
#nothing to do

%build
#nothing to do

%install
install -D -m 755 %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Sat Jun 09 2012 qmp <glang@lavabit.com> - 0.4-3
- Use SOURCE0 instead of _sourcedir
* Fri Jun 08 2012 qmp <glang@lavabit.com> - 0.4-2
- Rebuild for f17
* Sun Dec 26 2010 build@rnd - 0.4-1
- Initial packaging
