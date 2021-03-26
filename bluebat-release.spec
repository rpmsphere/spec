Name: bluebat-release
Version: 21
Release: 1
Summary: Personal repositories from Bluebat
License: Public Domain
Source0: bluebat.repo
BuildArch: noarch

%description
YUM configs to define the personal repositories:
* bluebat-copr for good packaged
* bluebat-obs for bad packaged
* bluebat-dropbox for ugly packaged

%prep

%build

%install
install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/bluebat.repo

%files
%{_sysconfdir}/yum.repos.d/bluebat.repo

%changelog
* Wed Jan 07 2015 Wei-Lun Chao <bluebat@member.fsf.org> 21
- Initial package
