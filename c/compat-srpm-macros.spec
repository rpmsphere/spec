Name:           compat-srpm-macros
Version:        2015
Release:        1%{?dist}
Summary:        RPM macros for building compat packages from various distributions
Group:          Development/Libraries
License:        GPLv3+
Source0:        macros.compat-srpm
BuildArch:      noarch

%description
The package provides macros for building compatible projects
from various distributions.

%prep

%build

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.compat-srpm

%files
%{_rpmconfigdir}/macros.d/macros.compat-srpm

%changelog
* Tue Dec 23 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2015
- Initial package
