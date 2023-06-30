Name: iredmail
Summary: Free, Open Source Email Server Solution
Version: 0.9.3
Release: 4.1
Group: Applications/Internet
License: GPLv2
URL: https://www.iredmail.org/
Source0: https://bitbucket.org/zhb/iredmail/downloads/iRedMail-%{version}.tar.bz2
BuildArch: noarch

%description
iRedMail is a zero cost, fully fledged, full-featured mail server solution.
All used packages are free and open source, provided by the Linux/BSD
distribution venders you trust.

%prep
%setup -q -n iRedMail-%{version}

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}
cat > %{name} <<EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
exec bash iRedMail.sh
EOF
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%post
echo 'RedHat 7' >> /etc/redhat-release

%postun
sed -i '/RedHat 7/d' /etc/redhat-release

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Jan 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3
- Rebuilt for Fedora
