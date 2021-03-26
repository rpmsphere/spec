%global debug_package %{nil}

Name: gogs
Summary: Go Git Service
Version: 0.11.91
Release: 1.bin
Group: Internet
License: opensource
URL: http://gogs.io
Source0: https://dl.gogs.io/0.11.91/gogs_%{version}_linux_amd64.tar.gz
Requires: openssl
Requires: readline
Requires: libxml2
Requires: libxslt
Requires: libevent
Requires: sqlite
Requires: pam
Requires: git
#Requires: postgresql-libs
#Requires: mysql-libs

%description
Gogs is a painless self-hosted Git Service written in Go.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a * %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_libexecdir}/%{name}
exec ./gogs "$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.91
- Initial binary package
