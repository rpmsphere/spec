Name: pygmynote
Summary: Python-based Personal Data Manager
Version: 0.11.05
Release: 2.1
Group: Applications/Databases
License: GPL
URL: https://github.com/dmpop/pygmynote
Source0: %{name}-master.zip
BuildArch: noarch
Requires: nano

%description
Pygmynote is a Python-based command-line tool for storing and managing hetero-
geneous bits of data, including notes, tasks, links, and file attachments.

%prep
%setup -q -n %{name}-master

%build

%install
install -Dm755 %{name}.py %{buildroot}%{_bindir}/%{name}
#install -Dm644 es/LC_MESSAGES/%{name}.mo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc README.md GPL.txt
%{_bindir}/%{name}
#%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Wed Jul 05 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.05
- Rebuild for Fedora
