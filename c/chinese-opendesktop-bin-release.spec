Name: chinese-opendesktop-bin-release
Version: 25
Release: 1
Summary: Repository from Chinese Opendesktop Binary
License: Public Domain
Source0: chinese-opendesktop-bin.repo
BuildArch: noarch

%description
YUM config to define the chinese-opendesktop-bin repository.

%prep

%build

%install
install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/chinese-opendesktop-bin.repo

%files
%{_sysconfdir}/yum.repos.d/chinese-opendesktop-bin.repo

%changelog
* Wed Nov 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 25
- Update package
