Name:         sscep
Version:      0.9.0
Release:      1
Summary:      Simple SCEP client
License:      BSD
Group:        Productivity/Security
Source:       %{name}-%{version}.tar.gz
URL:          https://github.com/certnanny/sscep
Requires:     openssl >= 1:0.9.7

%description
Simple SCEP (Simple Certificate Enrollment Protocol) client.

%prep
%setup -q

%build
%cmake .
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install

%files
%doc COPYING README.md AUTHORS ChangeLog TODO
%{_bindir}/sscep

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
