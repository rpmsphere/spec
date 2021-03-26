%global debug_package %{nil}

Name: hcxkeys
Summary: Small set of tools to generate plainmasterkeys
Version: 4.0.1
Release: 1
Group: Network
License: MIT
URL: https://github.com/ZerBea/hcxkeys
Source0: https://github.com/ZerBea/hcxkeys/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: opencl-headers

%description
Small set of tools to generate plainmasterkeys (rainbowtables) and hashes for
the use with latest hashcat and latest John the Ripper.

%prep
%setup -q

%build
make

%install
make install INSTALLDIR=%{buildroot}/usr/bin

%files
%doc README.md license.txt
%{_bindir}/*

%changelog
* Thu Dec 12 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.1
- Rebuild for Fedora

