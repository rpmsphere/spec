%global debug_package %{nil}

Name: crosswalk
Summary: An app runtime based on Chromium
Version: 19.48.492.0
Release: 1.bin
Group: Web Framework/Web Run Time
License: BSD-3-Clause
URL: https://github.com/otcshare/crosswalk
Source0: https://download.01.org/crosswalk/releases/crosswalk/linux/deb/canary/%{version}/%{name}_%{version}-1_amd64.deb
Source1: https://download.01.org/crosswalk/releases/crosswalk/linux/deb/canary/%{version}/%{name}_%{version}-1_i386.deb
AutoReqProv: off

%description
Crosswalk is an app runtime based on Chromium. It is an open source project
started by the Intel Open Source Technology Center (http://www.01.org).

%prep
%setup -T -c
%ifarch x86_64
ar -x %{SOURCE0}
%else
ar -x %{SOURCE1}
%endif

%build

%install
mkdir -p $RPM_BUILD_ROOT
tar xf data.tar.?z -C $RPM_BUILD_ROOT

%files
/opt/crosswalk-project
%{_bindir}/xwalk
%{_datadir}/doc/crosswalk/changelog.Debian.gz

%changelog
* Thu Mar 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 19.48.492.0
- Initial binary package
