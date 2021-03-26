Summary:	OxStore release files
Name:		oxstore-release
Version:	2
Release:	3
License:	MIT
Group:		System Environment/Base
URL:		http://oxstore.linux.net.tw/
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	ossii-release

%description
OxStore release yum configs to define the release.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 644 oxstore.repo $RPM_BUILD_ROOT/etc/yum.repos.d/oxstore.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Jul 27 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial package
