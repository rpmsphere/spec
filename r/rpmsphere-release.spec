Summary:        RPM Sphere release file
Name:           rpmsphere-release
Version:        40
Release:        1
License:        BSD
Group:          System Environment/Base
URL:            https://github.com/rpmsphere
Source0:        https://rpmsphere.github.io/rpmsphere.repo
BuildArch:      noarch
Recommends:     rpmfusion-free-release
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

%files
%{_sysconfdir}/yum.repos.d/*

%changelog
* Fri May 10 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 40
- Rebuilt for Fedora
