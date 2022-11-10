Name:		compat-srpm-macros
Version:	2022.10
Release:	1
Summary:	RPM macros for compatible building
Group:		Applications/Engineering
License:	MIT License
Source0:	macros.compat-srpm
BuildArch:	noarch

%description
macros.compat-srpm provides macros for building compatible projects from
various distributions.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.compat-srpm
   
%clean 
rm -rf $RPM_BUILD_ROOT

%files
%{_rpmconfigdir}/macros.d/macros.compat-srpm

%changelog
* Sun Oct 30 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2022.10
- Rebuilt for Fedora
