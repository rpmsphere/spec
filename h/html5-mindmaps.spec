Summary: HTML5 Mindmaps fork
Name: html5-mindmapr
Version: 1.2
Release: 1
License: AGPL V3, see LICENSE for more information
Group: Applications/Productivity
Source0: manishchiniwalar-mindmaps-d511416.tar.gz
URL: https://github.com/manishchiniwalar/mindmaps
Requires: oxzilla
BuildArch: noarch

%description
Simplify your thoughts by using mindmaps to note down ideas,to-dos and
decisions. Works Offline too!

%prep
%setup -q -n manishchiniwalar-mindmaps-d511416

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 1024x600 index.html
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Dec 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Initial build
