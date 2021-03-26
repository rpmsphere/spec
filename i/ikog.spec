Summary: 	It Keeps on growing
Name: 		ikog
Version: 	1.90
Release: 	3.1
License: 	GPL
Group: 		Applications/Productivity
Source: 	%{name}-%{version}.zip
URL:		https://sites.google.com/site/henspace/ikog
BuildArch:	noarch

%description 
This is a very simple utility designed to make the management of your
to-do lists quick and easy. The emphasis is on speed and portability.
The program is a text-only utility with no graphical user-interface
but it does include some features specifically designed to help with
techniques such as Getting Things Done (GTD).

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp * $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
./%{name} \$HOME/.%{name}
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Sep 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.90
- Rebuild for Fedora
