Name: biogenesis
Summary: Modern microbiology laboratory
Version: 0.8
Release: 9.1
Group: Science/Engineering
License: GPL
URL: http://biogenesis.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/biogenesis/biogenesis_src_0_8.zip
BuildArch: noarch
BuildRequires: java-devel-openjdk lua
Requires: jre

%description
Biogenesis simulates in a visual fashion the processes involved in the
evolution of unicellular organisms at nature. It tries to be a didactic
approximation to the ideas of mutation or evolution and can be enjoyed
also as an entertainment. It's intended to serve as a support to show
students some basic biological facts.

%prep
%setup -q -n %{name}_src

%build
javac -encoding utf-8 *.java
rm *.java

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
java %{name}
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora
