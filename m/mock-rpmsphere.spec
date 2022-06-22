Name:           mock-rpmsphere
Version:        36
Release:        1
Summary:        Mock config files for the RPM Sphere Repository
License:        BSD
URL:            https://rpmsphere.github.io/
Source0:        %{name}-%{version}.zip
BuildArch:      noarch
Requires:       mock-rpmfusion-nonfree

%description
Mock config files for the RPM Sphere Repository

%prep
%setup -q -c

%build
#Nothing to build

%install
mkdir -p %{buildroot}%{_sysconfdir}/mock
install -pm 0644 *.cfg %{buildroot}%{_sysconfdir}/mock

%files
%config(noreplace) %{_sysconfdir}/mock/*.cfg

%changelog
* Sun May 22 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 36
- Initial package
