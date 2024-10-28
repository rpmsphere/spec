Name: swiss
Version: 20160320
Release: 3.1
Summary: Swiss-system tournament manager in python3
License: opensource
Group: Games
Source0: Swiss-master.zip
URL: https://github.com/Hagge5/Swiss
Requires: python3
BuildArch: noarch

%description
Lines starting with # are comments. A command is written in the form of:
[command name] [arg0] [arg1] [arg2] ...
Each command ends with newline. To run with a file as input, simply pipe it.

%prep
%setup -q -n Swiss-master
sed -i '1i #!/usr/bin/python3' %{name}.py

%build

%install
rm -rf %{buildroot}
install -D -m 755 %{name}.py %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed May 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160320
- Rebuilt for Fedora
