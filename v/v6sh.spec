%undefine _debugsource_packages

Name: v6sh
Summary: A re-implementation of UNIX v6 sh
Version: 2006.07.13
Release: 5.1
Group: System Environment/Shells
License: PD
URL: http://blog.chinaunix.net/uid-20106293-id-142129.html
Source0: http://www.cublog.cn/u/13392/upfile/060714113802.tar

%description
A re-implementation of UNIX v6 sh.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags}

%install
install -Dm755 shell %{buildroot}%{_bindir}/v6sh
install -Dm755 if %{buildroot}%{_bindir}/v6if
install -Dm755 goto %{buildroot}%{_bindir}/v6goto

%files
%{_bindir}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2006.07.13
- Rebuilt for Fedora
