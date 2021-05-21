Name:           mock-rpmsphere
Version:        34
Release:        1
Summary:        Mock config files for the RPM Sphere Repository
License:        BSD
URL:            mock-rpmfusion-nonfree.spec
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
* Sun Apr 18 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 34
- Initial package
