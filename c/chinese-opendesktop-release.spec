Name: chinese-opendesktop-release
Version: 28
Release: 1
Summary: Repository from Chinese Opendesktop
License: Public Domain
Source0: chinese-opendesktop.repo
BuildArch: noarch
Requires: rpmsphere-release

%description
YUM config to define the chinese-opendesktop repository.

%prep

%build

%install
install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/chinese-opendesktop.repo

%files
%{_sysconfdir}/yum.repos.d/chinese-opendesktop.repo

%changelog
* Mon Nov 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 28
- Update package
