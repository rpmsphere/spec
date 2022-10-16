Summary: A stack oriented APL-like language
Name: lang5
Version: 1.0
Release: 1
License: freeware
Group: Development/Languages
Source0: https://github.com/bernd-ulmann/lang5/raw/master/%{name}.zip
URL: https://lang5.sourceforge.net/
BuildArch: noarch

%description
A Perl based interpreter for a language which is a blend of Forth and APL.
The power of lang5 stems from its arrays operations in conjunction with
the underlying Forth programming paradigm of bottom up programming.

%prep
%setup -q -n %{name}

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a %{name} %{name}.vim examples lib perl_modules doc %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
%{_datadir}/%{name}/%{name} "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files 
%doc *.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
