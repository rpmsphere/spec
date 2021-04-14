Summary:	RPM Sphere release file
Name:		rpmsphere-release
Version:	32
Release:	1
License:	Public Domain
Group:		System Environment/Base
URL:		https://github.com/rpmsphere
Source0:        rpmsphere.repo
BuildArch:	noarch
Recommends:	rpmfusion-free-release
Recommends:     rpmfusion-nonfree-release

%description
RPM Sphere release yum configs to define the repository.
Collection of extra packages for Fedora Linux.
Feel free to promote them in any form.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/rpmsphere.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/yum.repos.d/*

%changelog
* Thu Apr 30 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 32
- Rebuilt for Fedora
