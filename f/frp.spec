%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Name:           frp
Version:        0.46.0
Release:        1
Summary:        Reverse proxy to expose local server behind NAT/firewall to Internet
License:        Apache 2.0
URL:            https://github.com/fatedier/frp
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  golang

%description
frp is a fast reverse proxy to help you expose a local server behind a NAT or
firewall to the Internet. As of now, it supports TCP and UDP, as well as HTTP
and HTTPS protocols, where requests can be forwarded to internal services by
domain name.

%prep
%autosetup

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
#make_install
install -d %{buildroot}%{_bindir}
install -m755 bin/* %{buildroot}%{_bindir}

%files
%license LICENSE
%doc doc/* *.md
%{_bindir}/%{name}*

%changelog
* Sun Jan 15 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.46.0
- Rebuilt for Fedora
