Name:           compat-srpm-macros
Version:        2024.03
Release:        1
Summary:        RPM macros for compatible building
Group:          Applications/Engineering
License:        MIT License
Source0:        macros.compat-srpm
Source1:        LICENSE.MIT
BuildArch:      noarch

%description
macros.compat-srpm provides macros for building projects from
various distributions compatibly.

%prep
%setup -cT
cp %{SOURCE1} LICENSE

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.compat-srpm
   
%files
%doc LICENSE
%{_rpmconfigdir}/macros.d/macros.compat-srpm

%changelog
* Sun Mar 10 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2024.03
- Rebuilt for Fedora
